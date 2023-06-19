# from src.account import Account

class BankStatement:
    def __init__(self, account):
        self.account = account
        self.header = "date || credit || debit || balance\n"
    
    def view(self):
        transactions = self.account.activity_log
        transaction_strings = map(self.__get_transaction_row, transactions[::-1])

        return self.header + "\n".join(transaction_strings)
    
    # private
    def __get_transaction_row(self, activity):
        date = activity["transaction"].date
        amount = activity["transaction"].amount
        balance = self.__float_to_two_dp(activity["balance"])
        if amount > 0:
            amount_str = self.__float_to_two_dp(amount)
            return f'{date} || {amount_str} || || {str(balance)}'
        else:
            amount_str = self.__float_to_two_dp(-amount)
            return f'{date} || || {amount_str} || {str(balance)}'
        
    def __float_to_two_dp(self, float):
        return "{:.2f}".format(float)