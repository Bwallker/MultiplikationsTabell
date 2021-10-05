import random
from typing import Any
#Inbygger ett val av svårighetsgrad
class Difficulty:
    def __init__(self, min_value: int, max_value: int, increases_in_difficulty: bool = False) -> None:
        self.min_value = min_value
        self.max_value = max_value
        self.increases_in_difficulty = increases_in_difficulty
    def __str__(self) -> str:
        return f"{self.min_value} {self.max_value}"



def get_difficulty() -> Difficulty:
    EASY = Difficulty(1, 10)
    MEDIUM = Difficulty(1, 20)
    HARD = Difficulty(10, 100)
    EXPERT = Difficulty(1000, 100000)
    EXTREME = Difficulty(10000000, 10000000000, True)
    DIFFICULTIES = {
        "easy": EASY,
        "medium": MEDIUM,
        "hard": HARD,
        "expert": EXPERT,
        "extreme": EXTREME
    }
    print("type easy for easy difficulty")
    print("type medium for medium difficulty")
    print("type hard for hard difficulty")
    print("type expert for expert difficulty")
    print("type custom for custom difficulty")
    print()
    while True:
        difficulty_as_str = input("What difficulty do you want? ")
        print()
        difficulty_as_str = difficulty_as_str.strip().lower()
        if difficulty_as_str in DIFFICULTIES:
            return DIFFICULTIES[difficulty_as_str]
        elif difficulty_as_str == 'custom':
            while True:
                try:
                    min_value = int(input('What minimum value do you want? '))
                    print()
                except ValueError:
                    print("Your min value must be an integer")
                    continue
                max_value: int
                while True:
                    try:
                        max_value = int(input('What maximum value do you want? '))
                        print()
                        break
                    except ValueError:
                        print("Your max value must be an integer")
                        continue
                if max_value <= min_value:
                    print("max value must be bigger than min value")
                    print()
                    continue
                increases_in_difficulty: bool                
                while True:
                    increases_in_difficulty_as_str = input("Should the difficulty increase over time? (Y/N)")
                    if increases_in_difficulty_as_str.strip().lower() in ("y", "true", "t"):
                        increases_in_difficulty = True
                        print()
                        break
                    elif increases_in_difficulty_as_str.strip().lower() in ("n", "false", "f"):
                        increases_in_difficulty = False
                        print()
                        break
                    print("You did not input a valid value")
                    print()

                return Difficulty(min_value, max_value, increases_in_difficulty)
        else:
            print("Your difficulty was not valid. Try again.")

#Inbygger mängden av omgångar                        
def get_rounds() -> int:
    print("How many rounds do you want to play?")
    while True:
        try:
            rounds = int(input("> "))
            if rounds < 1: raise ValueError
            return rounds
        except ValueError:
            print("rounds to play must be an int")
def get_random_number(min_value: int, max_value: int) -> int:
    return      
        
def main() -> None:
    print("#######Multiplikationstabell#######")
    print("The computer will generate two random numbers in an interval you choose, and your job is to multiply them correctly")
    print("Best score wins!")
    print()
    rounds = get_rounds()
    difficulty = get_difficulty()
    correct_answers = 0
    for i in range(rounds):
        number_1 = random.randint(difficulty.min_value, difficulty.max_value)
        number_2 = random.randint(difficulty.min_value, difficulty.max_value)
        print()
        print(f"What is {number_1} * {number_2}?")
        answer = number_1*number_2
        user_answer: int
        while True:
            try:
                user_answer = int(input("Answer: "))
                break
            except ValueError:
                print("Your answer must be an int")
        if difficulty.increases_in_difficulty:
            difficulty.min_value += 1000
            difficulty.max_value += 1000
        if answer != user_answer:
            print("Wrong answer!")
            continue
        print("Correct answer!")
        correct_answers += 1
    
    print(f"You got {correct_answers} out of {rounds} questions right!")
    as_percentage = (correct_answers/rounds)*100
    #Remove decimals
    as_percentage = round(as_percentage, 0)
    as_percentage = int(as_percentage)
    print(f"You got {as_percentage}% right!")
if __name__ == '__main__':        
    main()
