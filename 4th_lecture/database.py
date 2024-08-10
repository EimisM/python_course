admin_users = ["admin", "sudo", "superuser"]
user_input = input("Please insert your username ")

if user_input not in admin_users:
    print("Welcome")
else:
    print(f"Welcome back {user_input}")