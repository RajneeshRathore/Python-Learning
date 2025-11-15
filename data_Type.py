# List is an built in data type in python and it is an data structure in python

my_list=[1,2,3]
print(type(my_list))

# #Integer -> int is also an data type in python
age=10
print(type(age))

# #String -> str is also an data type in python
user="rohit"
print(type(user))

# #Boolean -> bool is also an data type in python
visible=True
print(type(visible))

# #Float -> float is also an data type in python
avg=3.14
print(type(avg))

# #Float -> float is also an data type in python

salary=10000.3423445725793257239759235
print(type(salary))

# #Dictionary -> dict is an build in datatype and also an data structure
my_dict={
    "name":"Raj",
    "roll":49,
     "course":"B-Tech"
    }
print(type(my_dict))

#Tuple -> tuple is an build in data type and also an data structure
my_tuple=(1,2,3,4)
print(type(my_tuple))
# my_tuple[1]="ram" # tuple doesnot support item assignment because it is immutable
# print(my_tuple[1])


#Set -> set is an build in data type and also an data structure
my_set={1,1,2,3,4}
print(my_set)  # it will print {1,2,3,4} because set do not allow duplicate values
print(type(my_set))

#Creating list using list() function
my_list=list(range(101))
print(my_list)

list=[1,2,list(range(3,11))]
print(list)

#Creating set using set() function
my_set=set(range(1,11))
print(my_set)

#Creating tuple using tuple() function
my_tuple=tuple(range(1,11))
print(my_tuple)
print(type(my_tuple))

