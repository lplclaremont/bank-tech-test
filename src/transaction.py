from datetime import date
class Transaction:
    def __init__(self, amount):
        if (type(amount) != int) or (amount == 0):
            raise Exception("Input must be a non zero integer")
        self.amount = amount

    def date(self):
        today = date.today()
        return today.strftime("%y/%m/%d")
    