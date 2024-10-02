import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_char_criteria = re.search(r"[@$!%*?&#]", password) is not None

    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    if score == 5:
        return "Strong Password", None
    elif score >= 3:
        feedback = "Your password is medium. Try adding:"
        if not length_criteria:
            feedback += "\n- More characters (at least 8)."
        if not lowercase_criteria:
            feedback += "\n- Lowercase letters."
        if not uppercase_criteria:
            feedback += "\n- Uppercase letters."
        if not number_criteria:
            feedback += "\n- Numbers."
        if not special_char_criteria:
            feedback += "\n- Special characters (e.g., @$!%*?&#)."
        return "Medium Password", feedback
    else:
        feedback = "Your password is weak. Consider the following improvements:"
        if not length_criteria:
            feedback += "\n- Make it longer (at least 8 characters)."
        if not lowercase_criteria:
            feedback += "\n- Add lowercase letters."
        if not uppercase_criteria:
            feedback += "\n- Add uppercase letters."
        if not number_criteria:
            feedback += "\n- Add numbers."
        if not special_char_criteria:
            feedback += "\n- Add special characters (e.g., @$!%*?&#)."
        return "Weak Password", feedback

password = input("Enter a password to check: ")
strength, feedback = check_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print(feedback)














