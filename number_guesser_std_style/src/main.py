from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_random_number
from src.game_logic.hint_generator import provide_hint
from src.game_logic.scorer import Scorer


def main():
    target_number = generate_random_number(1, 100)
    score = Scorer()

    while True:
        user_guess = get_valid_input(1, 100)
        if user_guess == target_number:
            print(f"Congratulations! You've guessed the number {target_number} correctly!")
            print(f"Your final score is {score.get_score()}")
            break
        else:
            hint = provide_hint(user_guess, target_number)
            print(hint)
            score.update_score(penalty=10)
            print(f"Your current score is:      {score.get_score()}")
            if score.get_score() < 0:
                print("Game Over! You've run out of points.")
                break


if __name__ == "__main__":
    main()
    