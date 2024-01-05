#traffic light simulation
color = input("what is the color of the traffic light")

valid_color = ["red","Yellow","Green"]


if color == "red":
        print("stop")
 
elif color == "yellow":
        print("Proceed with caution")

    
elif color == "Green":
        print("Go")
    
else:
        print("Invalid color input")
        print("Go now. Drive slowly!")


# Traffic Light Simulation
color = input("What is the color of the traffic light? ")

valid_colors = ["red", "yellow", "green"]

# Check if the entered color is valid
if color.lower() in valid_colors:
    print(f"Color: {color.lower()}")  # Print the entered color

    if color.lower() == "red":
        print("Stop")
    elif color.lower() == "yellow":
        print("Proceed with caution")
    elif color.lower() == "green":
        print("Go")
    else:
        print("Invalid color input")
        print("Go now. Drive slowly!")
else:
    print("Invalid color input. Please enter 'red', 'yellow', or 'green'.")
