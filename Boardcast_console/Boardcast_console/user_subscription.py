import json
import os

SUBSCRIPTION_FILE = "data/subscriptions.json"
USER_SUBSCRIPTIONS_FILE = "data/user_subscriptions.json"

class UserSubscription:
    @staticmethod
    def ensure_file_exists():
        """Ensure subscription and user subscription files exist."""
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(SUBSCRIPTION_FILE):
            with open(SUBSCRIPTION_FILE, "w") as f:
                json.dump({}, f)  # Empty JSON object for subscription plans
        if not os.path.exists(USER_SUBSCRIPTIONS_FILE):
            with open(USER_SUBSCRIPTIONS_FILE, "w") as f:
                json.dump({}, f)  # Empty JSON object for user subscriptions

    @staticmethod
    def load_subscriptions():
        """Load all available subscription plans."""
        UserSubscription.ensure_file_exists()
        with open(SUBSCRIPTION_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save_user_subscriptions(data):
        """Save user subscriptions to file."""
        with open(USER_SUBSCRIPTIONS_FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_user_subscriptions():
        """Load user subscriptions from file."""
        UserSubscription.ensure_file_exists()
        with open(USER_SUBSCRIPTIONS_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def view_subscription_details():
        """Display all available subscription plans."""
        subscriptions = UserSubscription.load_subscriptions()

        if not subscriptions:
            print("No subscription plans available.")
            return

        print("\n=== Available Subscription Plans ===")
        for plan_id, details in subscriptions.items():
            print(f"Plan ID: {plan_id}")
            print(f"   Speed: {details['Speed']}")
            print(f"   Price: ${details['Price']}")
            print(f"   Duration: {details['Duration']}")
            print("-" * 30)

    @staticmethod
    def subscribe(user_email, plan_id):
        """Subscribe a user to a plan."""
        subscriptions = UserSubscription.load_subscriptions()
        user_subscriptions = UserSubscription.load_user_subscriptions()

        if plan_id not in subscriptions:
            print("Invalid Plan ID. Subscription failed.")
            return

        # Save user's subscription
        user_subscriptions[user_email] = subscriptions[plan_id]

        UserSubscription.save_user_subscriptions(user_subscriptions)
        print(f"User {user_email} successfully subscribed to Plan ID {plan_id}.")

    @staticmethod
    def cancel_subscription(user_email):
        """Cancel the user's subscription."""
        user_subscriptions = UserSubscription.load_user_subscriptions()

        if user_email not in user_subscriptions:
            print("No active subscription found to cancel.")
            return

        del user_subscriptions[user_email]
        UserSubscription.save_user_subscriptions(user_subscriptions)
        print(f"Subscription canceled for {user_email}.")
