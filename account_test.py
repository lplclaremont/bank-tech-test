import unittest
from freezegun import freeze_time
from datetime import date
from src.account import Account

class TestAccount(unittest.TestCase):
    def test_initial_balance(self):
        account = Account()
        self.assertEqual(account.get_balance(), 0)

if __name__ == '__main__':
    unittest.main()