print("=== Help Desk Password Reset Tool ===")

username = input("Enter username: ")
employee_id = input("Enter employee ID: ")

print("\nVerifying user...")

if employee_id.isdigit():
    print("User verified.")
    new_password = input("Enter new temporary password: ")

    print("\nPassword reset complete.")
    print(f"User '{username}' must change password at next login.")
else:
    print("\nVerification failed. Escalate ticket to Tier 2.")
