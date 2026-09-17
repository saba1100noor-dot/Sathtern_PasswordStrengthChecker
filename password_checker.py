import re

def check_password(password):
    common_passwords = [
        "123456",
        "password",
        "12345678",
        "qwerty",
        "admin",
        "welcome"
    ]

    if password.lower() in common_passwords:
        return "Very Weak", [
            "This is a commonly used password. Choose a more unique password."
        ]

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


print("=== Sathtern Password Strength Checker ===")

password = input("Enter your password: ")

strength, suggestions = check_password(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("Your password meets all basic security requirements!")