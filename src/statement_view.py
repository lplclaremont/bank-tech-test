from account import Account

class StatementView:
    def __init__(self, account):
        self.account = account
    
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
        
    