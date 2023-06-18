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
        mock_account.transactions = []
        
        statement = BankStatement(mock_account)
        expected_str = "date || credit || debit || balance\n"
        self.assertEqual(statement.view(), expected_str)
    
    """Testing the view method after one transaction added"""

    def test_after_one_deposit(self):
        mock_transaction = Mock(spec=Transaction)
        mock_transaction.get_date.return_value = "23/10/10"
        mock_transaction.get_amount.return_value = 1000

        mock_account = Mock(spec=Account)
        mock_account.get_balance.return_value = 1000
        mock_account.transactions = [mock_transaction]

        statement = BankStatement(mock_account)
        expected_str = """date || credit || debit || balance\n23/10/10 || 1000 ||  || 1000"""
        self.assertEqual(statement.view(), expected_str)


if __name__ == '__main__':
    unittest.main()