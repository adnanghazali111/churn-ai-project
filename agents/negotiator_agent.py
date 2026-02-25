class NegotiatorAgent:

    def generate_response(self, risk_level, ticket_text, complaint_count, refunds_taken, policy_text):

        if risk_level == "HIGH":

            # Read max discount from policy (hardcoded 40 for now)
            max_discount = 40

            discount = min(max_discount, 10 + complaint_count * 2 + refunds_taken * 3)

            response = f"""
Subject: We Value You – Let’s Make This Right

Dear Customer,

We sincerely apologize for your recent experience.

We understand your concern:
"{ticket_text}"

Based on our internal retention guidelines:

{policy_text}

As a gesture of goodwill, we would like to offer you a {discount}% loyalty discount on your next renewal.

Your satisfaction matters deeply to us.

Best Regards,
Customer Success Team
"""

        else:
            response = "No retention action needed."

        return response