import re
# import regular_expressions as regex
# import operator as op
# ops: dict = {
#     "+": op.add,
#     "-": op.sub,
#     "*": op.mul,
#     "/": op.itruediv,
#     "**": op.pow
# }
# # print (re.split(r"(?<![eE])[+\-*/]", "20+20.5-20.5e+10*4"))
# __operatorDelimPattern = re.compile(r"(?<!^)(?<![eE])[+\-*/]")
# __operandDelimPattern = re.compile(r"(?<!\d)-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?")
# print (re.split(__operatorDelimPattern, '3.5+2*10.45/40.5-40+12.0*20.4'))
# print (re.split(__operandDelimPattern, '10-4'))
# # r"\d+(?:\.\d+)?(?:e[+\-]?\d+)?"
expr = "10-5"

# Split to get operands
OP = r"(?<!^)(?<![eE])(?<=[0-9])[+\-*/](?=\d)"
nums = re.split(OP, expr)

# Split to get operators (with empty strings)
NUM = r"(?<!\d)-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?"
ops = re.split(NUM, expr)

print(nums)  # ['10', '-5']
print(ops)   # ['', '+', '']