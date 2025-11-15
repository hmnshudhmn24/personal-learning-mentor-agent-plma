import random

class QuizAgent:
    def __init__(self):
        pass

    def generate_quiz(self, topic, num_questions=5):
        print(f"[Quiz] Generating {num_questions} questions for {topic}")
        qs = []
        for i in range(1, num_questions+1):
            qs.append(f"Q{i}. What is a core concept in {topic}? (A/B/C/D)")
        return "\\n".join(qs)
