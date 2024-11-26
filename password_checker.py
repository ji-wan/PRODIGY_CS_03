import re

def check_password_strength(password):
    
    #criteria checks
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password)) 
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    #feedback
    feedback = []
    if length < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    if not has_upper:
        feedback.append("Password should have at least one uppercase letter.")
    if not has_lower:
        feedback.append("Password should have at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password should have at least one digit.")
    if not has_special:
        feedback.append("Password should have at least one special character.")
        
    #strength evaluation
    score = sum([has_upper, has_lower, has_digit, has_special]) + (length >=8)
    
    if score <= 2:
        strength = "weak passwword"
    elif score == 3:
        strength = "good password"
    else:
        strength = "strong password"
        
    return strength, feedback

#user interaction
def main():
    print("Password Complexity Checker")
    password = input("Enter your password: ").strip()
    
    strength, feedback = check_password_strength(password)
    
    print(f"\nPassword strength: {strength}")
    if feedback:
        print("suggestion for improvement:")
        for suggestion in feedback:
            print(f"- {suggestion}")
        else:
            print("your password meets all the criteria for strength.")
        
if __name__ == "__main__":
    main()