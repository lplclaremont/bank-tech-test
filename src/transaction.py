from datetime import date
class Transaction:
    def __init__(self, amount):
        self.__check_input(amount)
        self.set_date()
        self.amount = float(amount)

    def set_date(self):
        today = date.today()
        self.date = today.strftime("%d/%m/%Y")
    
    # private

    # checks for invalid input: whether amount is zero, whether it is 
    # a float with more than 2 decimal places and finally
    # whether it is neither an integer or a float
    def __check_input(self, amount):
        if (amount == 0):
            raise Exception("Input must be a non zero integer")
        
        elif (type(amount) == float) and len(str(amount).rsplit('.')[-1]) > 2:
            raise Exception("Must contain no more than 2 decimal places")
        
        elif type(amount) != int and type(amount) != float:
            raise Exception("Must be a number input")
        
    