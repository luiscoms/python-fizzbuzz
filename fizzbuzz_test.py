import unittest

from ddt import ddt, data

from fizzbuzz import fizzbuzz


@ddt
class FizzBuzzTest(unittest.TestCase):

    @data(1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19)
    def test_number_not_divisible_by_three_nor_five_should_be_equal(self, number):
        self.assertEqual(str(number), fizzbuzz(number))

    def test_one_should_be_one(self):
        number = 1
        self.assertEqual("1", fizzbuzz(number))

    @data(3, 6, 9, 12, 18)
    def test_number_divisible_by_three_should_be_fizz(self, number):
        self.assertEqual("Fizz", fizzbuzz(number))

    @data(5, 10, 20, 25)
    def test_number_divisible_by_five_should_be_fizz(self, number):
        self.assertEqual("Buzz", fizzbuzz(number))

    @data(15, 30, 45)
    def test_number_divisible_by_fifteen_should_be_fizzbuzz(self, number):
        self.assertEqual("FizzBuzz", fizzbuzz(number))


if __name__ == '__main__':
    unittest.main()
