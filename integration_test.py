import unittest
from freezegun import freeze_time
from src.account import Account
from src.bank_statement import BankStatement

class TestIntegration(unittest.TestCase):
    """Testing the BankStatement class properly displays
    the statement based on given deposits and withdrawals"""

    def test_initial_blank_statement(self):
        account = Account()
        statement = BankStatement(account)
        expected_str = "date || credit || debit || balance\n"
        self.assertEqual(statement.view(), expected_str)

    @freeze_time("2023-10-10")
    def test_statement_after_one_deposit(self):
        account = Account()
        account.deposit(1000)
        statement = BankStatement(account)
        expected_str = "date || credit || debit || balance\n23/10/10 || 1000.00 || || 1000.00"
        self.assertEqual(statement.view(), expected_str)

if __name__ == '__main__':
    unittest.main()
