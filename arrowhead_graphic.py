"""
ArrowHead Graphic

This program allows a user to create a customizable arrowhead graphic.

The program reads an input string from the user to determine character to composite graphic,
and an input integer from the user to determine graphic size.

GitHub: ShiriCodes
Date: 2025-08-27
"""
def til_valid(validator, prompt: str, error_message: str):
    """Creates a loop for validation"""
    while True:
        try:
            return validator(str(input(prompt)))
        except ValueError as e:
            print(error_message, e)

def char_input_validate(my_char):
    """Validates user character input for main arrow function"""
    if my_char.strip() == "":
        raise ValueError("Entered character must not be empty.")
    return my_char

def char_input():
    """Records user character input for main arrow function"""
    validator = char_input_validate
    prompt = "\nPlease enter desired character: "
    error_message = "\nTry again. Please enter something next time."
    return til_valid(validator,prompt,error_message)

def len_input_validate(max_length):
    """Validates user maximum length input for main arrow function"""
    if max_length.isdigit():
        max_length = int(max_length)
        if max_length > 0:
            return max_length
    raise ValueError("Maximum length must be a positive integer.")

def len_input():
    """Records user maximum length input for main arrow function"""
    validator = len_input_validate
    prompt = "\nPlease enter desired maximum length: "
    error_message = "\nTry again. Please enter a positive integer next time."
    return til_valid(validator,prompt,error_message)

def cont_input_validate(cont: str):
    """Validates user continue input for main arrow function"""
    if cont == "":
        return 1
    elif cont.isdigit():
        cont = int(cont)
        if cont in (0, 1):
            return cont
    raise ValueError("Continue input must be 1 or 0.")

def cont_input():
    """Records user continue input for main arrow function"""
    validator = cont_input_validate
    prompt = ("\nHope you've enjoyed your custom arrowhead. "
              "\nPlease enter 1 if you would like to create another arrowhead,"
              "\nand 0 if you would like to leave: ")
    error_message = "\nTry again. Please enter 1 to continue or 0 to quit."
    return til_valid(validator,prompt,error_message)

def arrow(my_char: str, max_length: int):
    """Returns an arrowhead graphic of my_char, arrowheads longest part of graphic is max_length long."""
    print("\n")
    for i in range(1, max_length):
        print(i * my_char)
    for i in range(max_length, 0, -1):
        print(i * my_char)
    print("\n")


def main():
    while True:
        arrow(char_input(), len_input())
        if cont_input() == 0:
            print("\nThanks for playing! Goodbye.")
            break

if __name__ == '__main__':
    main()