list1= [10,20,30,40,50]
print(len(list1))
list2= list()
print(list2)
str1='aeiou'
# creating list
list3= list(str1)
print(list3)
# append:
list4= [10,20,30,40]
list4.append(50)
print(list4)
list5=[10,20,30,40]
list5.append([50,60])
print(list5) 
# extend: multiple val add ,faster than append
list6= [10,20,30]
list7= [40,50]
list6.extend(list7)
print(list6)
# insert:
list8=[10,20,30,40,50]
list8.insert(2,25)
print(list8)
# count:
list9= [10,20,30,10,40,10]
print(list9.count(10))
print(list9.count(90))  
list10= [10,20,30,20,40,10]
print(list10.index(20))
# print(list10.index(90))
list11 =[10,20,30,40,50,30]
list11.remove(30)
print(list11)
# list11.remove(90)
print(list11)
list12= [10,20,30,40,50,60]
list12.pop(3)
print(list12)
list12.pop()
print(list12)
list13= ['Tiger', 'Zebra', 'Lion', 'Dog', 'Cat']
list13.sort()
print(list13)
list14= [34,66,12,89,28,99]
list14.sort(reverse= True)
print(list14)
list15= [23,45,11,67,85,56]
list16= sorted(list15)
print(list15)
print(list16)
print(min(list15))
print(max(list15))
print(sum(list15))