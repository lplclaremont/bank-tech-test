from .account import Account

class BankStatement:
    def __init__(self, account):
        self.account = account
        self.header = "date || credit || debit || balance\n"
    
    def view(self):
        transactions = self.account.transactions_and_balance
        transactions.reverse()
        transaction_strings = map(self.__format_transaction, transactions)

        return self.header + "\n".join(transaction_strings)   

    def __format_transaction(self, transaction):
        arr = self.__get_transaction_details_array(transaction)
        return " || ".join(arr)
    
    def __get_transaction_details_array(self, transaction_pair):
        date = transaction_pair[0].get_date()
        amount = transaction_pair[0].get_amount()
        current_balance = transaction_pair[1]
        if amount > 0:
            return [date, str(amount), "", str(current_balance)]
        else:
            return [date, "", str(-amount), str(current_balance)]
        
    