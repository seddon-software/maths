import random, time, os


while True:
    time.sleep(5)
    os.system("clear")    

    number = random.randint(2, 100)

    print(f"\nWhat is a factor of {number}?")
    print("Enter a factor, or P if the number is prime.")

    answer = input("> ").strip().upper()

    # Find proper factors (excluding 1 and the number itself)
    factors = [i for i in range(2, number) if number % i == 0]

    if answer == "P":
        if not factors:
            print("Correct")
        else:
            print("Fail")
    else:
        try:
            guess = int(answer)

            if guess in factors:
                print("Correct")
            else:
                print("Fail")

        except ValueError:
            print("Fail")
