# from src.account import Account

class BankStatement:
    def __init__(self, account):
        self.account = account
        self.header = "date || credit || debit || balance\n"
    
    def view(self):
        transactions = self.account.activity_log
        transactions.reverse()
        transaction_strings = map(self.__get_transaction_row, transactions)

        return self.header + "\n".join(transaction_strings)
    
    def __get_transaction_row(self, activity):
        date = activity["transaction"].date
        amount = activity["transaction"].amount
        balance = activity["balance"]
        if amount > 0:
            return f'{date} || {str(amount)} || || {str(balance)}'
        else:
            return f'{date} || || {str(-amount)} || {str(balance)}'
        
    