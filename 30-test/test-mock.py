import unittest
from unittest.mock import MagicMock

class A(unittest.TestCase):
    def m1(self):
        val = self.m2()
        self.m3(val)

    def m2(self):
        pass

    def m3(self, val):
        pass

    def test_m1(self):
        a = A()
        a.m2 = MagicMock(return_value="custom_val")
        a.m3 = MagicMock()
        a.m1()
        self.assertTrue(a.m2.called) # 验证 m2 被 call 过
        a.m3.assert_called_with("custom_val") # 验证 m3 被指定参数 call 过

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)