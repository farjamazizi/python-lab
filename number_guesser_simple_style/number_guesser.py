import random


def validate_input(user_guess):
        if not user_guess.isdigit():
            print("Invalid input. PLease try again.")
            return False
    
        user_guess = int(user_guess)
        if user_guess > 100 or user_guess < 1:
            print("Your guess is out of range. PLease try again. Your guess should be between 1 and 100.")
            # score -= 5
            return False
    
        return True


def main():
    rand_num = random.randint(1,100)
    print(rand_num)

    score = 100

    while True:
        user_guess = input("Guess a number between 1 and 100: ")

        if user_guess == "q":
            print("Thank you for playing. Goodbye!")
            break

        if not validate_input(user_guess):
            continue

        # elif not user_guess.isdigit():
        #         print("Invalid input. PLease try again.")
        #         continue
        
        # user_guess = int(user_guess)
        # if user_guess > 100 or user_guess < 1:
        #      print("Your guess is out of range. PLease try again. Your guess should be between 1 and 100.")
        #      score -= 5
        #      continue

        user_guess = int(user_guess)

        if rand_num == user_guess:
            print("You guessed the number correctly!")
            print(f"Your score is: {score}")
            Do_you_play = input("Do you want to play again? (y/n)")
            if Do_you_play == "y":
                rand_num = random.randint(1,100)
                print(rand_num)
                score = 100
                continue
            else:
                print("Thanks for play :)")
                break
        
        elif rand_num > user_guess:
            print("Your guess is too low. pLease try again.")
        else:
            print("your guess is too high. PLease try again")
    
        score -= 10
        # score = max(score, 0)


if __name__ == '__main__':
    main()
