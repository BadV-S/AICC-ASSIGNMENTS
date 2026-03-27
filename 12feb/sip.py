# ----------------------------------------
# Smart Input Program
# ----------------------------------------

def categorize_age(age):
    """
    Categorizes age into different groups
    using conditional statements.
    """
    if age < 0:
        return "Invalid Age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior Citizen"


def main():
    print("=== Smart Input Program ===\n")

    # Taking user inputs
    name = input("Enter your name: ").strip()
    
    try:
        age = int(input("Enter your age: ").strip())
    except ValueError:
        print("❌ Invalid age! Please enter a number.")
        return
    
    hobby = input("Enter your hobby: ").strip()

    # Categorizing age
    age_category = categorize_age(age)

    if age_category == "Invalid Age":
        print("❌ Age cannot be negative.")
        return

    # Personalized Message
    print("\n--- Personalized Message ---")
    print(f"Hello {name}! 👋")
    print(f"You are classified as: {age_category}.")
    print(f"It's awesome that you enjoy {hobby}! Keep pursuing it! 🚀")


if __name__ == "__main__":
    main()