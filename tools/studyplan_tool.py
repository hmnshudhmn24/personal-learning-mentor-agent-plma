class StudyPlanTool:
    def __init__(self):
        pass

    def generate_plan(self, user_profile):
        # Very simple rule-based plan generator
        goal = user_profile.get("goal", "").lower()
        level = user_profile.get("level", "beginner")
        if "python" in goal:
            path = ["Variables & Types", "Control Flow (if/else)", "Loops", "Functions", "Modules & Packages"]
        else:
            path = ["Introduction", "Core Concepts", "Practice", "Advanced Topics"]
        return {"path": path, "estimated_weeks": len(path)}
