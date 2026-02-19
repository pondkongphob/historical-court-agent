import wikipedia

def admirer_agent(state):
    topic = state["topic"]

    try:
        page = wikipedia.page(topic, auto_suggest=True)
        data = wikipedia.summary(page.title, sentences=5)
        state["pos_data"] += data
    except:
        state["pos_data"] += "No positive data found."
