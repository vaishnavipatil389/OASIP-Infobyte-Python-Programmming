import random
import string

def generate_password(length):
   
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password_complexity(password):
    complexity = {
        'length': len(password),
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digits': any(c.isdigit() for c in password),
        'special_characters': any(c in string.punctuation for c in password)
    }
    return complexity

def main():
    print("Welcome to the Password Generator!\n")

    while True:
        try:
            length = int(input("Enter the length of the password you want to generate: "))

            if length <= 0:
                print("\nPlease enter a positive integer for password length.")
            else:
                password = generate_password(length)
                print(f"\nGenerated Password: {password}")

                complexity = password_complexity(password)
                print("\nPassword Complexity:")
                print(f"- Length: {complexity['length']}")
                print(f"- Uppercase: {'Yes' if complexity['uppercase'] else 'No'}")
                print(f"- Lowercase: {'Yes' if complexity['lowercase'] else 'No'}")
                print(f"- Digits: {'Yes' if complexity['digits'] else 'No'}")
                print(f"- Special Characters: {'Yes' if complexity['special_characters'] else 'No'}")
                break
        except ValueError:
            print("\nInvalid input! Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
