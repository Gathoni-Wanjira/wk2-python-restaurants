from Customer import Customer
from Restaurant import Restaurant
from Review import Review


# Customers objects

customer1 = Customer("Noonie", 'Gathoni')
customer2 = Customer("Gathoni", 'Wanjira')

#Testing Customer methods
customer1.set_given_name= "uhuru"
# print(customer1.given_name) 

customer2.set_family_name = "Kenyatta"
# print(customer2.family_name)

print (customer2.full_name())

# Resturant Objects

Restaurant1 = Restaurant("Artcaffe")


# Review Objects

review1 = Review( "Mwanny","Bigsquare" , 5)

# Testing review methods

# reviews = all(all_review)
# print(reviews)