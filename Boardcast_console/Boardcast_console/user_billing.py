import json
import os

BILLING_FILE = "data/billing.json"
USER_SUBSCRIPTIONS_FILE = "data/user_subscriptions.json"

class UserBilling:
    @staticmethod
    def ensure_file_exists():
        """Ensure billing file exists."""
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(BILLING_FILE):
            with open(BILLING_FILE, "w") as f:
                json.dump({}, f)

    @staticmethod
    def load_billing():
        """Load billing data."""
        UserBilling.ensure_file_exists()
        with open(BILLING_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save_billing(data):
        """Save billing data."""
        with open(BILLING_FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def generate_bill(user_email):
        """Generate a bill based on the user's active subscription."""
        UserBilling.ensure_file_exists()

        # Load user's subscription
        with open(USER_SUBSCRIPTIONS_FILE, "r") as f:
            user_subscriptions = json.load(f)

        if user_email not in user_subscriptions:
            print("No active subscription found for billing.")
            return

        # Get the subscription details
        subscription = user_subscriptions[user_email]
        amount = float(subscription["Price"])  # Extract price from subscription

        # Load existing billing data
        bills = UserBilling.load_billing()

        # Store new bill
        if user_email not in bills:
            bills[user_email] = []

        bills[user_email].append({"amount": amount, "status": "Pending"})
        UserBilling.save_billing(bills)

        print(f"Bill of ${amount} generated automatically for {user_email}.")

    @staticmethod
    def make_payment(user_email, amount, method):
        """Process payment for a user's bill."""
        bills = UserBilling.load_billing()

        if user_email not in bills or not bills[user_email]:
            print("No pending bills found.")
            return

        # Get the first pending bill
        for bill in bills[user_email]:
            if bill["status"] == "Pending":
                if bill["amount"] == amount:
                    bill["status"] = "Paid"
                    bill["method"] = method
                    UserBilling.save_billing(bills)
                    print(f"Payment of ${amount} successful via {method}.")
                    return
                else:
                    print("Payment amount does not match the pending bill.")
                    return

        print("No pending bills match the entered amount.")
