import string

while True:
    # Get user input for the password
    password = input("Enter thy password (or type 'exit' 2 quit): ")

    # Check if the user wants to exit the program
    if password.lower() == 'exit':
        break

    # Your password strength analysis code here
    u_c = any([1 if c in string.ascii_uppercase else 0 for c in password])
    l_c = any([1 if c in string.ascii_lowercase else 0 for c in password])
    spec = any([1 if c in string.punctuation else 0 for c in password])
    digs = any([1 if c in string.digits else 0 for c in password])

    characters = [u_c, l_c, spec, digs]

    length = len(password)

    score = 0

    with open('500-worst-passwords.txt', 'r') as f:
        common = f.read().splitlines()

    if password in common:
        print("Password is too common.")

    # LENGTH PARAMETER
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 16:
        score += 1
    if length > 20:
        score += 1

    # CHARACTER DIVERSITY
    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1

    # FINAL SCORE PARAMETER
    if score < 4:
        print("Password strength: Naaaahhhhh")
    elif score == 4:
        print("Password strength: Ehhhhhh")
    elif 4 < score < 6:
        print("Password strength: Hmmmmmmm")
    else:
        print("Password strength: Hell yeah")

# The program will exit when the user types 'exit'
print("Program terminated. Also if that was your password then uhhhh oops")
