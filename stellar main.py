"""
 __author__ = Mitchell Achor
           INTEGRATION PROJECT
            Stellar Bodies

 This program is designed to explore mathematical ratios comparing weight
 measurements on earth and other bodies in space.
"""


def menu():

    """Start of the code
    Brings up menu choices for the user
    1 will call main and 5 will quit program"""

    print("Enter the choice for what you would like to see")
    print("1. Start Program")
    print("5. Quit Program")
    # function_call = int(input())
    function_call = 1
    while True:
        try:
            function_call = int(input())
            break
        except ValueError:
            print("Error. Please enter either a '1' or a '5'.")
            menu()
    if function_call == 1:
        print("You have called function number", function_call)
        main()
    elif function_call == 5:
        print("Exiting...")
        quit()


def weight_conversion(user_weight_pounds, conversion_constant):
    """Converts users weight from pounds into kilograms
    parameters: user_weight_pounds, gravitational_force, and constant called
    conversion_constant
    return: users mass in kilograms"""

    user_weight_kilograms = user_weight_pounds * conversion_constant
    # user_weight_newtons_earth = user_weight_kilograms * gravitational_force
    return format(user_weight_kilograms, '.2f')


gravitational_force_earth_meters_per_second = 10
# r = input("Enter your weight in pounds: ")
t = .453492


def main():

    """Main program including print statements and mathematical calculation"""

    user_name = input("What is your name?")
    print("Greetings,", user_name + "!", end=" ")
    print("Welcome to my program!\nThis program is designed to educate the "
          "user on some basic differences between our world and other solar "
          "bodies.")

    print("Let's begin!")
    user_weight_pounds = 1
    while True:
        try:
            user_weight_pounds = int(input(
                "Please enter your current weight in pounds: "))
            break
        except ValueError:
            print("Error")

    print("To calculate your weight on other planets I am first going to")

    print("convert your weight from pounds to kilograms.")

    print("One moment please...")

    user_weight_kilograms = user_weight_pounds * .453492
    # # * multiplies the users weight in pounds by a constant to convert into
    # kilograms
    user_weight_kilograms_string = str(user_weight_pounds * .453492)
    # # str converts users mass in kilograms to a string
    # gravitational_force_earth_meters_per_second = 10
    earth_gravity_string = "10 meters per seconds squared"
    # # two individual variables for earths force of gravity; one for
    # calculations and one for prints statements
    user_weight_newtons_earth = \
        user_weight_kilograms * gravitational_force_earth_meters_per_second
    weight_conversion(
        user_weight_pounds, t)
    print("Got it!")

    print("According to my calculations, your weight is approximately "
          "", format(float(user_weight_kilograms_string), '.2f'),
          " kilograms!", sep="")

    print("Before we go any further I would like to explore what exactly the")

    print("concept of 'weight' truly implies.")

    print("Weight is simply force of gravity upon any object that has mass.")

    print("The standard unit of measurement for weight is the Newton and the")

    print("standard unit for mass is the kilogram.")

    print("So,your weight is simply your mass, measured in kilograms, ")

    print("multiplied by the force of gravity on your home planet.")

    print("For example, if your mass was only 1 kilogram then your weight on ")

    print("Earth would be approximately 9.8 Newtons.")

    print("Here on earth, the gravity is 9.8 meters per seconds squared.")

    print("For efficiency we will round up to 10 meters per seconds squared.")

    print("So, to calculate your weight on earth in Newtons, simply multiply")

    print(format(float(user_weight_kilograms_string), '.2f'))

    print("by", earth_gravity_string + " and...")

    print("Voila!")

    print("Your weight measured in Newtons is approximately...")

    print(format(user_weight_newtons_earth, '.2f'), "Newtons.")

    print("Let's use this data to understand weight on other planets.")

    print("Take Jupiter, for example.")

    jupiter_gravity_mps = 25

    jupiter_gravity_mps = int(jupiter_gravity_mps)

    user_weight_newtons_jupiter = user_weight_kilograms * jupiter_gravity_mps

    user_weight_pounds_jupiter = user_weight_newtons_jupiter // 4.448

    user_weight_pounds_jupiter = int(user_weight_pounds_jupiter)

    user_weight_pounds_jupiter_string = str(user_weight_pounds_jupiter)

    # 1 KG = 2.205 pounds
    # 1 KG = 9.807 Newtons

    print("The gravity on Jupiter is about 25 meters per seconds squared. ")

    print("More than double the Earth's gravity!")

    print("According to my calculations, your weight on Jupiter is")

    print(format(user_weight_newtons_jupiter, ".2f") + " Newtons!", sep='')

    print("Meaning, your body would weigh around")

    print(user_weight_pounds_jupiter_string + " pounds!")

    sun_gravity_mps = 274

    sun_gravity_mps = int(sun_gravity_mps)

    print("Next we will examine weight on the sun.")

    print("The force of gravity on the sun is 274 meters per seconds squared!")

    user_weight_newtons_sun = user_weight_kilograms * sun_gravity_mps

    user_weight_pounds_sun = user_weight_newtons_sun // 4.448
    # // divides the users weight in newtons under the gravity of the sun by a
    # constant and only shows the integer portion of the calculation
    user_weight_pounds_sun = int(user_weight_pounds_sun)

    print("If, theoretically, you could stand upon the surface of the sun")

    print("your weight would be approximately...")

    print(user_weight_pounds_sun, "pounds! WOW!")

    user_weight_pounds_difference = user_weight_pounds_sun - user_weight_pounds
    # - takes the difference of the users weight on earth and the sun
    print("Your trip to the sun would have gained you...")

    print(user_weight_pounds_difference, "pounds.")

    print("One last thing before you go...")

    print("Did you know that Jupiter has much shorter days than earth?")

    one_jupiter_day = 24 * 0.41
    jupiter_hours_remainder = 24 % one_jupiter_day

    print("Because Jupiter spins more than twice as fast as earth,")

    print("a single day on Jupiter would be only", one_jupiter_day, "hours.")

    print("So, you could spend 2 whole days and", jupiter_hours_remainder)

    print("hours on Jupiter before a whole Earth-day passes!")

    num = int(input("Please enter a whole number between 1 and 100: "))
    for x in range(num):
        for i in range(num):
            print(i + 1, end=" ")
        num -= 1
        print()
    while True:
        enjoy = input("Did " + "you " + "enjoy " + "my "
                      + "program? Enter yes or no: ")
        # + puts strings together exactly as they are
        if enjoy == "yes":

            print("Hooray! I am so happy you enjoyed yourself.")

            print("And I hope to see you again for my future projects!")

            print("Thank you! " * 10)
            # * 10 here prints my statement 10 times
            print("Goodbye", user_name + "!")

            print("Returning to menu...")

            menu()
        elif enjoy == "no":

            print("Sorry :(")

            print("Returning to menu...")

            menu()
        else:
            print("Invalid Input")


menu()
weight_conversion(int(input("Enter weight in pounds: ")), t)
# SITED SOURCES

# https://www.schoolsobservatory.org/discover/quick/weight
