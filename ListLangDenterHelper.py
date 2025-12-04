from typing import Optional, List
from antlr4 import Token
from antlr4.Token import CommonToken


class ListLangDenterHelper:
    """
    Помощник для обработки отступов в ListLang (по аналогии с Python)
    """
    
    def __init__(self, lexer, nl_token: int, indent_token: int, dedent_token: int, ignore_eof: bool = False):
        self.lexer = lexer
        self.nl_token = nl_token
        self.indent_token = indent_token
        self.dedent_token = dedent_token
        self.ignore_eof = ignore_eof
        
        self.token_queue: List[Token] = []
        self.indent_stack: List[int] = [0]
        self.reached_eof = False
        self.paren_level = 0
        self.at_line_start = True  # Флаг начала строки
        self.pending_tokens: List[Token] = []  # Буфер для накопления токенов
        
    def next_token(self) -> Token:
        """Возвращает следующий токен с учетом INDENT/DEDENT"""
        # Если в очереди есть токены, возвращаем их
        if self.token_queue:
            return self.token_queue.pop(0)
        
        # Получаем следующий токен от базового лексера
        token = self.pull_token()
        
        # Обрабатываем EOF
        if token.type == Token.EOF:
            return self.handle_eof(token)
        
        # Обрабатываем скобки
        self.handle_parentheses(token)
        
        # Обрабатываем NEWLINE
        if token.type == self.nl_token:
            # Если внутри скобок — просто пропускаем как обычный NEWLINE
            if self.paren_level > 0:
                self.at_line_start = False
                return token
            # Вне скобок NEWLINE переводит нас в начало логической строки.
            self.at_line_start = True
            # Важный момент: после NEWLINE могут идти еще пустые строки и комментарии.
            # Мы возвращаем сам NEWLINE, но не трогаем INDENT/DEDENT, пока не встретим значимый токен.
            return token
    
        # Если мы в начале строки и не внутри скобок
        if self.at_line_start and self.paren_level == 0:
            # Не сбрасываем флаг раньше времени — handle_indent сам вернет первый токен и поставит очередь.
            return self.handle_indent(token)
    
        self.at_line_start = False
        return token

    def handle_eof(self, eof_token: Token) -> Token:
        """Обрабатывает конец файла"""
        if not self.reached_eof:
            self.reached_eof = True
        
            # Генерируем DEDENT для всех незакрытых уровней
            if not self.ignore_eof:
                while len(self.indent_stack) > 1:
                    self.indent_stack.pop()
                    self.token_queue.append(self.create_token(self.dedent_token, eof_token))
            
                if self.token_queue:
                    self.token_queue.append(eof_token)
                    return self.token_queue.pop(0)
    
        return eof_token

    def handle_parentheses(self, token: Token):
        """Обрабатывает открытие/закрытие скобок"""
        if token.type in [self.lexer.OPEN_PAREN, self.lexer.OPEN_BRACE, self.lexer.OPEN_BRACKET]:
            self.paren_level += 1
        elif token.type in [self.lexer.CLOSE_PAREN, self.lexer.CLOSE_BRACE, self.lexer.CLOSE_BRACKET]:
            self.paren_level -= 1

    def handle_indent(self, first_token_on_line: Token) -> Token:
        """
        Обрабатывает отступы в начале логической строки.
        Важно: COMMENT и пустые строки не должны приводить к генерации INDENT/DEDENT.
        """
        # Мы уже получили первый токен после NEWLINE или это старт файла.
        # Но если это комментарий/еще один NEWLINE (например, предыдущий был возвращен в поток),
        # следует просто вернуть его без изменения отступов.
        if first_token_on_line.type == self.nl_token:
            # Остаемся в начале строки до первого значимого токена
            self.at_line_start = True
            return first_token_on_line

        # Комментарии у вас skip-аются в лексере, сюда они не попадут.
        # WS тоже skip-ается, поэтому полагаться на column всё же можно:
        # column у первого значимого токена — это число ведущих пробелов до него.
        indent_level = first_token_on_line.column
        current_indent = self.indent_stack[-1]
    
        result_tokens: List[Token] = []

        if indent_level > current_indent:
            # Увеличение отступа - INDENT
            self.indent_stack.append(indent_level)
            result_tokens.append(self.create_token(self.indent_token, first_token_on_line))
            result_tokens.append(first_token_on_line)
        elif indent_level < current_indent:
            # Уменьшение отступа - один или несколько DEDENT
            while len(self.indent_stack) > 1 and self.indent_stack[-1] > indent_level:
                self.indent_stack.pop()
                result_tokens.append(self.create_token(self.dedent_token, first_token_on_line))
        
            # Проверка на корректность отступа
            if self.indent_stack[-1] != indent_level:
                raise Exception(f"Indentation error at line {first_token_on_line.line}: inconsistent indentation")
        
            result_tokens.append(first_token_on_line)
        else:
            # Отступ не изменился
            result_tokens.append(first_token_on_line)
    
        # Первый токен возвращаем, остальные в очередь
        if len(result_tokens) > 1:
            for t in result_tokens[1:]:
                self.token_queue.append(t)

        # После обработки начала строки мы больше не на начале строки
        self.at_line_start = False
        return result_tokens[0]

    def pull_token(self) -> Token:
        """Получает следующий токен от базового лексера"""
        token = super(type(self.lexer), self.lexer).nextToken()
        return token

    def create_token(self, token_type: int, reference_token: Token) -> Token:
        """Создает искусственный токен INDENT или DEDENT"""
        token = CommonToken(
            source=(self.lexer, self.lexer._input),
            type=token_type,
            channel=Token.DEFAULT_CHANNEL,
            start=reference_token.start,
            stop=reference_token.start - 1
        )
        token.line = reference_token.line
        token.column = reference_token.column
        token.text = ("INDENT" if token_type == self.indent_token else "DEDENT")
        return token
