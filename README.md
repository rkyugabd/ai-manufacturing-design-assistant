# AI Manufacturing Design Assistant

An AI-powered engineering assistant that generates manufacturing design proposals, engineering reports, and PDF documentation using Generative AI.

---

## Live Demo

**Frontend**  
https://ai-manufacturing-design-assistant.vercel.app/

**Backend API**  
https://ai-manufacturing-design-assistant.onrender.com/

**API Documentation**  
https://ai-manufacturing-design-assistant.onrender.com/docs

---

## Overview

AI Manufacturing Design Assistant helps engineers quickly generate manufacturing documentation using AI.

Users enter:

- Manufacturing Category
- Project Name
- Engineering Requirements

The system automatically generates:

- Engineering Proposal
- Design Recommendations
- Material Selection
- Manufacturing Process
- Bill of Materials (BOM)
- Cost Estimation
- Risk Analysis
- PDF Engineering Report

---

## System Architecture

```text
React Frontend
       │
       ▼
FastAPI Backend
       │
       ▼
Google Gemini AI
       │
       ▼
Engineering Report
       │
       ▼
PDF Generator
```

---

## Technology Stack

### Frontend

- React
- Vite
- JavaScript
- CSS

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

### AI

- Google Gemini API
- Prompt Engineering

### Deployment

- Vercel
- Render
- GitHub

---

## Features

### AI Engineering Report Generation

Generate complete manufacturing engineering reports from user requirements.

Example Input

Category

```
Trailer Design
```

Project

```
50 Ton Grain Trailer
```

Requirements

```
Payload: 50 tons

Steel Frame

Ontario Transportation

Hydraulic Discharge System
```

Generated Output

- Project Overview
- Engineering Design
- Material Selection
- Manufacturing Process
- Quality Control
- BOM
- Cost Estimation
- Engineering Risks
- PDF Report

---

### PDF Export

Automatically generates downloadable engineering PDF reports.

---

### REST API

Health Check

```
GET /health
```

Generate Report

```
POST /generate-report
```

Example Request

```json
{
  "category": "Trailer Design",
  "projectName": "50 Ton Grain Trailer",
  "requirements": "Payload 50 tons, steel frame, hydraulic discharge system"
}
```

---

## Current Version (V1)

Completed

- React Frontend
- FastAPI Backend
- Gemini AI Integration
- Prompt Engineering
- Engineering Report Generation
- PDF Export
- REST API
- Cloud Deployment
- Production-ready Demo

---

## Future Development (V2)

### Enterprise Database Integration

The AI assistant will connect to company engineering databases.

Future Workflow

```text
User Requirement
        │
        ▼
AI Assistant
        │
        ▼
Company Database
        │
        ▼
Engineering Recommendation
```

Example Company Database

```
Part Number

GB-1001

Type

Industrial Gearbox

Material

Alloy Steel

Manufacturing Process

CNC Machining

Heat Treatment

Assembly

Status

Approved
```

Current AI

```
Recommended gearbox:

A

B

C
```

Future AI

```
Recommended gearbox:

GB-1001

Reason:

Already approved by company

Suitable torque capacity

Existing manufacturing process

Lower production cost

Available inventory
```

---

## Future Development (V3)

### Specialized AI Prompt System

Each engineering module will have its own prompt.

Examples

```
Gearbox Design Prompt

Trailer Design Prompt

Sheet Metal Prompt

Machining Prompt

Material Selection Prompt

Welding Prompt

Assembly Planning Prompt

Manufacturing Cost Prompt

BOM Generation Prompt

Quality Inspection Prompt
```

Benefits

- Better engineering accuracy
- Faster AI response
- Easier maintenance
- Modular architecture
- Higher quality output

---

## Future Development (V4)

### AI Manufacturing Platform

Future Features

- ERP Integration
- Engineering Database
- BOM Optimization
- Manufacturing Routing (BOO)
- Process Planning
- Supplier Recommendation
- Inventory Lookup
- Cost Estimation
- AI Design Assistant
- CAD Integration
- Engineering Knowledge Base
- Multi-Agent AI Workflow

---

## Project Purpose

This project demonstrates practical experience building a complete AI-powered engineering application.

Skills Demonstrated

- Full Stack Development
- React
- FastAPI
- Python
- REST API
- Prompt Engineering
- Google Gemini API
- PDF Generation
- Cloud Deployment
- AI Application Development
- Software Architecture

---

## Future Vision

This project is evolving toward an Enterprise AI Manufacturing Assistant capable of combining Large Language Models with real company engineering data.

Instead of generating generic engineering reports, future versions will understand:

- Company Parts Database
- Approved Components
- Manufacturing Standards
- BOM
- BOO (Bill of Operations)
- Supplier Information
- Engineering Rules

This allows AI to generate engineering reports using actual enterprise data rather than generic recommendations.

---

## Author

Portfolio Project

AI Application Development

Full Stack Development

Manufacturing Engineering Automation

Built for demonstrating practical AI software engineering skills to employers.
