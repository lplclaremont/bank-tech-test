import unittest
from unittest.mock import patch
from src.account import Account

class TestAccount(unittest.TestCase):
    """Testing the .balance attribute of an account is initialised
    at 0 and updates when depositing and withdrawing"""

    def test_initial_balance_zero(self):
        account = Account()
        self.assertEqual(account.balance, 0)

    def test_valid_deposit_input(self):
        account = Account()
        account.deposit(1000)
        self.assertEqual(account.balance, 1000)

    def test_valid_withdraw_input(self):
        account = Account()
        account.deposit(1000)
        account.withdraw(100)
        self.assertEqual(account.balance, 900)

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

    def test_bad_type_deposit_input(self):
        account = Account()
        with self.assertRaises(Exception):
            account.deposit('5')
    
    def test_bad_type_withdraw_input(self):
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
            transactions = account.transactions_and_balance

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