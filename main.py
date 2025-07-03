from eda_code import generate_eda_code, generate_visualization_code
from resume_generator import generate_resume
from interview_questions import generate_interview_questions
from meeting_summary import generate_meeting_summary

def run_all_tasks():
    print("\nGPT Output for task: 'Generate EDA code'\n")
    print(generate_eda_code("homeprices.csv"))

    print("\nGPT Output for task: 'Generate visualization code'\n")
    print(generate_visualization_code("homeprices.csv"))

    print("\nGPT Output for task: 'Generate a resume'\n")
    print(generate_resume())

    print("\nGPT Output for task: 'Generate interview questions'\n")
    print(generate_interview_questions())

    print("\nGPT Output for task: 'Summarize meeting notes'\n")
    print(generate_meeting_summary())

if __name__ == "__main__":
    run_all_tasks()
