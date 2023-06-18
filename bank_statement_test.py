import unittest
from unittest.mock import Mock
from src.account import Account
from src.transaction import Transaction
from src.bank_statement import BankStatement

class TestBankStatement(unittest.TestCase):
    """Testing the get_statement method returns correct string"""
    
    def test_initial_blank_statement(self):
        print("IN TEST")
        mock_account = Mock(spec=Account)
        statement = BankStatement(mock_account)
        expected_str = "date || credit || debit || balance"
        self.assertEqual(statement.view(), expected_str)
        
    
    # def test_statement_initial_columns(self):
    #     account = Account()
    #     expected_str = "date || credit || debit || balance"
    #     self.assertEqual(account.get_statement(), expected_str)

if __name__ == '__main__':
    unittest.main()