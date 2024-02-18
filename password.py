import string


def check_pwd(password):
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char.isspace():
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "Very Bad Password !!! Change ASAP"
    elif strength == 2:
        remarks = "Not a good password!!! Change ASAP"
    elif strength == 3:
        remarks = "It is a weak password, consider changing"
    elif strength == 4:
        remarks = "It is a hard password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"

    print('Your password has:')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Password strength: {strength}")
    print(f"Hint: {remarks}")
    
    return remarks


def main():
    print("Welcome to the Password Strength Checker!")
    while True:
        password = input("Please enter your password: ")
        if len(password) < 8:
            print("Password must be at least 8 characters long. Please try again.")
        else:
            break

    remarks = check_pwd(password)
    print("Your password strength is:", remarks)


if __name__ == "__main__":
    main()