def admirer_agent(state):
    """
    Extract positive achievements from Wikipedia text
    """

    text = state.get("wiki_text", "")

    if not text:
        state["pos_data"] += "No positive data found.\n"
        return

    positive_keywords = [
        "founded", "united", "success", "achievement",
        "expanded", "improved", "leader", "innovative"
    ]

    sentences = text.split(". ")

    positives = [
        s for s in sentences
        if any(word in s.lower() for word in positive_keywords)
    ]

    state["pos_data"] += "\n".join(positives[:5]) + "\n"
