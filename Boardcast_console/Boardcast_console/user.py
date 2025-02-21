import json
import os

USER_FILE = "data/users.json"

class User:
    def __init__(self, name, email, password, contact, billing_address):
        self.name = name
        self.email = email
        self.password = password  # In a real system, store hashed passwords
        self.contact = contact
        self.billing_address = billing_address

    def to_dict(self):
        """Convert user object to dictionary."""
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "contact": self.contact,
            "billing_address": self.billing_address
        }

    @staticmethod
    def ensure_file_exists():
        """Ensure the user file exists."""
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(USER_FILE):
            with open(USER_FILE, "w") as f:
                json.dump([], f)

    @staticmethod
    def save_users(users):
        """Save all users to users.json."""
        with open(USER_FILE, "w") as f:
            json.dump(users, f, indent=4)

    @staticmethod
    def load_users():
        """Load users from users.json."""
        User.ensure_file_exists()
        with open(USER_FILE, "r") as f:
            return json.load(f)

    @classmethod
    def register(cls, name, email, password, contact, billing_address):
        """Register a new user."""
        users = cls.load_users()

        # Check if the user already exists
        for user in users:
            if user["email"] == email:
                print("User already exists!")
                return None

        new_user = cls(name, email, password, contact, billing_address)
        users.append(new_user.to_dict())
        cls.save_users(users)
        print("User registered successfully!")
        return new_user

    @classmethod
    def login(cls, email, password):
        """Authenticate a user."""
        users = cls.load_users()
        for user in users:
            if user["email"] == email and user["password"] == password:
                print("Login successful!")
                return cls(**user)

        print("Invalid email or password!")
        return None
