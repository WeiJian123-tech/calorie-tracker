if __name__ == "__main__":

    calories = 0

    while True:
        print("Press q to quit the program.")
        print("Press any other key to continue.")

        option = input("Keypress: ")

        if option == "q":
            break
        
        option = input("Enter the number of calories from a food item: ")

        calories += int(option)

        print(str(calories) + " calories added. \n")

    
    print("Number of total calories: " + str(calories))