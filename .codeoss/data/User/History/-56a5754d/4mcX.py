def verdict_agent(state):
    report = f"""
Topic: {state['topic']}

POSITIVE:
{state['pos_data']}

NEGATIVE:
{state['neg_data']}
"""

    with open("report.txt", "w") as f:
        f.write(report)
