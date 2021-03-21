#Mitchell Achor
#              INTEGRATION PROJECT

#This program is designed to explore mathmatical ratios comparing measuments on earth and other planets.

def menu():
    print("Enter the choice for what you would like to see")
    print("1-4. Start Program")
    print("5. Quit Program")
    function_call = int(input())
    if 4 >= function_call >= 1:
        print("You have called function number", function_call)
        main()
    elif function_call == 5:
        quit()
    else:
        print("Invalid selection. Try again.")
        menu()

def weight_conversion(user_weight_pounds, gravitational_force, conversion_constant):
    user_weight_kilograms = user_weight_pounds * conversion_constant
    user_weight_newtons_earth = user_weight_kilograms * gravitational_force
    return format(user_weight_kilograms, '.2f')

gravitational_force_earth_meters_per_second = 10
r = int(input("Enter your weight in pounds: "))
t = .453492



def main():
    user_name = input("What is your name?")
    print("Greetings, ", user_name + "!", end = " ")
    print("Welcome to my program!\nWhile you are here you can learn about earth and the other planets in our solar system!")

    print("Let's begin!")

    user_weight_pounds = int(input("Please enter your current weight in pounds: "))

    print("To most efficiently calculate your weight on other planets I am going to convert your weight from pounds to kilograms.")

    print("One moment please...")

    user_weight_kilograms = user_weight_pounds * .453492
    # # * multiplies the users weight in pounds by a constant to covnvert into kilograms
    user_weight_kilograms_string = str(user_weight_pounds * .453492)
    # # str converts users mass in kilograms to a string
    # gravitational_force_earth_meters_per_second = 10
    earth_gravity_string = "10 m/s**2"
    # # two individual variables for earths force of gravity; one for calculations and one for prints statements
    user_weight_newtons_earth = user_weight_kilograms * gravitational_force_earth_meters_per_second
    weight_conversion(r, gravitational_force_earth_meters_per_second, t)
    print("Got it!")

    print("According to my calculations, your weight is approximately ", format(float(user_weight_kilograms_string), '.2f'), " kilograms!", sep="")

    print("Before we go any further I would like to explore what exactly the concept of 'weight' truly implies.")

    print("Weight is simply force of gravity upon any object that has mass and we measure weight in Newtons.")

    print("So, your weight, is just your mass, measured in kilograms, multiplied by the force of gravity on your home planet.")

    print("Here on planet earth, the force of gravity averages at about", earth_gravity_string)

    print("So, to calculate your weight on earth in Newtons, simply multiply", format(float(user_weight_kilograms_string), '.2f') + " by", earth_gravity_string + " and...")

    print("Voila!")

    print("Your weight measured in Newtons is approximately", format(user_weight_newtons_earth, '.2f'))

    print("But what about on other planets? Jupiter, for example.")

    jupiters_gravity_mps = 25

    jupiters_gravity_mps = int(jupiters_gravity_mps)

    user_weight_newtons_jupiter = user_weight_kilograms * jupiters_gravity_mps

    user_weight_pounds_jupiter = user_weight_newtons_jupiter // 4.448

    user_weight_pounds_jupiter = int(user_weight_pounds_jupiter)

    # 1 KG = 2.205 pounds
    # 1 KG = 9.807 Newtons

    print("According to my calculations, your weight on Jupiter would be approximately ", user_weight_pounds_jupiter, format(user_weight_pounds_jupiter, "1d") + " pounds!", sep='')

    sun_gravity_mps = 274

    sun_gravity_mps = int(sun_gravity_mps)

    print("While jupiter has some extreme gravity there is still one more object in the solar system with even greater gravitational force.")

    print("That's right! The sun! The force of gravity on the sun is 274m/s**2!")

    user_weight_newtons_sun = user_weight_kilograms * sun_gravity_mps

    user_weight_pounds_sun = user_weight_newtons_sun // 4.448
    # // divides the users weight in newtons under the gravity of the sun by a constant and only shows the integer portion of the calculation
    user_weight_pounds_sun = int(user_weight_pounds_sun)

    print("If, thoeretically, you could stand upon the surface of the sun your weight would be approximately", user_weight_pounds_sun, "pounds! WOW!")

    user_weight_pounds_difference = user_weight_pounds_sun - user_weight_pounds
    # - takes the difference of the users weight on earth and the sun
    print("Your trip to the sun would have gained you", user_weight_pounds_difference, "pounds.")

    print("One last thing before you go...")

    print("Did you know that Jupiter has much shorter days than earth?")

    one_jupiter_day = 24 * 0.41
    jupiter_hours_remainder = 24 % one_jupiter_day

    print("Because Jupiter spins more than twice as fast as earth, a standard day on Jupiter would be only", one_jupiter_day, "hours.")

    print("So, you could spend 2 whole days and", jupiter_hours_remainder, "hours on Jupiter before a whole Earth-day passes. Very interesting!")

    num = int(input("Now, enter a whole number between 1 and 100 for a surprise: "))
    for x in range(num):
        for x in range(num):
            print(x + 1, end=" ")
        num -= 1
        print()
    while True == True:
        enjoy = input("Did " + "you " + "enjoy " + "my " + "program? Enter yes or no: ")
        # + puts strings together exactly as they are
        if enjoy == "yes":

            print("Yay! I am so happy you enjoyed yourself.")

            print("And I hope to see you again for my future developments!")

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

weight_conversion(r, gravitational_force_earth_meters_per_second, t)
menu()
# SITED SOURCES

# https://www.schoolsobservatory.org/discover/quick/weight
