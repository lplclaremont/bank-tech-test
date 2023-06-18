from .account import Account

class BankStatement:
    def __init__(self, account):
        self.account = account
        self.statement = "date || credit || debit || balance"
    
    def view(self):
        return self.statement

    def __format_transaction(self, transaction):
        arr = self.__get_transaction_details_array(transaction)
        return " || ".join(arr)
    
    def __get_transaction_details_array(self, transaction):
        date = transaction.get_date()
        amount = transaction.get_amount()
        balance = self.get_balance()
        if amount > 0:
            return [date, str(amount), "", str(balance)]
        else:
          return [date, "", str(-amount), str(balance)]
        
    