import json
import os

SUBSCRIPTION_FILE = "data/subscriptions.json"

class Admin:
    ADMIN_PASSWORD = "admin123"

    @staticmethod
    def ensure_file_exists():
        """Ensures the subscription file exists."""
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(SUBSCRIPTION_FILE):
            with open(SUBSCRIPTION_FILE, "w") as f:
                json.dump({}, f)

    @classmethod
    def admin_login(cls, password):
        """Admin login to manage subscription plans."""
        if password == cls.ADMIN_PASSWORD:
            print("Admin logged in successfully!")

            while True:
                print("\n=== Admin Console ===")
                print("1. Add Subscription Plan")
                print("2. View Plans")
                print("3. Logout")

                choice = input("Enter choice: ")

                if choice == "1":
                    plan_id = input("Enter Plan ID: ")
                    speed = input("Enter Speed: ")
                    price = float(input("Enter Price: "))
                    duration = input("Enter Duration (e.g., 1 month, 3 months): ")

                    cls.add_plan(plan_id, speed, price, duration)

                elif choice == "2":
                    cls.view_plans()

                elif choice == "3":
                    print("Logging out from Admin...")
                    break

                else:
                    print("Invalid choice. Try again.")

        else:
            print("Invalid Admin Password!")

    @classmethod
    def add_plan(cls, plan_id, speed, price, duration):
        """Adds a new subscription plan."""
        cls.ensure_file_exists()

        with open(SUBSCRIPTION_FILE, "r") as f:
            plans = json.load(f)

        if plan_id in plans:
            print("Plan ID already exists!")
            return

        plans[plan_id] = {
            "Speed": speed,
            "Price": price,
            "Duration": duration
        }

        with open(SUBSCRIPTION_FILE, "w") as f:
            json.dump(plans, f, indent=4)

        print(f"Subscription Plan {plan_id} added successfully!")

    @classmethod
    def view_plans(cls):
        """Displays available subscription plans."""
        cls.ensure_file_exists()

        with open(SUBSCRIPTION_FILE, "r") as f:
            plans = json.load(f)

        if not plans:
            print("No subscription plans available.")
        else:
            print("\n=== Available Subscription Plans ===")
            for plan_id, details in plans.items():
                print(f"Plan ID: {plan_id}")
                print(f"   Speed: {details['Speed']}")
                print(f"   Price: ${details['Price']}")
                print(f"   Duration: {details['Duration']}")
                print("-" * 30)
