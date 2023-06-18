import unittest
from freezegun import freeze_time
from datetime import date
from src.transaction import Transaction
from src.account import Account

class TestAccount(unittest.TestCase):
    
    def test_initial_balance(self):
        account = Account()
        self.assertEqual(account.get_balance(), 0)