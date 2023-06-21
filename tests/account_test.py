import sys
sys.path.insert(0, '../')

import unittest
from unittest.mock import patch
from src.account import Account

class TestAccount(unittest.TestCase):
    """Testing error raise when the deposit or withdrawal
    amount is invalid"""

    def test_negative_deposit_input(self):
        account = Account()
        with self.assertRaises(Exception):
            account.deposit(-10)
    
    def test_negative_withdraw_input(self):
        account = Account()
        with self.assertRaises(Exception):
            account.withdraw(-10)

    def test_too_many_dp_input(self):
        account = Account()
        with self.assertRaises(Exception):
            account.deposit(200.0102)

    def test_invalid_deposit_input_type(self):
        account = Account()
        with self.assertRaises(Exception):
            account.deposit('5')
    
    def test_invalid_withdraw_input_type(self):
        account = Account()
        with self.assertRaises(Exception):
            account.withdraw('5')
    

    """Testing the transactions array is populated
    when a deposit or withdrawal is made"""

    def test_initial_transactions_empty(self):
        account = Account()
        log = account.activity_log
        self.assertEqual(log, [])

    ## We will mock the result of `transaction.amount` in the following
    ## two tests to ensure we are only testing Account class
    ## and not the behaviour of the Transaction class

    def test_transactions_after_deposit(self):
        with patch('src.account.Transaction', autospec=True) as mock_transaction:
            mock_transaction.return_value.amount = 1000
            account = Account()
            account.deposit(1000)
            transactions = account.activity_log

            self.assertEqual(len(transactions), 1)
            self.assertEqual(transactions[0][0].amount, 1000)
        
    def test_transactions_after_deposit(self):
        with patch('src.account.Transaction', autospec=True) as mock_transaction:
            mock_transaction.return_value.amount = -1000
            account = Account()
            account.withdraw(1000)
            log = account.activity_log
            transaction = log[0]["transaction"]

            self.assertEqual(len(log), 1)
            self.assertEqual(transaction.amount, -1000)

if __name__ == '__main__':
    unittest.main()