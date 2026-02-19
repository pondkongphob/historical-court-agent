def verdict_agent(state):
    """
    Generate final report file
    """

    report = f"""
=========================================
        HISTORICAL COURT REPORT
=========================================

Topic: {state['topic']}

---------------- POSITIVE ----------------
{state['pos_data']}

---------------- NEGATIVE ----------------
{state['neg_data']}

=========================================
Verdict:
This report presents a balanced view based on
historical sources from Wikipedia.
=========================================
"""

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("📄 Report saved to report.txt")
