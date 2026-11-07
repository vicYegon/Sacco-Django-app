import re
from decimal import Decimal, InvalidOperation

# member registration functions
def display_welcome():
    print("=" * 50)
    print("           SACCO MEMBER REGISTRATION ")
    print("=" * 50)
    print("      Welcome to sacco management system")
    print()

def get_member_details():
    print("\nEnter Your Details")
    print("-" * 30)

    while True:
        full_name = validate_name(input("Full Name: "))

        if full_name is not None:
            break

    national_id = input("National ID: ").strip()

    while True:
        phone_number = validate_phone(input("Phone Number: "))
    
        if phone_number is not None:
            break
    
    while True:
        email = validate_email(input("Email Address: "))
    
        if email is not None:
            break

    while True:
        age = validate_age(input("Your Age: "))
    
        if age is not None:
            break

    while True:
        monthly_contribution = validate_contribution(input("Monthly Contribution (KES): "))

        if monthly_contribution is not None:
            break

    

    if full_name is None:
        print("Registration failed: Invalid name")
        return None
    
    if phone_number is None:
        print("Registration failed: Invalid phone number.")
        return None

    if email is None:
        print("Registration failed: Invalid email.")
        return None

    if age is None:
        print("Registration failed: Invalid age.")
        return None

    if monthly_contribution is None:
        print("Registration failed: Invalid contribution.")
        return None

    member = {
        "full_name": full_name,
        "national_id": national_id,
        "phone_number": phone_number,
        "email":email,
        "age": age,
        "monthly_contribution": monthly_contribution,
    }

    return member

# validation functions
def validate_age(age):
        try:
            age = int(age)

            if age < 18:
                print("Error: Member must be atleast 18 years old.")
                return None

            return age
        except ValueError:
            print("Error: Age must be a valid number.")
            return None

def validate_contribution(monthly_contribution):
    try: 
        monthly_contribution = Decimal(monthly_contribution)

        if not monthly_contribution.is_finite():
            print("Error: Contribution must be a finite number.")
            return None

        if monthly_contribution < 0:
            print("Error: Monthly contribution cannot be negative")
            return None

        if monthly_contribution.as_tuple().exponent < -2:
            print("Error: Use at most two decimal places.")
            return None

        return monthly_contribution 

    except InvalidOperation:
        print("Error: Enter a valid contribution amount.")
        return None

def validate_name(full_name):
    full_name = full_name.strip()

    if not full_name:
        print("Error: Name cannot be empty.")
        return None

    if len(full_name) < 4:
        print("Error: Name must contain at least 4 characters.")
        return None
    
    return full_name
    
def validate_phone(phone_number):
    phone_number = phone_number.strip()

    pattern = r"^(?:0[17]\d{8}|\+?254[17]\d{8})$"

    if not re.fullmatch(pattern, phone_number):
        print("Error: Enter a valid Kenyan mobile number.")
        return None

    return phone_number

def validate_email(email):
    email = email.strip()

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(pattern, email):
        print("Error: Enter a valid email address.")
        return None

    return email



if __name__=="__main__":
    display_welcome()

    member = get_member_details()
    
    if member is not None:
        print("\nMember Details Captured:")
        print(member)