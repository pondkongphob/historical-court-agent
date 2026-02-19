import wikipedia

def admirer_agent(state):
    topic = state["topic"]
    data = wikipedia.summary(topic, sentences=3)
    state["pos_data"] += data
