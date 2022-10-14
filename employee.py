"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    commission = False
    contract = ''
    commission_type = ''
    def __init__(self, name, commission, contract):
        self.name = name
        self.commission = commission
        self.contract = contract

    def emp_commision(self, type):
        self.type = commission_type
    def get_pay(self):
        if(self.commission == True):
            if(self.contract == 'salary'):
                if(self.commision_type == 'contract'):
                    print(__str__(self) + 'works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800. \n' )
                elif(self.commision_type == 'bonus'):
                    print(__str__(self) + 'works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500. \n')
            elif(self.contract == 'hourly'):
                if(self.commision_type == 'contract'):
                    print(__str__(self) + 'works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410. \n')
                elif(self.commision_type == 'bonus'):
                    print(__str__(self) + 'works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200. \n')
        else:
            if(self.contract == 'salary'):
                print(__str__(self) + 'works on a monthly salary of 4000.  Their total pay is 4000. \n')
            elif(self.contract == 'hourly'):
                print(__str__(self) + 'works on a contract of 100 hours at 25/hour.  Their total pay is 2500. \n')
    def get_commision_type(self):
        return self.commission_type
    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', False, 'salary')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 'hourly')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 'salary')
renee.emp_commision('contract')
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', True, 'hourly')
jan.emp_commision('contract')
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 'salary')
robbie.emp_commision('bonus')
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', True, 'hourly')
robbie.emp_commision('bonus')
