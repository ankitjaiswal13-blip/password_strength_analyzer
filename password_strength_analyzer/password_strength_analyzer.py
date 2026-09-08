import re

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "qwerty123", "admin", "admin123",
    "letmein", "welcome", "iloveyou"
}

def analyze_password(password):
    score = 0
    suggestions = []

    length = len(password)

    # Length
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters; 12+ is better.")

    # Character diversity
    checks = [
        (r"[A-Z]", "Add at least one uppercase letter (A-Z)."),
        (r"[a-z]", "Add at least one lowercase letter (a-z)."),
        (r"\d", "Add at least one number (0-9)."),
        (r"[^A-Za-z0-9]", "Add at least one special character.")
    ]

    for pattern, suggestion in checks:
        if re.search(pattern, password):
            score += 1
        else:
            suggestions.append(suggestion)

    # Uniqueness / common-password check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append("Avoid common or easily guessed passwords.")

    # Repeated-character check
    if re.search(r"(.)\1\1", password):
        score = max(0, score - 1)
        suggestions.append("Avoid repeating the same character three or more times.")

    # Verdict
    if score <= 2:
        verdict = "Weak"
    elif score <= 4:
        verdict = "Medium"
    else:
        verdict = "Strong"

    return {
        "length": length,
        "score": score,
        "verdict": verdict,
        "suggestions": suggestions
    }


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    password = input("Enter a password to check: ")

    result = analyze_password(password)

    print("\nPassword Analysis")
    print("-" * 45)
    print(f"Length:   {result['length']}")
    print(f"Score:    {result['score']}/6")
    print(f"Verdict:  {result['verdict']}")

    if result["suggestions"]:
        print("\nSuggestions:")
        for suggestion in result["suggestions"]:
            print(f"- {suggestion}")
    else:
        print("\nNo major improvements suggested.")

    print("\nNote: This tool analyzes password characteristics locally.")
    print("Do not enter a real password that you currently use.")


if __name__ == "__main__":
    main()
