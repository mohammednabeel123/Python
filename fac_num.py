#Create a recursive function to calculate the factorial of a given number.
def fac_num(number):
    if number == 0 or number == 1 :
        return 1
    else:
        return number*fac_num(number -1)

number = int(input("Enter your number fac: "))
if number < 0:
    print("cant be found ")
else:
    result = fac_num(number)
    print(result)
    