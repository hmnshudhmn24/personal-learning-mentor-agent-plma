class PlannerAgent:
    def __init__(self, plan_tool):
        self.tool = plan_tool

    def create_plan(self, user_profile):
        # Use tool to design a simple plan
        plan = self.tool.generate_plan(user_profile)
        print("[Planner] Plan created with", len(plan['path']), "topics.")
        return plan
