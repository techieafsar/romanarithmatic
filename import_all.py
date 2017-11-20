import check_validity
import roman_to_arabic
import operator_choice
import arabic_to_roman
import unittest


def roman_operations(num1, num2, operator):
    check_validity.roman_validity(num1)
    check_validity.roman_validity(num2)
    operand1 = roman_to_arabic.romantoarabic(num1)
    operand2 = roman_to_arabic.romantoarabic(num2)
    res = operator_choice.operator_sel(operand1, operand2, operator)
    if res > 3999 or res <= 0:    # numbers above 3999 and below 1 are not represented in roman numeric form(non bar)
        raise ValueError(' output is invalid ')
    else:
        fin_res = arabic_to_roman.num_to_roman(res)

    return fin_res


class TestRomanConversion(unittest.TestCase):
    def setUp(self):
        self.numbers_add = [('XL', 'X', 'L'),
                        ('C', 'I', 'CI'),
                        ('C', 'X', 'CX'),
                        ('X', 'X', 'XX'),
                        ('CD', 'XCIX', 'CDXCIX')
                        ]
        self.numbers_sub = [('L', 'X', 'XL'),
                            ('C', 'I', 'XCIX'),
                            ('C', 'X', 'XC'),
                            ('M', 'I', 'CMXCIX'),
                            ('MD', 'CC', 'MCCC')
                            ]
        self.numbers_div = [('L', 'X', 'V'),
                            ('M', 'I', 'M'),
                            ('C', 'X', 'X'),
                            ('M', 'D', 'II'),
                            ('CLXX', 'XVII', 'X')
                            ]

        self.numbers_mul = [('L', 'X', 'D'),
                        ('V', 'I', 'V'),
                        ('C', 'X', 'M'),
                        ('M', 'II', 'MM'),
                        ('CLXX', 'XVII', 'MMDCCCXC')
                        ]

    def test_add(self):
        for num in self.numbers_add:
            self.assertEqual(num[2], roman_operations(num[0], num[1], '+'))

    def test_sub(self):
        for num in self.numbers_sub:
            self.assertEqual(num[2], roman_operations(num[0], num[1], '-'))

    def test_div(self):
        for num in self.numbers_div:
            self.assertEqual(num[2], roman_operations(num[0], num[1], '/'))

    def test_mul(self):
        for num in self.numbers_mul:
            self.assertEqual(num[2], roman_operations(num[0], num[1], '*'))

if __name__ == '__main__':
    unittest.main()

    '''verification can be done using after uncommenting the below lines and commenting just above line'''
    inp1 = input("enter the first roman number:").upper().strip()
    inp2 = input("enter the second roman number:").upper().strip()
    op = input("enter the operator")
    print(roman_operations(inp1, inp2, op))