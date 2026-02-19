import wikipedia

def critic_agent(state):
    topic = state["topic"]

    try:
        page = wikipedia.page(topic, auto_suggest=True)
        data = wikipedia.summary(page.title + " controversy", sentences=5)
        state["neg_data"] += data
    except:
        state["neg_data"] += "No negative data found."
