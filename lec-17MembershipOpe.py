list1= [1,2,3,4,5]
print(1 in list1)
print(10  in list1)
reg_user= ["varun", "ravi", "amrit", "nitin"]
name= input("Enter your name: ")
if name in reg_user:
    print("Access granted. Welcom bro")
else:
    print("Access denied. You are not registered.")
