time = input("Enter the time now. Whether day or night: ")
weather = ("daytime","nighttime")

if time.lower() in weather[0]:
    print("its day time ")
        
elif time.lower() == weather[1]:
    print("its night time")

else:
    print("i cant detect the weather")


