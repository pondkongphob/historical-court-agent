import wikipedia

# ตั้งภาษาเป็น English
wikipedia.set_lang("en")

def critic_agent(state):
    topic = state["topic"]

    try:
        page = wikipedia.page(topic)
        data = wikipedia.summary(page.title, sentences=5)
        state["neg_data"] += data
    except Exception as e:
        state["neg_data"] += "No negative data found."
