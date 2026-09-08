from password_strength_analyzer import analyze_password

examples = {
    "123456": "Weak",
    "hello123": "Medium",
    "Secure@2026Test": "Strong",
}

for password, expected in examples.items():
    result = analyze_password(password)
    print(password, "->", result["verdict"], "(expected:", expected + ")")
