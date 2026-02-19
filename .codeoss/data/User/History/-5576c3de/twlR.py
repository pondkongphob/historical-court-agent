import wikipedia

def critic_agent(state):
    topic = state["topic"]
    data = wikipedia.summary(topic + " controversy", sentences=3)
    state["neg_data"] += data
