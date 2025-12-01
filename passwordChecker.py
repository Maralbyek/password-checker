import re

def check_password_strength(password):
    score = 0
    feedback = []


    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 characters).")


    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[ ]", password):
        score += 1
    else:
        feadback.append("Space between the password not allowed.")


    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")


    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!, @, #, etc).")

    weak_list = ["password", "123456", "qwerty", "abc123", "111111"]
    if password.lower() in weak_list:
        feedback.append("This password is extremely weak and commonly used.")


    if score >= 10:
        strength = "Almost Impossible "
    elif score >= 8:
        strength = "Strong"
    elif score >= 4:
        strength = "Weak"
    else:
        strength = "Pease of cake"

    return strength, feedback


if __name__ == "__main__":
    print("=== Password Strength Checker ===")
    pwd = input("Enter a password to evaluate: ")

    strength, issues = check_password_strength(pwd)

    print("\nPassword Strength:", strength)
    if issues:
        print("\nSuggestions to improve:")
        for issue in issues:
            print("- " + issue)
    else:
        print("Your password looks great!")

