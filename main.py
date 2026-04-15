from fastapi import FastAPI
from pydantic import BaseModel
from ai_logic import analyze_symptoms, analyze_vitals

app = FastAPI(title="Healthcare AI MCP Server")

# -------- Request Models --------

class SymptomInput(BaseModel):
    symptoms: list

class VitalInput(BaseModel):
    heart_rate: int
    blood_pressure: int

# -------- MCP Tools (APIs) --------

@app.get("/")
def root():
    return {"message": "Healthcare AI MCP Server Running"}

@app.post("/analyze_symptoms")
def symptom_analysis(input: SymptomInput):
    result = analyze_symptoms(input.symptoms)
    return {
        "tool": "analyze_symptoms",
        "input": input.symptoms,
        "output": result
    }

@app.post("/check_vitals")
def vital_analysis(input: VitalInput):
    result = analyze_vitals(input.heart_rate, input.blood_pressure)
    return {
        "tool": "check_vitals",
        "output": result
    }

@app.post("/get_recommendation")
def recommendation(input: SymptomInput):
    result = analyze_symptoms(input.symptoms)

    if result["risk"] == "High":
        advice = "Consult doctor immediately"
    elif result["risk"] == "Medium":
        advice = "Take rest and monitor symptoms"
    else:
        advice = "No major concern"

    return {
        "tool": "get_recommendation",
        "disease": result["disease"],
        "advice": advice
    }
