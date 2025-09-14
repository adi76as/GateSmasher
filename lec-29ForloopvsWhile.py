# While loop:
# x=0
# while not(1<=x<=100):
#     x=int(input('Please enter a number between 1 and 100: '))
# print("valid no",x)

# for loop:
for i in range(4):
    x=int(input("please enter a number: "))
    if 1<=x<=100:
        print("valid no", x)
        break
    else:
        print("invalid number.Try again")
