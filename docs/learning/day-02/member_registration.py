def display_welcome():
    print("=" * 50)
    print("           SACCO MEMBER REGISTRATION ")
    print("=" * 50)
    print("      Welcome to sacco management system")
    print()

def get_member_details():
    print("\nEnter Your Details")
    print("-" * 30)

    full_name = input("Full Name: ").strip()
    national_id = input("National ID: ").strip()
    phone_number = input("Phone Number: ").strip()
    email = input("Email Address: ").strip()
    age = validate_age(input("Your Age: "))
    monthly_contribution = input("Monthly Contribution (KES): ").strip()

    if age is None:
        print("Registration failed: Invalid age.")
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


if __name__=="__main__":
    display_welcome()

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

    member = get_member_details()
    
    if member is not None:
        print("\nMember Details Captured:")
        print(member)