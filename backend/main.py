import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from ai_service import generate_engineering_report
from pdf_generator import create_pdf


# 自动创建PDF目录（避免 generated_reports 不存在报错）
os.makedirs("generated_reports", exist_ok=True)


app = FastAPI(
    title="AI Manufacturing Design Assistant API",
    version="1.0.0"
)


# React connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# PDF folder
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
def generate_report(project: ProjectRequest):

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

    return {
        "report": report,
        "pdf_url": f"http://127.0.0.1:8000/reports/{filename}"
    }