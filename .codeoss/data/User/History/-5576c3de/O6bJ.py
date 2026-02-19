import wikipedia

def critic_agent(state):
    topic = state["topic"]

    results = wikipedia.search(topic + " controversy")

    if results:
        try:
            data = wikipedia.summary(results[0], sentences=3)
            state["neg_data"] += data
        except:
            state["neg_data"] += "No negative data found."
