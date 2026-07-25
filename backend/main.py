import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from ai_service import generate_engineering_report
from pdf_generator import create_pdf


# Create PDF folder
os.makedirs("generated_reports", exist_ok=True)


app = FastAPI(
    title="AI Manufacturing Design Assistant API",
    version="1.0.0"
)


# React frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-manufacturing-design-assistant.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Static PDF folder
app.mount(
    "/reports",
    StaticFiles(directory="generated_reports"),
    name="reports"
)


class ProjectRequest(BaseModel):

    category: str

    projectName: str

    requirements: str



@app.get("/")
def root():

    return {
        "message": "AI Manufacturing Design Assistant API is running"
    }



@app.get("/health")
def health():

    return {
        "status": "ok"
    }



@app.post("/generate-report")
def generate_report(
    project: ProjectRequest,
    request: Request
):

    report = generate_engineering_report(
        category=project.category,
        project_name=project.projectName,
        requirements=project.requirements
    )


    pdf_path = create_pdf(
        project_name=project.projectName,
        report_content=report
    )


    filename = os.path.basename(pdf_path)


    pdf_url = str(request.base_url) + f"reports/{filename}"


    return {
        "report": report,
        "pdf_url": f"https://ai-manufacturing-design-assistant.onrender.com/reports/{filename}"
    }