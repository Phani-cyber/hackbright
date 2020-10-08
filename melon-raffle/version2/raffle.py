"""Randomly pick customer and print customer info"""
import customers
import random

file_path = 'customers.txt'

customer_list = customers.get_customers_from_file(file_path)
#print(customer_list)


random_customer = int(random.random() * len(customer_list))
#print(random_customer)
print(customer_list[random_customer].display())



# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries
