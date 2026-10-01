# LLM Code Evaluator

An AI-powered code evaluation system that uses Large Language Models (LLMs) to analyze, review, and evaluate source code. The project is designed to provide automated feedback on code quality, correctness, potential issues, and improvement areas.

## 🚀 Features

- 🤖 **AI-Powered Code Evaluation**
  - Uses an LLM to analyze submitted source code.
  - Generates meaningful and structured feedback.

- 🔍 **Code Analysis**
  - Identifies potential bugs and logical issues.
  - Reviews code structure and implementation.
  - Highlights possible improvements.

- 📊 **Structured Evaluation**
  - Provides evaluation results in an easy-to-understand format.
  - Can be extended to include scoring and multiple evaluation criteria.

- 💡 **Improvement Suggestions**
  - Provides recommendations for writing cleaner and more maintainable code.
  - Helps developers understand problems in their implementation.

- ⚡ **Automated Evaluation Pipeline**
  - Reduces the need for manual code review.
  - Can be integrated into development or learning workflows.

---

## 🏗️ How It Works

The basic workflow of the system is:

```text
User
  │
  ▼
Submit Code
  │
  ▼
Code Evaluation API
  │
  ▼
LLM Analysis
  │
  ├── Correctness
  ├── Code Quality
  ├── Bugs / Issues
  └── Improvements
  │
  ▼
Structured Evaluation
  │
  ▼
User Feedback
```

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **AI/LLM:** Large Language Model API
- **Backend:** API-based architecture
- **Environment Management:** `.env`
- **Version Control:** Git & GitHub

> The exact LLM provider and model can be configured according to the project environment.

---

## 📁 Project Structure

```text
llm-code-evaluator/
│
├── app/
│   ├── ...
│
├── tests/
│   ├── ...
│
├── .env.example
├── requirements.txt
├── README.md
└── ...
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd llm-code-evaluator
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
LLM_API_KEY=your_api_key_here
```

Add any additional configuration required by your selected LLM provider.

**Never commit your `.env` file to GitHub.**

Make sure `.gitignore` contains:

```text
.env
venv/
__pycache__/
```

---

## ▶️ Running the Project

Start the application using the project's configured entry point.

For example:

```bash
python main.py
```

If the project uses an API server such as FastAPI, run:

```bash
uvicorn main:app --reload
```

The API will then be available locally at:

```text
http://127.0.0.1:8000
```

---

## 🔌 Example Evaluation Flow

A code submission can be sent to the evaluator:

```json
{
  "language": "python",
  "code": "def add(a, b):\n    return a + b"
}
```

The evaluator processes the code using the configured LLM and returns structured feedback.

Example response:

```json
{
  "score": 9,
  "correctness": "Correct",
  "issues": [],
  "suggestions": [
    "Consider adding type hints for better readability."
  ]
}
```

> The exact request and response format depends on the implementation.

---

## 🧠 Evaluation Criteria

The evaluator can be extended to assess code using multiple criteria:

| Criteria | Description |
|---|---|
| Correctness | Checks whether the implementation solves the intended problem |
| Code Quality | Reviews readability and maintainability |
| Structure | Evaluates organization and implementation approach |
| Bugs | Identifies potential logical or implementation issues |
| Efficiency | Reviews possible time and space complexity concerns |
| Best Practices | Suggests improvements based on common coding practices |

---

## 🧪 Testing

Run the project's tests using:

```bash
pytest
```

For a specific test:

```bash
pytest tests/
```

---

## 🔮 Future Improvements

- [ ] Support multiple programming languages
- [ ] Add detailed code scoring
- [ ] Add test-case execution
- [ ] Add time and space complexity analysis
- [ ] Add code plagiarism/similarity detection
- [ ] Add web-based dashboard
- [ ] Add authentication and user management
- [ ] Add persistent evaluation history
- [ ] Support multiple LLM providers
- [ ] Add Docker deployment

---

## 🔒 Security

- Keep API keys inside environment variables.
- Never expose secret keys in source code.
- Validate user-submitted code before processing.
- Avoid executing untrusted code directly on the host machine.
- Use sandboxed execution if actual code execution is implemented.

---

## 📌 Use Cases

This project can be useful for:

- 🎓 Coding education platforms
- 💻 Programming practice systems
- 🧑‍💼 Automated code review
- 🧪 Coding assessment platforms
- 🤖 AI developer tools
- 📚 Interview preparation platforms

---

## 👨‍💻 Author

**Anshuman Singh**

Built as an AI/LLM-based developer project focused on automated code evaluation and intelligent developer feedback.

---

## ⭐ Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add new feature"
```

5. Push the branch.

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

---

## 📄 License

This project is available for educational and development purposes. Add an appropriate open-source license if you intend to distribute the project publicly.
