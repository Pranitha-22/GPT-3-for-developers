from gpt_utils import ask_gpt

def generate_interview_questions(language):
    prompt = f"Generate 10 interview questions in English."
    return ask_gpt(prompt)
