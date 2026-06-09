try:
    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()

    if name == "" or feedback == "":
        raise ValueError("Name or feedback cannot be empty!")

    print("\nThank you,", name)
    print("Your feedback:", feedback)

except ValueError as e:
    print("Error:", e)

finally:
    print("\nThank you for visiting our restaurant 😊")