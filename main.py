# movie showings
movies = {
    "Frozen": {
        "age": 3,
        "tickets": 94,
    },
    "The Batman": {
        "age": 17,
        "tickets": 45,
    },
    "The Godfather": {
        "age": 21,
        "tickets": 100,
    },
    "Barbie": {
        "age": 16,
        "tickets": 49,
    },
    "Twilight": {
        "age": 45,
        "tickets": 4,
    },
    "Rocky": {
        "age": 18,
        "tickets": 40,
    },
}

while True:
    choice = input("Good evening! Please make your movie selection: ").strip().title()
    # verify movie is showing
    if choice in movies:
        # check user's age
        age = int(input("A fine selection! Please enter your age to verify if you meet the age requirement: ").strip())

        if age >= movies[choice]["age"]:
            tickets = int(input("Thank you! How many tickets would you like?: ").strip())
            # check if enough seats
            if tickets <= movies[choice]["tickets"]:
                print("Sure thing! Here are your tickets. Enjoy your movie!")
                break
            else:
                print("I'm sorry, there aren't enough tickets to accommodate your request.")
        else:
            print("I'm sorry, you aren't old enough to watch this movie. Please select another movie to watch!")
    else:
        print("I'm sorry! We don't have that movie.")
