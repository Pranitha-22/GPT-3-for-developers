from gpt_utils import ask_gpt

def generate_meeting_summary():
    meeting_notes = """
    Max: Profits up 50%
    Ruby: New servers are online
    Kyle: Need more time to fix software
    Walker: Happy to help
    Parkman: Beta testing almost done
    """
    prompt = f"Summarize the following meeting notes:\n{meeting_notes}"
    return ask_gpt(prompt, max_tokens=150)

