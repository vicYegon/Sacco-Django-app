import re
from decimal import Decimal, InvalidOperation

# member registration functions
def display_welcome():
    print("=" * 50)
    print("           SACCO MEMBER REGISTRATION ")
    print("=" * 50)
    print("      Welcome to sacco management system")
    print()



class Member:
    def __init__(
        self, 
        membership_number,
        full_name,
        national_id,
        phone_number,
        email,
        age,
        monthly_contribution
    ):

        self.membership_number = membership_number
        self.full_name = full_name
        self.national_id = national_id
        self.phone_number = phone_number
        self.email = email
        self.age = age
        self.monthly_contribution = monthly_contribution
        self.status = "ACTIVE"

    def display_details(self):
        print("\n" + "=" * 50)
        print("         MEMBER INFORMATION")
        print("=" * 50)

        print(f"Membership number: {self.membership_number}")
        print(f"Full name: {self.full_name}")
        print(f"National ID: {self.national_id}")
        print(f"Phone number: {self.phone_number}")
        print(f"Email Address: {self.email}")
        print(f"Age: {self.age}")
        print(f"Monthly Contribution: KES {self.monthly_contribution:,.2f}")
        print(f"Status: {self.status}")

        print("=" * 45)

def generate_membership_number(member_count):
    return f"SACCO-{member_count + 1:04d}"


# get member details function
def get_member_details(members):
    print("\nEnter Your Details")
    print("-" * 30)

    # loop breaking input of details untill input is corrected
    while True:
        full_name = validate_name(input("Full Name: "))

        if full_name is not None:
            break

    while True:
        national_id = validate_national_id(input("National ID: "))

        if national_id is None:
            continue

        if is_duplicate_national_id(national_id, members):
            print("Error: A member with this national ID already exists.")
            print("Please enter a diffrent National ID.")
            continue

        break

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

    
    # conditions checking if validation passed
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

    #dictionary for how member details are displayed & saved
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

def validate_national_id(national_id):
    national_id = national_id.strip()

    if not national_id.isdigit():
        print("Error: National ID must contain only numbers.")
        return None

    if len(national_id) not in (7, 8):
        print("Error: National ID must contain 7 or 8 digits.")
        return None

    return national_id

#checking for duplicate national ID's
def is_duplicate_national_id(national_id, members):
    for member in members:
        if member.national_id == national_id:
            return True

    return False

def register_member(members):
    member_details = get_member_details(members)

    if member_details is None:
        print("Registration cancelled.")
        return 

    national_id = member_details["national_id"]

    if is_duplicate_national_id(national_id, members):
        print("Error: A member with this national ID already exists.")
        return

    membership_number = generate_membership_number(len(members))

    member = Member(
        membership_number=membership_number, 
        **member_details
    )

    members.append(member)

    print("\nMember successfully registered!")

# function to display registered members
def view_members(members):
    #check wether member list is empty
    if not members:
        print("\nNo members registered yet.")
        return

    print("\nREGISTERED SACCO MEMBERS")
    print("=" * 45)

    for member in members:
        print(
            f"{member.membership_number} | "
            f"{member.full_name} | "
            f"{member.phone_number} | "  
            f"{member.status}"
        )

#application menu
def display_menu():
    print("\n" + "=" * 50)
    print("           SACCO MAIN MENU")
    print("=" * 50)

    print("1. Register Member")
    print("2. View Registered Members")
    print("3. Exit")

    print("=" * 50)

# main program
if __name__=="__main__":
    display_welcome()

    members = []

    #creating application loop
    while True:
        display_menu()

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            register_member(members)

        elif choice == "2":
            view_members(members)

        elif choice == "3":
            print("\nThank you for using SACCO management system")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")
