from unittest import TestCase, main
import regular_expressions as regex 
import re
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
          