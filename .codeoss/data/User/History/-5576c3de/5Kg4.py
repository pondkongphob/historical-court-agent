def critic_agent(state):
    text = state.get("wiki_text", "")

    if not text:
        state["neg_data"] += "No negative data found."
        return

    # เอาช่วงท้ายเป็นมุมลบ
    state["neg_data"] += text[-500:]
