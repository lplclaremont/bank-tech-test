# Bank Mock Tech Test

# Overview
This is a first draft of the bank test during Makers Academy. It's specification is as follows:

## Specification

### Requirements

* You should be able to interact with your code via a REPL like IRB or Node.  (You don't need to implement a command line interface that takes input from STDIN.)
* Deposits, withdrawal.
* Account statement (date, amount, balance) printing.
* Data can be kept in memory (it doesn't need to be stored to a database or anything).

### Acceptance criteria

**Given** a client makes a deposit of 1000 on 10-01-2023  
**And** a deposit of 2000 on 13-01-2023  
**And** a withdrawal of 500 on 14-01-2023  
**When** she prints her bank statement  
**Then** she would see

```
date || credit || debit || balance
14/01/2023 || || 500.00 || 2500.00
13/01/2023 || 2000.00 || || 3000.00
10/01/2023 || 1000.00 || || 1000.00
```

## Approach
I decided to implement this in Python since I wanted an extra challenge and to get some exposure to another language. I used the unittest library to test drive this project.
Each class was designed sequentially:
**Transaction**
This creates a transaction which contains the date and monetary total of the transaction.

**Account**
This creates a blank account with an initial balance of 0 and an array which will be populated with logs of transaction, storing the transaction object and the current balance after that transaction is added.

**BankStatement**
This is initialised with an account object and will create a statement for the account up to that point.

## Running the code
With python3 installed, clone this repository and cd into the source code by running this in your terminal:

```
git clone https://github.com/lplclaremont/bank-tech-test
cd bank-tech-test
cd src
```

Open REPL and use the following commands:

'''
python3
from account import Account
from bank_statement import BankStatement
account = Account()
'''

Now you are able to make deposits and withdrawals as follows:

'''
account.deposit(1000)
account.deposit(500)
account.withdraw(250)
'''

And view your statement:

'''
statement = BankStatement(account)
print(statement.view())
'''