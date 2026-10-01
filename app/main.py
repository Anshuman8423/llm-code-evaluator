from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.evaluator import evaluate_code


app = FastAPI(
    title="LLM Code Evaluator",
    description="AI-powered code evaluation API",
    version="1.0.0"
)


class CodeRequest(BaseModel):
    code: str
    language: str
    problem: str


@app.get("/")
def root():
    return {
        "message": "LLM Code Evaluator API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/evaluate")
def evaluate(request: CodeRequest):

    if not request.code.strip():
        raise HTTPException(
            status_code=400,
            detail="Code cannot be empty"
        )

    if not request.problem.strip():
        raise HTTPException(
            status_code=400,
            detail="Problem statement cannot be empty"
        )

    try:
        result = evaluate_code(
            code=request.code,
            language=request.language,
            problem=request.problem
        )

        return {
            "success": True,
            "evaluation": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )