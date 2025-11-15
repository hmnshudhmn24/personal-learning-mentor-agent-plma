# Personal Learning Mentor Agent (PLMA)

A multi-agent system that designs personalized learning paths, teaches concepts, generates quizzes, evaluates answers, and tracks long-term progress. Built as a demo for the Kaggle AI Agents Intensive Capstone.

## Features
- Multi-agent architecture (Planner, Tutor, Quiz, Evaluator, Tracker, Orchestrator)
- Custom tools for study plan generation and quiz creation
- Code execution examples for programming exercises (mocked)
- In-memory session & memory bank for personalization
- Mock LLM fallback for offline demos; optional real LLM integration via env vars

## Quickstart
1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the demo:
```bash
python main.py
```

3. Open `outputs/` to see generated quizzes, progress.json and sample report.

## Notes
- Do NOT commit API keys.
- This is a demo scaffold — customize and extend for production.

