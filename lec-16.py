# data type r data jodi same hoi tahole same memory location thake (address same)
x=10
y=10
print(x is y)
z=x
print(z is x)
# x,y,z er same memory location
print(id(x))
print(id(y))
print(id(z)) 
str1="Hii"
str2="Hii"
print(str1 is str2)
# identity operator works only in small int
# List,dict egulo te diff memory location hoi same val dileo
list1= [10,20,30]
list2= [10,20,30]
print(list1 is list2)
print(id(list1))
print(id(list2))
num1= None
num2= None
print(num1 is num2)