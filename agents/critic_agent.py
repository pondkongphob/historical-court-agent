def critic_agent(state):
    """
    Extract criticisms and controversies
    """

    text = state.get("wiki_text", "")

    if not text:
        state["neg_data"] += "No negative data found.\n"
        return

    negative_keywords = [
        "critic", "controversy", "war", "violence",
        "despot", "tyrant", "conflict", "killed"
    ]

    sentences = text.split(". ")

    negatives = [
        s for s in sentences
        if any(word in s.lower() for word in negative_keywords)
    ]

    state["neg_data"] += "\n".join(negatives[:5]) + "\n"
