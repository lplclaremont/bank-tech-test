import sys
sys.path.insert(0, '../')

import unittest
from unittest.mock import Mock
from src.account import Account
from src.transaction import Transaction
from src.bank_statement import BankStatement

class TestBankStatement(unittest.TestCase):
    """Testing the view method returns 
    the correct string initially"""
    
    def test_initial_blank_statement(self):
        mock_account = Mock(spec=Account)
        mock_account.activity_log = []

        statement = BankStatement(mock_account)
        expected_str = "date || credit || debit || balance\n"
        self.assertEqual(statement.view(), expected_str)
    
    """Testing the view method after one transaction added"""

    def test_after_one_deposit(self):
        mock_transaction = Mock(spec=Transaction)
        mock_transaction.date = "10/10/2023"
        mock_transaction.amount = 1000

        mock_account = Mock(spec=Account)
        mock_account.activity_log = [
            {"transaction": mock_transaction, "balance": 1000}
            ]

        statement = BankStatement(mock_account)
        expected_str = "date || credit || debit || balance\n10/10/2023 || 1000.00 || || 1000.00"
        self.assertEqual(statement.view(), expected_str)

    """Testing the view method after deposit and a withdrawal"""
    
    def test_after_two_transactions(self):
        mock_transaction_1 = Mock(spec=Transaction)
        mock_transaction_1.date = "10/10/2023"
        mock_transaction_1.amount = 1000

        mock_transaction_2 = Mock(spec=Transaction)
        mock_transaction_2.date = "10/12/2023"
        mock_transaction_2.amount = -500

        mock_account = Mock(spec=Account)
        mock_account.activity_log = [
            {"transaction": mock_transaction_1, "balance": 1000},
            {"transaction": mock_transaction_2, "balance": 500}]

        statement = BankStatement(mock_account)
        expected_str = "\n".join([
            "date || credit || debit || balance",
            "10/12/2023 || || 500.00 || 500.00",
            "10/10/2023 || 1000.00 || || 1000.00"
        ])
        
        self.assertEqual(statement.view(), expected_str)

if __name__ == '__main__':
    unittest.main()