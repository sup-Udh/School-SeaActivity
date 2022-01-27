# To check whether a number is divisible by 5 and 11 or not.

userinput = int(input("enter the number:"))

if userinput % 5 == 0 and userinput % 11 == 0:
    print("divisible by 5 and 11")
else:
    print("not divisible by 5 and 11")