from Review import Review


class Customer:
    
    customers = []
    
    
    #  Instance Attributes
    def __init__(self , first_name , last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.customers.append(self)
        self.all_reviews = []
        
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
    
    # Object Relationship
    
    def add_review (self , restaurants, rating):
            customer_review = (Review(self, restaurants=restaurants, rating=rating))
            self.all_reviews.append(customer_review)
            
    
    def resturants(self):
        return list ({review.restaurants for review in self.all_reviews})
    
    # Aggregate and Association Methods
    
    def num_reviews(self):
        return len([review for review in Review.all_review if review.customer.full_name == self.full_name])
       
    
    def find_by_name(cls, name):
        for Customer in cls.customers:
            if Customer.full_name == name:
                return Customer
    
    def find_all_by_given_name(cls,name):
        return [Customer.given_name for Customer in cls.customers if Customer.given_name == name]
      
    
    
        