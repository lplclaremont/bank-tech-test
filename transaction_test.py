import unittest
from src.transaction import Transaction

class TestTransaction(unittest.TestCase):
    transaction = Transaction(100)
    def test_valid_amount(self):
        transaction = Transaction(100)
        self.assertEqual(transaction.amount, 100)
    def test_negative_amount(self):
        transaction = Transaction(-100)
        self.assertEqual(transaction.amount, -100)
    def test_invalid_amount(self):
        with self.assertRaises(Exception):
            transaction = Transaction()

    def test_date_format(self):
        with self.assertRaises(Exception):
            transaction = Transaction('five')

if __name__ == '__main__':
    unittest.main()
