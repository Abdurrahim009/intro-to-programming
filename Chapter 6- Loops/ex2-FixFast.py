while True:

    age = int(input("Enter your age (or type 'quit' to stop): "))
    
    if age < 3:
        print("Your ticket is free!")

    elif 3 <= age <= 12:
        print("Your ticket costs $10.")

    else:
        print("Your ticket costs $15.")
