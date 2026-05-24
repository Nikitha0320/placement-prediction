from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from routes.placement_predict import predict_placement
from routes.risk_scoring import get_risk_prediction
from routes.bias_scoring import get_bias_analysis
from routes.skill_gap import predict_skill_gap

app = FastAPI( title="Placement Prediction API",
    description="Student Placement Prediction System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Change later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#-------------Student input schema----------------

class StudentInput(BaseModel):
    age: int
    cgpa: float
    coding_skill_score: int 
    mock_interview_score: int
    logical_reasoning_score: int
    communication_skill_score: int
    projects_count: int
    internships_count: int
    aptitude_score: int
    attendance_percentage: float
    backlogs: int
    gender: str
    branch: str

# ---------------- Home Route ----------------

@app.get("/")
def home():

    return {
        "message":
        "Placement Prediction API Running Successfully"
    }



#---------------- Placement Prediction Endpoint ----------------

@app.post("/predict_placement")
def placement_prediction(student: StudentInput):

    result = predict_placement(
        student.dict()
    )

    return result

# ---------------- Risk Scoring ----------------

@app.post("/risk-score")
def risk_score(student: StudentInput):

    result = get_risk_prediction(
        student.dict()
    )

    return result

# ---------------- Bias Analysis ----------------

@app.get("/bias-analysis")
def bias_analysis():

    return get_bias_analysis()
# ---------------- Skill Gap Prediction ----------------

@app.post("/skill-gap")
def skill_gap_prediction(student: StudentInput):

    result = predict_skill_gap(
        student.dict()
    )

    return result