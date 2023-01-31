class BankAccount:
    def __init__(self, account_number, owner, balance, pin):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.pin = pin
    
    def deposit(self, amount, pin):
        if pin != self.pin:
            raise ValueError("Incorrect PIN")
        self.balance += amount
    
    def withdraw(self, amount, pin):
        if pin != self.pin:
            raise ValueError("Incorrect PIN")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    
    def get_balance(self, pin):
        if pin != self.pin:
            raise ValueError("Incorrect PIN")
        return self.balance
    
    def __str__(self):
        return f"Account number: {self.account_number}\nOwner: {self.owner}\nBalance: {self.balance}"

account1 = BankAccount(12345, "Mr Z", 2300, 1219)

account1.deposit(700,1219)
# print(account1.get_balance(1219))

print(account1)








