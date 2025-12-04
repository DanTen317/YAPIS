from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        error = {
            'line': line,
            'column': column,
            'message': msg,
            'symbol': offending_symbol.text if offending_symbol else None
        }
        self.errors.append(error)
        # print(f"Syntax error at {line}:{column}: {msg}")
