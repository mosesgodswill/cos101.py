

def area_of_circle():
    radius =float(input("Enter Radius"))
    area = 2 * 22/7 * radius
    print(area)

#area_of_circle()

def calculate_velocity():
    distance = float(input("Enter Distance"))
    time = int(input("Enter Time"))
    velocity = distance / time
    print(velocity)

    calculate_velocity()


def calculate_acceleration():
    initial_velocity = float(input("Enter the value for initial velocity: "))
    final_velocity = float(input("Enter the value for final velocity: "))
    time_elapsed = float(input("Enter the value for time: "))
    acceleration = (final_velocity-initial_velocity/time_elapsed)
    print("Acceleration is ",acceleration,"m/s")



#Calculate_the_length_of_the_hypotenuse_using_Pythagoras'theorem
def calculate_hypotenus():
    a = float(input("enter the length of side a "))
    b = float(input("enter the length of side b "))
    hypotenus = (a + b)
    print("Length of hypotenuse is: ",hypotenus ,"cm")



def calculate_rectangle_area():
    length = float(input("enter the value for length "))
    width = float(input("enter the value for width "))
    area = (length * width)
    print("The value of area is:",area, "cm" )


def calculate_exponentiation():
    a = float(input("enter the value for a "))
    b = float(input("enter the value for b "))
    result = (a ** b)
    print("result:",result)


def calculate_multiplication():
    a = float(input("enter the value for a "))
    b = float(input("enter the value for b "))
    result = (a * b)
    print("result:",result)



start = int(input("Type 1 to calculate acceleration\nType 2 to calculate the length of the hypothenus\nType 3 to calculate rectangle area"
                  "\nType 4 to calculate exponentiation\nType 5 to calculate multiplication"))

print(start)


if start == 1:
    calculate_acceleration()
elif start == 2:
    calculate_hypotenus()
elif start == 3:
    calculate_rectangle_area()
elif start == 4:
     calculate_exponentiation()
elif start == 5:
    calculate_multiplication()
else:
    print("Invalid entry")