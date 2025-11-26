import operator as op
import regular_expressions as regexp
import re
PAIRING_ERROR = "Parentheses Pairing Error"
__ops: dict = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.itruediv,
    "**": op.pow
}
__exprPattern = re.compile(regexp.arithmeticExpression(__ops))
__operatorDelimPattern = re.compile(rf"(?<=\d){regexp.arithmeticOperatorRe(__ops)}")
__operandPattern = re.compile(rf"(?<!\d)-?{regexp.numberRe()}")


def __binCompute(op1: float, op2: int, operation: float) -> float:
    """ evaluation of binary operator

    Args:
        op1 (int): first number
        op2 (int): second number
        operation (str): code of operation from ops defined above
    """
    operator = __ops.get(operation)
    if not operator:
        raise ValueError(f"{operation} not found")
    return operator(op1, op2)
def __checkPairing(expr: str):
    count: int = 0
    for ch in expr:
        if ch == "(":
            count += 1
        elif ch == ")":
            count -= 1
        if count < 0: raise ValueError(PAIRING_ERROR) 
    if count != 0: raise ValueError(PAIRING_ERROR)       

def __ltrEvaluationNoParentheses(expr: str) -> float:
    """Left to right expression evaluation in accordance with the above ops
        Assumed that all operators (ops) have the same preference
    Args:
        expr (str): expression with no parentheses, for example 10 + 5 * 10 / 15 -> 10
    """
    
    operands: list[str] = re.split(__operatorDelimPattern, expr)
    operators: list[str] = re.split(__operandPattern, expr)
    res = float(operands[0])
    for i in range(1, len(operands)):
        res = __binCompute(res, float(operands[i]), operators[i])
    return res



    

def ltrEvaluation(expr: str) -> int:
    """evaluation of expression containing parentheses 
     example: 3 + (2 * 10 / (40 - 20))+(3 * 4)
     replacing expressions inside parentheses with evaluation results
    Args:
        expr (str): _description_

    Returns:
        int: result of evaluation
    """
    __checkPairing(expr)
    if not re.fullmatch(__exprPattern, expr):
        raise ValueError(f"'syntax error in {expr}' ")
    expr = re.sub(r"\s+", "", expr)
    while mo := re.search(r"\([^()]+\)", expr):
        inner = mo.group()[1:-1]  # removing ()
        value = __ltrEvaluationNoParentheses(inner)
        expr = expr[:mo.start()] + str(value) + expr[mo.end():]
    return __ltrEvaluationNoParentheses(expr)
