import unittest
from unittest.mock import patch
from freezegun import freeze_time
from datetime import date
from src.account import Account

class TestAccount(unittest.TestCase):
    """Testing the get_balance method of an account is initialised
    at 0 and updates when depositing and withdrawing"""

    def test_initial_balance_zero(self):
        account = Account()
        self.assertEqual(account.get_balance(), 0)

    def test_valid_deposit_input(self):
        account = Account()
        account.deposit(1000)
        self.assertEqual(account.get_balance(), 1000)
    
    def test_negative_deposit_input(self):
        account = Account()
        with self.assertRaises(Exception):
            account.deposit(-10)

    def test_valid_withdraw_input(self):
        account = Account()
        account.deposit(1000)
        account.withdraw(100)
        self.assertEqual(account.get_balance(), 900)

    def test_negative_withdraw_input(self):
        account = Account()
        with self.assertRaises(Exception):
            account.withdraw(-10)

    """Testing the transactions array is populated
    when a deposit or withdrawal is made"""

    def test_initial_transactions_empty(self):
        account = Account()
        transactions = account.transactions
        self.assertEqual(transactions, [])
        
    @patch('src.transaction.Transaction.get_amount')
    def test_transactions_after_deposit(self, mock_get_amount):
        mock_get_amount.return_value = 1000

        account = Account()
        account.deposit(1000)
        transactions = account.transactions

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].get_amount(), 1000)
    
    @patch('src.transaction.Transaction.get_amount')
    def test_transactions_after_withdrawal(self, mock_get_amount):
        mock_get_amount.return_value = -1000

        account = Account()
        account.withdraw(1000)
        transactions = account.transactions

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].get_amount(), -1000)

if __name__ == '__main__':
    unittest.main()