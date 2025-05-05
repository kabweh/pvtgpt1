# ai_tutor_project/quiz_generator.py
from langchain import PromptTemplate, LLMChain

class QuizGenerator:
    def __init__(self):
        self.chain = LLMChain(
            prompt=PromptTemplate(
                input_variables=["content"],
                template="Generate 5 comprehension MCQs from the following content:\n\n{content}"
            )
        )

    def generate(self, text: str) -> list:
        out = self.chain.run(content=text)
        # parse into list by line
        return [line for line in out.split('\n') if line.strip()]
