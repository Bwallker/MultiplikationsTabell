import random
import dataclasses


@dataclasses.dataclass
class Difficulty:
    min_value: int
    max_value: int
    increases_in_difficulty: bool = False


def get_difficulty() -> Difficulty:
    # Constants here since globals are not allowed
    EASY = Difficulty(1, 10)
    MEDIUM = Difficulty(1, 20)
    HARD = Difficulty(10, 100)
    EXPERT = Difficulty(100, 500)
    EXTREME = Difficulty(1000, 5000, True)
    DIFFICULTIES = {
        "easy": EASY,
        "medium": MEDIUM,
        "hard": HARD,
        "expert": EXPERT,
        "extreme": EXTREME
    }
    for value in DIFFICULTIES:
        print(f"type {value} for {value} difficulty")
    # Custom isn't in difficulties since it doesn't have predefined values
    print("type custom for custom difficulty")
    print()

    while True:
        print("What difficulty do you want?")
        difficulty_as_str = input("> ")
        difficulty_as_str = difficulty_as_str.strip().lower()
        print()
        if difficulty_as_str in DIFFICULTIES:
            return DIFFICULTIES[difficulty_as_str]
        elif difficulty_as_str == 'custom':
            return get_custom_difficulty()
        else:
            print("Your difficulty was not valid. Try again.")
            print()


def get_custom_difficulty() -> Difficulty:
    while True:
        min_value = get_min_value()
        max_value = get_max_value()
        if max_value <= min_value:
            print("Biggest number must be bigger than smaller number")
            print()
            continue
        increases_in_difficulty = should_increase_in_difficulty()

        return Difficulty(min_value, max_value, increases_in_difficulty)


def get_min_value() -> int:
    while True:
        print('What should the smallest number the computer might guess be?')
        try:
            min_value = int(input('> '))
            print()
            # Negative values are allowed
            return min_value
        except ValueError:
            print("Your smallest number must be an integer. Try again")
            print()


def get_max_value() -> int:
    while True:
        print('What should the biggest number the computer might guess be?')
        try:
            max_value = int(input('> '))
            print()
            # Negative values are allowed
            return max_value
        except ValueError:
            print("Your biggest number must be an integer. Try again")
            print()


def should_increase_in_difficulty() -> bool:
    while True:
        print("Should the difficulty increase over time? (Y/N)")
        increases_in_difficulty_as_str = input("> ")
        increases_in_difficulty_as_str = increases_in_difficulty_as_str.strip().lower()
        if increases_in_difficulty_as_str in ("y", "yes"):
            print()
            return True
        elif increases_in_difficulty_as_str in ("n", "no"):
            print()
            return False
        print("You did not input a valid value. Try again")
        print()


def get_rounds() -> int:
    while True:
        print("How many rounds do you want to play?")
        try:
            rounds = int(input("> "))
            if rounds < 1:
                raise ValueError
            print()
            return rounds
        except ValueError:
            print("Rounds to play must be a positive integer. Try again")
            print()


def main() -> None:
    print("#######Multiplikationstabell#######")
    print("The computer will generate two random numbers in an interval you choose every round, and your job is to multiply them correctly")
    print("You are graded based on how many rounds you get right")
    print()
    rounds = get_rounds()
    difficulty = get_difficulty()
    correct_answers = 0
    print("Starting game!")
    print()
    for _ in range(rounds):
        number_1 = random.randint(difficulty.min_value, difficulty.max_value)
        number_2 = random.randint(difficulty.min_value, difficulty.max_value)
        print()
        print(f"What is {number_1} * {number_2}?")
        answer = number_1*number_2
        user_answer = get_user_answer()

        if difficulty.increases_in_difficulty:
            # Arbitrarily chosen increase factor. Future feature idea might be to allow the user to change it
            difficulty.min_value = int(difficulty.min_value*1.2)
            difficulty.max_value = int(difficulty.max_value*1.2)
        print(difficulty)
        if answer != user_answer:
            print("Wrong answer!")
            print(f"Correct answer was: {answer}")
            print()
            continue
        print("Correct answer!")
        print()
        correct_answers += 1
    print("Game finished!")
    print()
    print(f"You got {correct_answers} out of {rounds} questions right!")
    as_percentage = (correct_answers/rounds)*100
    # Remove decimals
    # round is returning a float even though it claims to return an int?
    as_percentage = int(round(as_percentage, 0))
    print(f"You got {as_percentage}% right!")


def get_user_answer() -> int:
    while True:
        try:
            return int(input("Answer: "))
        except ValueError:
            print("Your answer must be an integer")
            print()


if __name__ == '__main__':
    main()
