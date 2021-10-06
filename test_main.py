import main
import typing
I = 0
INPUTS = []
OUTPUTS = []
RANDOM_NUMBERS = []
SENTINAL = typing.TypeVar('SENTINAL')
def mock_input(_: str = None) -> None:
    return INPUTS.pop(0)
def mock_print(output: str = SENTINAL) -> None:
    if output == SENTINAL:
        print()
    else:
        print(output)
    OUTPUTS.append(output)
    
def mock_randint(min_value: int, max_value: int):
    return RANDOM_NUMBERS.pop(0)
def test_get_difficulty() -> None:
    global INPUTS, OUTPUTS, RANDOM_NUMBERS
    print("test_get_difficulty")
    main.input = mock_input
    main.print = mock_print
    main.random.randint = mock_randint
    INPUTS = ["3", "easy", "45", "24", "15"]
    RANDOM_NUMBERS = [5, 9, 3, 8, 5, 9]
    main.main()
    main.input = input
    main.print = print
    assert OUTPUTS[-2] == "You got 2 out of 3 questions right!"
    assert OUTPUTS[-1] == "You got 67% right!"
    
