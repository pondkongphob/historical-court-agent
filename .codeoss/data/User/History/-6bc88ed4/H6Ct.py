def admirer_agent(state):
    text = state.get("wiki_text", "")

    if not text:
        state["pos_data"] += "No positive data found."
        return

    # เอาแค่ 500 ตัวแรกเป็นมุมบวก
    state["pos_data"] += text[:500]
