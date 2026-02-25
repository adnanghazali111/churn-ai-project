class ResearchAgent:

    def __init__(self):
        self.policy_text = self.load_policy()

    def load_policy(self):
        try:
            with open("policy.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            return "No policy file found."

    def get_policy(self):
        return self.policy_text