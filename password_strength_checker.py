import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (minimum 8 characters)": length_error,
        "Missing a digit": digit_error,
        "Missing an uppercase letter": uppercase_error,
        "Missing a lowercase letter": lowercase_error,
        "Missing a symbol": symbol_error
    }

    if all(not error for error in errors.values()):
        return "✅ Strong Password", errors
    elif sum(errors.values()) <= 2:
        return "⚠️ Moderate Password", errors
    else:
        return "❌ Weak Password", errors

# --- Main Program ---
password = input("🔑 Enter your password to check strength: ")
strength, issues = check_password_strength(password)

print("\nPassword Strength:", strength)
for issue, is_problem in issues.items():
    if is_problem:
        print("•", issue)
