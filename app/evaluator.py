import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def evaluate_code(code: str, language: str, problem: str):

    prompt = f"""
You are an expert software engineer and coding interviewer.

Evaluate the following code.

Problem:
{problem}

Programming Language:
{language}

Code:
```{language}
{code}
"""