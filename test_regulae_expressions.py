from unittest import TestCase, main
import regular_expressions as regex 
import re
import operator as op
ops: dict = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.itruediv,
    "**": op.pow
}
class TestRegEx(TestCase):
    def test_pythonic_name_true(self):
        self.assertTrue(re.fullmatch(regex.pythonicNameRe(),"__"))
        self.assertTrue(re.fullmatch(regex.pythonicNameRe(),"a"))
        self.assertTrue(re.fullmatch(regex.pythonicNameRe(),"_aA12"))
        self.assertTrue(re.fullmatch(regex.pythonicNameRe(),"__a__"))
    def test_pythonic_name_false(self):
        self.assertFalse(re.fullmatch(regex.pythonicNameRe(),"1_"))
        self.assertFalse(re.fullmatch(regex.pythonicNameRe(),"a b"))
        self.assertFalse(re.fullmatch(regex.pythonicNameRe(),"$a12"))  
        self.assertFalse(re.fullmatch(regex.pythonicNameRe(),"a*b")) 
    def test_password_true(self) :
        self.assertTrue(re.fullmatch(regex.passwordRe(), "Aa123#57")) 
        self.assertTrue(re.fullmatch(regex.passwordRe(), "Aa123#57--")) 
    def test_password_false(self) :
        self.assertFalse(re.fullmatch(regex.passwordRe(), "aa123#57")) 
        self.assertFalse(re.fullmatch(regex.passwordRe(), "Aa123#57 "))
        self.assertFalse(re.fullmatch(regex.passwordRe(), "Aa123#5")) 
        self.assertFalse(re.fullmatch(regex.passwordRe(), "AaBBB###")) 
        self.assertFalse(re.fullmatch(regex.passwordRe(), "aa12357CD1")) 
    def test_ipV4_true(self) :
        self.assertTrue(re.fullmatch(regex.ipV4AddressRe(), "0.0.0.0")) 
        self.assertTrue(re.fullmatch(regex.ipV4AddressRe(), "0.01.002.000")) 
        self.assertTrue(re.fullmatch(regex.ipV4AddressRe(), "000.1.249.59")) 
        self.assertTrue(re.fullmatch(regex.ipV4AddressRe(), "250.255.199.9"))
    def test_ipV4_false(self) :
        self.assertFalse(re.fullmatch(regex.ipV4AddressRe(), "0.0.0")) 
        self.assertFalse(re.fullmatch(regex.ipV4AddressRe(), "0000.0.0.2"))  
        self.assertFalse(re.fullmatch(regex.ipV4AddressRe(), "0.0.0.256"))
        self.assertFalse(re.fullmatch(regex.ipV4AddressRe(), "0.0 0.2"))
        self.assertFalse(re.fullmatch(regex.ipV4AddressRe(), "0.0.0.280"))
        self.assertFalse(re.fullmatch(regex.ipV4AddressRe(), "0.0.0.0001"))
        self.assertFalse(re.fullmatch(regex.ipV4AddressRe(), "0.0.0. 190"))
        self.assertFalse(re.fullmatch(regex.ipV4AddressRe(), "0.0.0.+1"))
        self.assertFalse(re.fullmatch(regex.ipV4AddressRe(), "0.0.0.a"))
    def test_mobile_israel_true(self):
        self.assertTrue(re.fullmatch(regex.mobileIsraelNumberRe(), "+972-54-1234567"))
        self.assertTrue(re.fullmatch(regex.mobileIsraelNumberRe(), "+972-541234567")) 
        self.assertTrue(re.fullmatch(regex.mobileIsraelNumberRe(), "+972-541234567"))
        self.assertTrue(re.fullmatch(regex.mobileIsraelNumberRe(), "059123-45-67")) 
        self.assertTrue(re.fullmatch(regex.mobileIsraelNumberRe(), "054-1-23-45-67"))
        self.assertTrue(re.fullmatch(regex.mobileIsraelNumberRe(), "0571-23-45-67"))
    def test_mobile_israel_false(self):
        self.assertFalse(re.fullmatch(regex.mobileIsraelNumberRe(), "+972-054-1234567"))
        self.assertFalse(re.fullmatch(regex.mobileIsraelNumberRe(), "+972-54-1-234-567")) 
        self.assertFalse(re.fullmatch(regex.mobileIsraelNumberRe(), "+972-54123456"))
        self.assertFalse(re.fullmatch(regex.mobileIsraelNumberRe(), "059123-45-677")) 
        self.assertFalse(re.fullmatch(regex.mobileIsraelNumberRe(), "054-1-2-3-45-67"))
        self.assertFalse(re.fullmatch(regex.mobileIsraelNumberRe(), "0571-23-45-6-7")) 
    def test_arithmetic_operand(self):
        self.assertTrue(re.fullmatch(regex.arithmeticOperandRe(), "42") ) 
        self.assertTrue(re.fullmatch(regex.arithmeticOperandRe(), " 42 ") ) 
        self.assertTrue(re.fullmatch(regex.arithmeticOperandRe(), "(42)") )
        self.assertTrue(re.fullmatch(regex.arithmeticOperandRe(), " ( 42 )") ) 
        self.assertTrue(re.fullmatch(regex.arithmeticOperandRe(), "42.5") ) 
        self.assertTrue(re.fullmatch(regex.arithmeticOperandRe(), "42.555e+20") )
        self.assertFalse(re.fullmatch(regex.arithmeticOperandRe(), "42 5") ) 
        self.assertFalse(re.fullmatch(regex.arithmeticOperandRe(), "") ) 
        self.assertFalse(re.fullmatch(regex.arithmeticOperandRe(), "()") )
        self.assertFalse(re.fullmatch(regex.arithmeticOperandRe(), ")42.5") ) 
        self.assertFalse(re.fullmatch(regex.arithmeticOperandRe(), "42&5") ) 
        self.assertFalse(re.fullmatch(regex.arithmeticOperandRe(), "42.555(") )
    def test_arithmetic_operator(self):
        operatorRe = regex.arithmeticOperatorRe(ops)
        self.assertTrue(re.fullmatch(operatorRe, "**"))
        self.assertTrue(re.fullmatch(operatorRe, "+"))
        self.assertTrue(re.fullmatch(operatorRe, "*"))
        self.assertTrue(re.fullmatch(operatorRe, "-"))
        self.assertTrue(re.fullmatch(operatorRe, "/")) 
        
        self.assertFalse(re.fullmatch(operatorRe, "++"))
        self.assertFalse(re.fullmatch(operatorRe, "//"))  
    def test_arithmetic_expression(self):
        arithmeticExpr = regex.arithmeticExpression(ops)
        self.assertTrue(re.fullmatch(arithmeticExpr, "3+4-7")) 
        self.assertTrue(re.fullmatch(arithmeticExpr, "3 + 4 - 7.5")) 
        self.assertTrue(re.fullmatch(arithmeticExpr, "10"))
        self.assertTrue(re.fullmatch(arithmeticExpr, "3+(4-7)"))
        self.assertTrue(re.fullmatch(arithmeticExpr,"(3 + (2 * 10 / (40 - 20))+(3 * 4)) * 10" ))
        self.assertTrue(re.fullmatch(arithmeticExpr,"(3 ** (2.3 * 10.8 / (40 - 20))+(3 * 4)) * (10/3)" )) 
        self.assertFalse(re.fullmatch(arithmeticExpr,"(3 ** (2.3 * 1 0.8 / (40 - 20)) +(3 * 4)) * (10/3)" )) 
        self.assertFalse(re.fullmatch(arithmeticExpr,"(3 ** (2.3 * 10.8 & (40 - 20))+(3 * 4)) * (10/3)" )) 
         
                              
          