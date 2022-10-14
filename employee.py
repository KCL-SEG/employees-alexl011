"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    commission = False
    contract = ''
    commission_type = ''
    salary = 0
    def __init__(self, name, commission, contract, commission_type):
        self.name = name
        self.commission = commission
        self.contract = contract
        self.commission_type = commission_type

    def get_pay(self):
        if(self.commission == True):
            if(self.contract == 'salary'):
                if(self.get_commision_type() == 'contract'):
                    salary = 3800
                    return salary
                elif(self.get_commision_type() == 'bonus'):
                    salary = 3500
                    return salary
            elif(self.contract == 'hourly'):
                if(self.get_commision_type() == 'contract'):
                    salary = 4410
                    return salary
                elif(self.get_commision_type() == 'bonus'):
                    salary = 4200
                    return salary
        else:
            if(self.contract == 'salary'):
                salary = 4000
                return salary
            elif(self.contract == 'hourly'):
                salary = 2500
                return salary
    def get_commision_type(self):
        return self.commission_type
    def __str__(self):
        if(self.commission == True):
            if(self.contract == 'salary'):
                if(self.get_commision_type() == 'contract'):
                    return self.name + ' works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800. \n'
                elif(self.get_commision_type() == 'bonus'):
                    return self.name + ' works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500. \n'
            elif(self.contract == 'hourly'):
                if(self.get_commision_type() == 'contract'):
                    return self.name + ' works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410. \n'
                elif(self.get_commision_type() == 'bonus'):
                    return self.name + ' works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200. \n'
        else:
            if(self.contract == 'salary'):
                return self.name + ' works on a monthly salary of 4000.  Their total pay is 4000. \n'
            elif(self.contract == 'hourly'):
                return self.name + ' works on a contract of 100 hours at 25/hour.  Their total pay is 2500. \n'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', False, 'salary', 'no commission')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 'hourly', 'no commission')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 'salary', 'contract')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', True, 'hourly', 'contract')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 'salary', 'bonus')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', True, 'hourly', 'bonus')
