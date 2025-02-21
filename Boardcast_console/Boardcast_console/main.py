from user import User
from user_subscription import UserSubscription
from user_billing import UserBilling
from admin import Admin

def main():
    while True:
        print("\n=== Broadcast Console ===")
        print("1. Register")
        print("2. Login")
        print("3. Admin Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                password = input("Enter password: ")
                contact = input("Enter contact: ")
                billing_address = input("Enter billing address: ")
                User.register(name, email, password, contact, billing_address)

            case "2":
                email = input("Enter email: ")
                password = input("Enter password: ")
                user_logged_in = User.login(email, password)

                if user_logged_in:
                    while True:
                        print("\n=== Subscription & Billing ===")
                        print("1. View Subscription Details")
                        print("2. Subscribe to a Plan")
                        print("3. Cancel Subscription")
                        print("4. Generate Bill")
                        print("5. Make Payment")
                        print("6. Logout")

                        sub_choice = input("Enter your choice: ")

                        match sub_choice:
                            case "1":
                                UserSubscription.view_subscription_details()

                            case "2":
                                plan_id = input("Enter Plan ID to Subscribe: ")
                                UserSubscription.subscribe(user_logged_in.email, plan_id)

                            case "3":
                                UserSubscription.cancel_subscription(user_logged_in.email)

                            case "4":
                                UserBilling.generate_bill(user_logged_in.email)

                            case "5":
                                amount = float(input("Enter amount to pay: "))
                                print("Select Payment Method: 1. Credit Card  2. PayPal  3. UPI")
                                method = input("Enter your choice: ")
                                UserBilling.make_payment(user_logged_in.email, amount, method)

                            case "6":
                                print("Logging out...")
                                break

                            case _:
                                print("Invalid choice. Try again.")

            case "3":
                admin_pass = input("Enter Admin Password: ")
                Admin.admin_login(admin_pass)

            case "4":
                print("Exiting the application...")
                break

            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
