import json
import os

class TrackerAgent:
    def __init__(self, session_service):
        self.session = session_service
        self.file = "outputs/progress_data.json"

    def update_progress(self, user, topic, eval_res):
        data = {"user": user, "topic": topic, "evaluation": eval_res}
        os.makedirs("outputs", exist_ok=True)
        with open(self.file, "w") as f:
            json.dump(data, f, indent=2)
        self.session.set("last_progress", data)
        print("[Tracker] Progress updated.")
