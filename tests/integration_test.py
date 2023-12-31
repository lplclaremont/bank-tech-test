import sys
sys.path.insert(0, '../')

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
        expected_str = "date || credit || debit || balance\n10/10/2023 || 1000.00 || || 1000.00"
        self.assertEqual(statement.view(), expected_str)

    @freeze_time("2023-10-10")
    def test_statement_after_multiple_transactions(self):
        account = Account()
        account.deposit(1000)
        account.deposit(500)
        account.withdraw(2000)
        statement = BankStatement(account)
        expected_str = "\n".join([
            "date || credit || debit || balance",
            "10/10/2023 || || 2000.00 || -500.00",
            "10/10/2023 || 500.00 || || 1500.00",
            "10/10/2023 || 1000.00 || || 1000.00"
        ])
        self.assertEqual(statement.view(), expected_str)

    @freeze_time("2023-10-10")
    def test_statement_after_transactions_with_decimal_places(self):
        account = Account()
        account.deposit(1000.01)
        account.deposit(500.05)
        account.withdraw(2000.1)
        statement = BankStatement(account)
        expected_str = "\n".join([
            "date || credit || debit || balance",
            "10/10/2023 || || 2000.10 || -500.04",
            "10/10/2023 || 500.05 || || 1500.06",
            "10/10/2023 || 1000.01 || || 1000.01"
        ])
        self.assertEqual(statement.view(), expected_str)

    def test_statement_with_multiple_transaction_dates(self):
        account = Account()
        with freeze_time("2023-10-12"):
            account.deposit(1000)

        with freeze_time("2023-10-13"):
            account.deposit(500)

        with freeze_time("2023-10-14"):
            account.withdraw(2000)

        expected_str = "\n".join([
            "date || credit || debit || balance",
            "14/10/2023 || || 2000.00 || -500.00",
            "13/10/2023 || 500.00 || || 1500.00",
            "12/10/2023 || 1000.00 || || 1000.00"
        ])
        statement = BankStatement(account)
        self.assertEqual(statement.view(), expected_str)

if __name__ == '__main__':
    unittest.main()
