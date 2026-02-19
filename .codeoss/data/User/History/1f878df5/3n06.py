def judge_agent(state):
    if len(state["pos_data"]) < 200:
        return "positive"

    if len(state["neg_data"]) < 200:
        return "negative"

    state["loop_done"] = True
    return "done"
