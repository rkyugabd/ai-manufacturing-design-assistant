import os
from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_engineering_report(
    category: str,
    project_name: str,
    requirements: str
):

    prompt = f"""
You are a senior mechanical design engineer specialized in manufacturing engineering.

Your task is to create a preliminary engineering project proposal.

Project Category:
{category}

Project Name:
{project_name}

Customer Requirements:
{requirements}

Create a professional engineering report including:

1. Project Overview

2. Design Requirements Analysis

3. Engineering Design Proposal

4. Main Components Selection

5. Material Selection

6. Manufacturing Process

7. Assembly Process

8. Preliminary BOM (Bill of Materials)

9. Cost Estimation

10. Engineering Risks and Recommendations


Important:

- Explain engineering decisions.
- Provide realistic manufacturing considerations.
- Write like a professional engineering document.
"""


    response = client.models.generate_content(
       model="gemini-flash-latest",
        contents=prompt
    )


    return response.text