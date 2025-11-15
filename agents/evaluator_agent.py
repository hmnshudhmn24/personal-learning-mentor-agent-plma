class EvaluatorAgent:
    def __init__(self):
        pass

    def evaluate(self, quiz_text, answers):
        print("[Evaluator] Scoring answers (mock evaluation).")
        # Mock scoring: count 'A' as correct
        score = sum(1 for a in answers if a.strip().upper() == 'A')
        total = len(answers)
        result = {"score": score, "total": total, "percent": round(score/total*100,2)}
        return result
