# slicing in python
# index- R to L (0 theke start)
# index- L to R(-1 theke start)
# [start: Stop: Step] step na bolle by default 1
# stop exclude(add hobe na)
string1= "Gate Smashers"
substr1= string1[5:10]
substr2= string1[:10]
substr3= string1[5:]
substr4= string1[:]
substr5= string1[-8:-3]
substr6= string1[5::2]
substr7= string1[::-1]
substr8= string1[5:12].upper()
print(substr1)
print(substr2)
print(substr3)
print(substr4)
print(substr5)
print(substr6)
print(substr7)
print(substr8)