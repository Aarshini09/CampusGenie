def summarize_text(text):
    return f"Summary: {text[:100]}..."

def explain_topic(topic):
    return f"Explanation of {topic}: This is a dummy explanation for now."

def extract_deadlines(text):
    return [
        {
            "task": "CS101 Assignment",
            "deadline": "Tomorrow 11:59 PM",
            "priority": "High"
        }
    ]
