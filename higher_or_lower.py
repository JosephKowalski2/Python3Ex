from random import randrange




def compare_user_number_and_random_number():
    number = int(input("Please enter a number 1 to 10 \n"))
    random_number = randrange(10)
    if number > random_number:
        print("Your guess was too high")
    elif number < random_number:
        print("Your guess was too low")
    else:
        print("You guessed right!")
    print(f'You guessed {number}')
    print(f'The number was {random_number}')

compare_user_number_and_random_number()

