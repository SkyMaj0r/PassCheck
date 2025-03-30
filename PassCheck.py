import zxcvbn

def check_password_strength(password):
    result = zxcvbn.zxcvbn(password)
    score = result['score']
    feedback = result['feedback']
    
    print(f"Password strength: {score}/4")
    print(f"Estimated crack time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    
    if feedback['warning']:
        print(f"Warning: {feedback['warning']}")
    
    for suggestion in feedback['suggestions']:
        print(f"Suggestion: {suggestion}")

# Example usage
password = input("Enter a password to check: ")
check_password_strength(password)
