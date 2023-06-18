from account import Account

class StatementView:
    def __init__(self, account):
        self.account = account
    
    def __format_transaction(self, transaction):
        date = transaction.get_date()
        amount = transaction.get_amount()
        balance = self.get_balance()
        if amount > 0:
            arr = [date, str(amount), "", str(balance)]
        else:
          arr = [date, "", str(-amount), str(balance)]
        
        return " || ".join(arr)
    