import json

def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

def analyze_symptoms(user_symptoms):
    data = load_data()

    for entry in data:
        if all(symptom in user_symptoms for symptom in entry["symptoms"]):
            return {
                "disease": entry["disease"],
                "risk": entry["risk"]
            }

    return {
        "disease": "Unknown",
        "risk": "Low"
    }

def analyze_vitals(heart_rate, bp):
    if heart_rate > 100 or bp > 140:
        return "High Risk"
    elif heart_rate < 60:
        return "Low Risk"
    else:
        return "Normal"
