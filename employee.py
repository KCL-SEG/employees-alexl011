"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, hours = 0, commission = 0, num_of_contracts = 0):
        self.name = name
        self.pay = pay
        self.hours = hours
        self.commission = commission
        self.num_of_contracts = num_of_contracts

    def get_pay(self):
        pay = self.pay
        if self.hours > 0:
            pay *= self.hours
        if self.commission > 0:
            commission = self.commission
            if self.num_of_contracts > 0:
                commission *= self.num_of_contracts
            pay += commission
        return pay

    def __str__(self):
        fin_str = f"{self.name}"
        if self.hours > 0:
            fin_str = fin_str + f" works on a contract of {self.hours} hours at {self.pay}/hour"
        else:
            fin_str = fin_str + f" works on a monthly salary of {self.pay}"
        if self.commission > 0:
            if self.num_of_contracts > 0:
                fin_str = fin_str + f" and receives a commission for {self.num_of_contracts} contract(s) at {self.commission}/contract"
            else:
                fin_str = fin_str + f" and receives a bonus commission of {self.commission}"

        fin_str = fin_str + f". Their total pay is {self.get_pay()}."
        return fin_str

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', pay = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', pay = 25, hours = 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', pay = 3000, commission = 200, num_of_contracts = 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', pay = 25, hours = 150, commission = 220, num_of_contracts = 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', pay = 2000, commission = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel, pay = 30, hours = 120, commission = 600)
