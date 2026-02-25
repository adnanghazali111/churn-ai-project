class RiskAgent:

    def calculate_risk(self, churn_probability, complaint_count, refunds_taken):

        # Risk Score Formula
        risk_score = (
            0.6 * churn_probability * 100 +
            0.3 * complaint_count * 10 +
            0.1 * refunds_taken * 20
        )

        # Risk Level Classification
        if risk_score > 70:
            risk_level = "HIGH"
        elif risk_score > 40:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        return float(risk_score), risk_level