from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status")
def get_status():
    return {
        "risk": "HIGH",
        "zones": {
            "A": "MEDIUM",
            "B": "CRITICAL",
            "C": "HIGH"
        },
        "alerts": [
            "Abnormal crowd surge detected at Sector B",
            "Immediate inflow restriction advised",
            "Medical teams moved to standby"
        ]
    }
