import unittest
from src.transaction import Transaction

class TestTransaction(unittest.TestCase):
    transaction = Transaction(100)
    def test_amount(self):
        transaction = Transaction(100)
        self.assertEqual(transaction.amount, 100)

if __name__ == '__main__':
    unittest.main()
