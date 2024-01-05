#leap year calculator
print("welcome to the leap year calculator")

leap_year = int(input("Enter a year\n"))

if leap_year % 4 == 0:
    if leap_year % 100 ==0:
        print("its not a leap year")
        if leap_year % 400 ==0:
            
            print("its is a leap year")
        else:
            print("its not a leap year")
    else:
        print("its a leap year")
else:
    print("its not a leap year")
    
        