#!/usr/bin/env python3
from agents.orchestrator_agent import OrchestratorAgent
from tools.studyplan_tool import StudyPlanTool
from memory.session_service import InMemorySessionService
import json
from pathlib import Path

def main():
    session = InMemorySessionService()
    tool = StudyPlanTool()
    orchestrator = OrchestratorAgent(session, tool)
    # simple demo user
    user_profile = {
        "name": "Demo Learner",
        "goal": "Learn Python basics",
        "level": "beginner",
        "time_per_week": 5
    }
    out = orchestrator.run_session(user_profile)
    Path("outputs").mkdir(exist_ok=True)
    with open("outputs/progress.json","w") as f:
        json.dump(out, f, indent=2)
    print("Demo finished. Check outputs/progress.json and outputs/quiz.txt")

if __name__ == '__main__':
    main()
