#Write a function that checks whether the function is odd or even
#Add input validation and handle negative numbers
def is_odd_or_even(number):
    if not isinstance(number, int):
        return "Invalid input: Please enter an integer."
    if number < 0:
        number = abs(number)
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

# Write unit tests for the function
def test_is_odd_or_even():
    assert is_odd_or_even(4) == "Even"
    assert is_odd_or_even(7) == "Odd"
    assert is_odd_or_even(-2) == "Even"
    assert is_odd_or_even(-9) == "Odd"
    assert is_odd_or_even(0) == "Even"
    assert is_odd_or_even(3.5) == "Invalid input: Please enter an integer."
    assert is_odd_or_even("test") == "Invalid input: Please enter an integer."
    print("All tests passed!")

# Run the tests
test_is_odd_or_even()
