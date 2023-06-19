from transaction import Transaction
from account import Account
from bank_statement import BankStatement

account = Account()
account.deposit(1000)
account.deposit(30)
account.withdraw(530)
account.withdraw('hi')

statement = BankStatement(account)

print(statement.view())
