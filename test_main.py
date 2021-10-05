import main
I = 0
INPUTS = []
OUTPUTS = []
def mock_input(_: str = None) -> None:
    global I
    
    while True:
        try:
            yield INPUTS[I]
            I += 1
        except IndexError:
            break
def mock_print(output: str) -> None:
    print(output)
    OUTPUTS.append(output)
def test_get_difficulty() -> None:
    global INPUTS, OUTPUTS
    print("test_get_difficulty")
    main.input = mock_input
    main.print = mock_print
    INPUTS = [1, 2, 3]
    print([_ for _ in mock_input()])
    
    main.input = input
    main.print = print
    main.main()
