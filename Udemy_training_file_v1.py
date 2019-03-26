# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:40:25 2019

@author: Dell
"""

my_list = [4,3,2,1]

# append 
my_list.append(5)
print(my_list)

# pop
my_list.pop(4)
print(my_list)

# remove
my_list.remove(4)
print(my_list)

# insert
my_list.insert(1,250)
print(my_list)

# clear
my_list.clear()
print(my_list)

# index
my_list.index(1)

# count
my_list = [4,3,2,1,1,1,1]
my_list.count(1)

# sort 
print(my_list)
my_list.sort()




###### DICTIONARIES 

my_dict = {"school": "def of school"}

my_dict = {"school": "def of school", "coding": "def of coding", "python": "def of python"}
print(my_dict)

print(my_dict["python"])

# add def
my_dict["soccer"] = "def of soccer"
print(my_dict)

# print them in separate lines

for key, value in my_dict.items():
    print(key, "     ", value)
    
    
    
##### TOPLES

person = "Samy", 27, "brown"
print(person)

print(person[1])
print(person[0])

name,age, hair = person
print(name)
print(age)
print(hair)
print(person)


# loop it
for value in person:
    print(value)

# Nested tuples 
person = "Samy", ("brown", "black"), 27
print(person[1])

person = "Rudi", 31, "yellow"
print(person)



###### LIST COMPREHENSION

import random
print(random.randint(0,100))

our_list = []

for value in range(0,20):
    our_list.append(random.randint(0,100))
print(our_list)

# do it with list comprehension

new_list = []
new_list = [value for value in range(0,20)]
print(new_list)

new_list = []
new_list = [random.randint(0,100) for value in range(0,20)]
print(new_list)

# inner list 
task_list = []
print(task_list)

for row in range(0,25,5):
    inner_list = []
    print(inner_list)
    for column in range(row, row+5):
        inner_list.append(column)
        print(task_list)
    task_list.append(inner_list) 
    
for row in task_list: 
    print(row)
    
# list composition 
new_list = [[column for column in range(row, row+5)]for row in range(0,25,5)]

for row in new_list:
    print(row)
pass

# list composition vol 2
n1_list = [[column for column in range(row, row+10)]for row in range(0,45,1)]

for row in n1_list:
    print(row)
pass




###### IF ELSE FUNCTIONS

a = 20
print("a is 20" if a == 20 else "a is not 20")

b = True if a == 20 else False 
print(b)




###### ADDING EXCEL SHEETS

# necessary input 
from xlsxwriter import Workbook

# make workbook
workbook = Workbook("first_file.xlsx")

# add worksheet 
worksheet = workbook.add_worksheet()

# write functions
worksheet.write(0,0, "zero rows and zero columns")
worksheet.write(0,1, "zero rows and one column")

worksheet.write(1,0, "one row and zero columns")
worksheet.write(1,1, "one row and one column")

# close workbook 
workbook.close()


























