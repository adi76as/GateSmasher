# concatenation: add kore
list1= [1,3,5,7,9]
list2= [2,4,6,8]
list3=list1+list2
print(list3)
list4= ['a','b','c']
list5= [1,2,3]
list6= list4+list5
print(list6)
# repetition: elements of list7 repeated 5 times
list7= ['Hello']
print(list7*5)
# Membership: list er part naki check kora, (not in) use kora jabe
list8= ['varun', 'ravinder', 'amrit']
print('amrit' in list8)
print('nitin' in list8)
# slicing: list[start:end:indexjump](end=stop-1)
# index= -6      -5         -4      -3      -2      -1
list9= ['varun','ravinder','amrit','nitin','rahul','parjwal']
#          0        1         2       3       4        5     
print(list9[0:5])  
# items start through stop-1
print(list9[0:])
# items start through the rest of the array
print(list9[:5])
# items from the beginning through stop-1
print(list9[:])
# a copy of whole array
print(list9[-1])
# last item in the array
print(list9[-2:])
# last two items in the array
print(list9[:-2])
# everything except the last two items
print(list9[::-1])
# all items in the array,reversed
print(list9[1::-1])
# the first two items,reversed
print(list9[:-3:-1])
# the last two items,reversed
print(list9[-3::-1])
# everything except the last two items,reversed

