from dataclasses import dataclass, field
from typing import List, Optional, Any
from enum import Enum


class NodeType(Enum):
    """AST node types."""
    PROGRAM = "program"
    FUNCTION = "function"
    ASSIGNMENT = "assignment"
    EXPRESSION = "expression"
    IF_STATEMENT = "if_statement"
    WHILE_STATEMENT = "while_statement"
    FOR_STATEMENT = "for_statement"
    SWITCH_STATEMENT = "switch_statement"
    BREAK_STATEMENT = "break_statement"
    RETURN_STATEMENT = "return_statement"
    LITERAL = "literal"
    VARIABLE = "variable"
    BINARY_OP = "binary_op"
    UNARY_OP = "unary_op"
    CALL = "call"
    METHOD_CALL = "method_call"


class Type(Enum):
    """Language types."""
    INT = "int"
    BOOL = "bool"
    FLOAT = "float"
    STRING = "string"
    LIST = "list"
    ELEMENT = "element"
    TREE = "tree"
    VOID = "void"
    UNKNOWN = "unknown"


@dataclass
class ASTNode:
    """Base AST node."""
    node_type: NodeType
    line: int = 0
    column: int = 0


@dataclass
class Program(ASTNode):
    """Root node of the AST. """
    functions: List['Function'] = field(default_factory=list)
    statements: List[ASTNode] = field(default_factory=list)

    def __init__(self, functions=None, statements=None):
        super().__init__(NodeType.PROGRAM)
        self.functions = functions or []
        self.statements = statements or []


@dataclass
class Function(ASTNode):
    """AST node representing a function."""
    name: str = ""
    parameters: List['Parameter'] = field(default_factory=list)
    body: List[ASTNode] = field(default_factory=list)
    return_type: Type = Type.VOID

    def __init__(self, name, parameters=None, body=None):
        super().__init__(NodeType.FUNCTION)
        self.name = name
        self.parameters = parameters or []
        self.body = body or []


@dataclass
class Parameter:
    """Function parameter."""
    name: str = ""
    by_reference: bool = False  # True если передача по результату (&)
    type: Type = Type.UNKNOWN


@dataclass
class Assignment(ASTNode):
    """Assignment statement."""
    targets: List[str] = field(default_factory=list)
    values: List[ASTNode] = field(default_factory=list)

    def __init__(self, targets, values):
        super().__init__(NodeType.ASSIGNMENT)
        self.targets = targets
        self.values = values


@dataclass
class IfStatement(ASTNode):
    condition: ASTNode = None
    then_body: List[ASTNode] = field(default_factory=list)
    else_body: List[ASTNode] = field(default_factory=list)

    def __init__(self, condition, then_body, else_body=None):
        super().__init__(NodeType.IF_STATEMENT)
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body or []


@dataclass
class WhileStatement(ASTNode):
    condition: ASTNode = None
    body: List[ASTNode] = field(default_factory=list)

    def __init__(self, condition, body):
        super().__init__(NodeType.WHILE_STATEMENT)
        self.condition = condition
        self.body = body


@dataclass
class ForStatement(ASTNode):
    targets: List[str] = field(default_factory=list)
    iterables: List[ASTNode] = field(default_factory=list)
    body: List[ASTNode] = field(default_factory=list)

    def __init__(self, targets, iterables, body):
        super().__init__(NodeType.FOR_STATEMENT)
        self.targets = targets
        self.iterables = iterables
        self.body = body


@dataclass
class SwitchStatement(ASTNode):
    expression: ASTNode = None
    cases: List['CaseBlock'] = field(default_factory=list)
    default_case: Optional[List[ASTNode]] = None

    def __init__(self, expression, cases, default_case=None):
        super().__init__(NodeType.SWITCH_STATEMENT)
        self.expression = expression
        self.cases = cases
        self.default_case = default_case


@dataclass
class CaseBlock:
    value: ASTNode
    body: List[ASTNode] = field(default_factory=list)


@dataclass
class ReturnStatement(ASTNode):
    values: Optional[ASTNode] = field(default_factory=list)

    def __init__(self, values):
        super().__init__(NodeType.RETURN_STATEMENT)
        self.values = values


@dataclass
class BreakStatement(ASTNode):
    def __init__(self):
        super().__init__(NodeType.BREAK_STATEMENT)


@dataclass
class Literal(ASTNode):
    value: Any = None
    type: Type = Type.UNKNOWN

    def __init__(self, value, value_type):
        super().__init__(NodeType.LITERAL)
        self.value = value
        self.type = value_type


@dataclass
class Variable(ASTNode):
    name: str = ""
    var_type: Type = Type.UNKNOWN

    def __init__(self, name):
        super().__init__(NodeType.VARIABLE)
        self.name = name


@dataclass
class BinaryOp(ASTNode):
    operator: str = ""
    left: ASTNode = None
    right: ASTNode = None

    def __init__(self, operator, left, right):
        super().__init__(NodeType.BINARY_OP)
        self.operator = operator
        self.left = left
        self.right = right


@dataclass
class UnaryOp(ASTNode):
    operator: str = ""
    operand: ASTNode = None
    result_type: Type = Type.UNKNOWN

    def __init__(self, operator, operand):
        super().__init__(NodeType.UNARY_OP)
        self.operator = operator
        self.operand = operand


@dataclass
class FunctionCall(ASTNode):
    name: str = ""
    arguments: List[ASTNode] = field(default_factory=list)
    return_type: Type = Type.UNKNOWN

    def __init__(self, name, arguments):
        super().__init__(NodeType.CALL)
        self.name = name
        self.arguments = arguments


@dataclass
class MethodCall(ASTNode):
    object_name: str = ""
    method_name: str = ""
    arguments: List[ASTNode] = field(default_factory=list)
    return_type: Type = Type.UNKNOWN

    def __init__(self, object_name, method_name, arguments):
        super().__init__(NodeType.METHOD_CALL)
        self.object_name = object_name
        self.method_name = method_name
        self.arguments = arguments

class MemberAccess(ASTNode):
    object_name: str = ""
    member_name: str = ""

    def __init__(self, object_name, member_name):
        super().__init__(NodeType.VARIABLE)
        self.object_name = object_name
        self.member_name = member_name

