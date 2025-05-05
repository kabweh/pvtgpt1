# ai_tutor_project/lesson_explainer.py
import manus_ai_sdk

class LessonExplainer:
    def __init__(self, api_key: str = None):
        self.client = manus_ai_sdk.Client(api_key)

    def explain(self, text: str, level: str="medium") -> dict:
        # send text to MANUS AI with anchor points
        response = self.client.generate_explanation(content=text, difficulty=level)
        return response  # expected dict with text & highlight spans
