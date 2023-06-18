import unittest
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
        
        

if __name__ == '__main__':
    unittest.main()