import wikipedia

def admirer_agent(state):
    topic = state["topic"]

    results = wikipedia.search(topic + " biography")

    if results:
        try:
            data = wikipedia.summary(results[0], sentences=5)
            state["pos_data"] += data
        except:
            state["pos_data"] += "No positive data found."
