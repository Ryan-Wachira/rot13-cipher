# Import the pyperclip module to copy text to the clipboard (optional).
try:
    import pyperclip
except ImportError:
    pass  # If pyperclip is not installed, continue without clipboard functionality.

# Define constants for uppercase and lowercase letters.
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

# Main program loop.
while True:
    # Ask the user to input a message to encrypt or decrypt.
    print('Enter a message to encrypt/decrypt (or QUIT):')
    message = input('> ')

    # If the user types "QUIT", break out of the loop to end the program.
    if message.upper() == 'QUIT':
        break

    # Initialize an empty string to store the translated message.
    translated = ''

    # Loops through each character in the input message.
    for character in message:
        # If the character is uppercase, apply ROT13 to it.
        if character.isupper():
            # Find the new position after shifting by 13 and wrap around if necessary.
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        # If the character is lowercase, apply ROT13 to it.
        elif character.islower():
            # Find the new position after shifting by 13 and wrap around if necessary.
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
        # If it's not a letter, add the character unchanged.
        else:
            translated += character

    # Displays the translated message to the user.
    print('The translated message is:')
    print(translated)
    print()

    # Trys to copy the translated message to the clipboard.
    try:
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except:
        pass  # If pyperclip is not installed, skip this step.
