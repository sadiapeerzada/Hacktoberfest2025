import re

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    # Criteria
    if len(password) < 6:
        remarks = "Too short! Use at least 8 characters."
    elif len(password) <= 10:
        strength += 1
        remarks = "Weak, try adding more characters."
    else:
        strength += 2
        remarks = "Good length."

    # Check character types
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&*()_+!]", password):
        strength += 1

    # Final score
    if strength <= 2:
        level = "⚠️ Weak"
    elif 3 <= strength <= 4:
        level = "🟡 Medium"
    else:
        level = "🟢 Strong"

    return f"Password Strength: {level}\nFeedback: {remarks}"

# Example usage
password = input("Enter your password to check: ")
print(check_password_strength(password))
