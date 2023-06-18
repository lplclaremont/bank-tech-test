import unittest
from freezegun import freeze_time
from datetime import date
from src.transaction import Transaction

class TestTransaction(unittest.TestCase):
    """Testing the get_amount method returns correct ammount of a
    transaction object and throws an error when input is not valid"""
    def test_valid_amount_input(self):
        transaction = Transaction(100)
        self.assertEqual(transaction.get_amount(), 100)

    def test_negative_amount_input(self):
        transaction = Transaction(-100)
        self.assertEqual(transaction.get_amount(), -100)

    def test_zero_amount_input(self):
        with self.assertRaises(Exception):
            transaction = Transaction(0)

    def test_no_amount_input(self):
        with self.assertRaises(Exception):
            transaction = Transaction()
            
    def test_invalid_input_type(self):
        with self.assertRaises(Exception):
            transaction = Transaction('five')
    
    """Testing the get_date method returns the correct date in the 
    correct format"""
    @freeze_time("2023-06-25")
    def test_date_format(self):
        transaction = Transaction(100)
        self.assertEqual(transaction.get_date(), '23/06/25')

if __name__ == '__main__':
    unittest.main()
