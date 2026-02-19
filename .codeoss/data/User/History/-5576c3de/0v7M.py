def judge_agent(state):
    """
    Judge checks balance between positive and negative data
    """

    pos_len = len(state["pos_data"])
    neg_len = len(state["neg_data"])

    print("Judge checking balance...")

    if pos_len < 300:
        print("⚖️ Need more positive data")
        return "positive"

    elif neg_len < 300:
        print("⚖️ Need more negative data")
        return "negative"

    else:
        print("⚖️ Data balanced")
        state["loop_done"] = True
        return "done"
