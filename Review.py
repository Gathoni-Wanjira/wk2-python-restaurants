class Review:
    
    all_review = []
    
    def __init__(self, a_customer, a_resturant , a_rating):
        self.a_customer = a_customer
        self.a_resturant = a_resturant
        self.a_rating = a_rating
        self.all_review.append(self)
      
    @property  
    def rating(self):
        return self.a_rating 
    
    @classmethod
    def all(cls):
        return cls.all_review
        
        # Object Relationship
    