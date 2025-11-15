from .planner_agent import PlannerAgent
from .tutor_agent import TutorAgent
from .quiz_agent import QuizAgent
from .evaluator_agent import EvaluatorAgent
from .tracker_agent import TrackerAgent
from pathlib import Path
import json

OUT_DIR = Path("outputs")
OUT_DIR.mkdir(exist_ok=True)

class OrchestratorAgent:
    def __init__(self, session, plan_tool):
        self.session = session
        self.planner = PlannerAgent(plan_tool)
        self.tutor = TutorAgent()
        self.quiz = QuizAgent()
        self.evaluator = EvaluatorAgent()
        self.tracker = TrackerAgent(session)

    def run_session(self, user_profile):
        # Plan
        plan = self.planner.create_plan(user_profile)
        # Teach first topic
        topic = plan['path'][0]
        lesson = self.tutor.teach(topic)
        # Generate quiz
        quiz_text = self.quiz.generate_quiz(topic, num_questions=5)
        # Evaluate sample answers (mock)
        sample_answers = ['A','B','C','D','A']
        eval_res = self.evaluator.evaluate(quiz_text, sample_answers)
        # Update progress
        self.tracker.update_progress(user_profile['name'], topic, eval_res)
        OUT_DIR.joinpath("quiz.txt").write_text(quiz_text)
        OUT_DIR.joinpath("lesson.txt").write_text(lesson)
        return {"plan": plan, "evaluation": eval_res}
