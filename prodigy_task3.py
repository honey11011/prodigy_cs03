import re
def assess_password_strength(password):
    length_weight = 1
    upper_weight = 1
    lower_weight = 1
    digit_weight = 1
    special_weight = 1
    min_length = 8
    length_score = length_weight if len(password) >= min_length else 0
    upper_score = upper_weight if re.search(r'[A-Z]', password) else 0
    lower_score = lower_weight if re.search(r'[a-z]', password) else 0
    digit_score = digit_weight if re.search(r'\d', password) else 0
    special_score = special_weight if re.search(r'[\W_]', password) else 0
    total_score = length_score + upper_score + lower_score + digit_score + special_score
    if total_score == 5:
        strength = 'Very Strong'
    elif total_score == 4:
        strength = 'Strong'
    elif total_score == 3:
        strength = 'Moderate'
    elif total_score == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'
    feedback = []
    if length_score == 0:
        feedback.append(f"Password should be at least {min_length} characters long.")
    if upper_score == 0:
        feedback.append("Password should include at least one uppercase letter.")
    if lower_score == 0:
        feedback.append("Password should include at least one lowercase letter.")
    if digit_score == 0:
        feedback.append("Password should include at least one digit.")
    if special_score == 0:
        feedback.append("Password should include at least one special character.")
    return {
        'strength': strength,
        'feedback': feedback
    }
password = input("Enter a password to assess: ")
result = assess_password_strength(password)
print(f"Password strength: {result['strength']}")
for fb in result['feedback']:
    print(f"- {fb}")