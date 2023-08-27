class Customer:
    
    customers = []
     
    def __init__(self , first_name , last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.customers.append(self)
        
    @property
    def given_name(self):
        return self.first_name
    
    @given_name.setter
    def set_given_name(self, given_name):
        self.first_name = given_name
    
    @property
    def family_name(self):
        return self.last_name
    
    @family_name.setter
    def set_family_name(self, family_name):
        self.last_name = family_name
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @classmethod
    def all (cls):
        return cls.customers
    
    def add_review (self , restaurants, rating)
    