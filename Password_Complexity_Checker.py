import re

def check_password_complexity(password):

    score = 0
    feedback = []

     # Criteria 1: Length
    if len(password) < 10:
        feedback.append("Password should be at least 10 characters long.")
    else:
        score += 1


    # Criteria 2: Uppercase letters
    if not re.search(r"[A-Z]", password):
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        score += 1

    # Criteria 3: Lowercase letters
    if not re.search(r"[a-z]", password):
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        score += 1

   # Criteria 4: Numbers
    if not re.search(r"\d", password):
        feedback.append("Password should contain at least one number.")
    else:
        score += 1


   # Criteria 5: Special characters
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        feedback.append("Password should contain at least one special character.")
    else:
        score += 1


    if score >= 5:
        return "Strong password! Keep it safe."
    else:
        return "Weak password. " + " ".join(feedback)
    


if __name__ == "__main__":
    print("Welcome to the Password Complexity Checker!")
    print("Please enter your password below:")

    while True:
        password = input("> ")
        if password.lower() == 'exit':
            print("Exiting...")
            break
        strength_feedback = check_password_complexity(password)
        print(strength_feedback)