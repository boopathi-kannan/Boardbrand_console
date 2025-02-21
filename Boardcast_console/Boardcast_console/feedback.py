import json

FEEDBACK_FILE = "data/feedback.json"

class Feedback:
    @staticmethod
    def submit_feedback(user_email, feedback, rating):
        print("Feedback submitted! Thank you.")
