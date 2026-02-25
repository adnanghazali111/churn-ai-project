import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agents.feature_agent import FeatureAgent
from agents.risk_agent import RiskAgent
from agents.negotiator_agent import NegotiatorAgent
from agents.research_agent import ResearchAgent


# ----------------------------
# Logging Configuration
# ----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ----------------------------
# Request Model
# ----------------------------
class SupportTicket(BaseModel):
    ticket_text: str
    complaint_count: int
    refunds_taken: int
    subscription_months: int


# ----------------------------
# Response Model
# ----------------------------
class PredictionResponse(BaseModel):
    churn_probability: float
    risk_score: float
    risk_level: str
    retention_email: str


# ----------------------------
# App Initialization
# ----------------------------
app = FastAPI()

feature_agent = FeatureAgent()
risk_agent = RiskAgent()
negotiator_agent = NegotiatorAgent()
research_agent = ResearchAgent()


# ----------------------------
# Prediction Endpoint
# ----------------------------
@app.post("/predict", response_model=PredictionResponse)
def predict(ticket: SupportTicket):

    try:
        logger.info("Received support ticket")

        ticket_text = ticket.ticket_text
        complaint = ticket.complaint_count
        refund = ticket.refunds_taken
        sub = ticket.subscription_months

        logger.info(f"Ticket text: {ticket_text}")

        # Agent 1 → ML Prediction
        prob = feature_agent.predict_churn(ticket_text, complaint, refund, sub)
        logger.info(f"Churn probability predicted: {prob}")

        # Agent 2 → Risk Calculation
        risk_score, risk_level = risk_agent.calculate_risk(prob, complaint, refund)
        logger.info(f"Risk score: {risk_score} | Risk level: {risk_level}")

        # Agent 3 → Policy Research
        policy_text = research_agent.get_policy()

        # Agent 4 → Negotiation
        retention_email = negotiator_agent.generate_response(
            risk_level,
            ticket_text,
            complaint,
            refund,
            policy_text
        )

        logger.info("Retention response generated successfully")

        return {
            "churn_probability": prob,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "retention_email": retention_email
        }

    except Exception as e:
        logger.error(f"Processing error: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail=f"Internal Processing Error: {str(e)}"
        )