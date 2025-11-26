import re


def pythonicNameRe() -> str:
    return r"[A-Za-z_]\w*"


def passwordRe():
    return r"(?=.*[A-Z])(?=.*[a-z])(?=.*[#$%])(?=.*[\d])[A-Za-z#$%\d_-]{8,}"


def ipV4Octet() -> str:
    return r"([0-1]?\d{1,2}|2([0-4]\d|5[0-5]))"


def ipV4AddressRe() -> str:
    """returns regexp as match pattern of IPv4 address
       comprises of 4 octets separated by dot
       each octet contains 1-3 symbols from 0 to 255
    """
    octet_grp = ipV4Octet()
    return rf"({octet_grp}\.){{3}}{octet_grp}"


def mobileIsraelNumberRe() -> str:
    """returns regexp for mobile phone Israel number
       +972- - Israel preffix (not mandatary)
       Operator preffix 0 (only without +972-)
       50,51, 52, 53, 54, 55, 56, 57,58, 59
       optional dash
       7 digits as follows
       xxxxxxx
       xxx-xx-xx
       x-xx-xx-xx
    """
    return r"(\+972-?|0)5\d-?\d-?\d{2}-?\d{2}-?\d{2}"

def numberRe():
    return r"\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?"
def arithmeticOperandRe() -> str:
    number: str =numberRe()
    return rf"\s*\(*\s*{number}\s*\)*\s*"


def arithmeticOperatorRe(ops) -> str:
    op_symbols = sorted(ops.keys(), key=len, reverse=True)
    return  rf"(?:{'|'.join(re.escape(op) for op in op_symbols)})"

def arithmeticExpression(ops) -> str:
    operand = arithmeticOperandRe()
    operator = arithmeticOperatorRe(ops)
    return rf"{operand}({operator}{operand})*"
    
