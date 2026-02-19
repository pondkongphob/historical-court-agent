import wikipedia

# ตั้งภาษาเป็น English
wikipedia.set_lang("en")

def admirer_agent(state):
    topic = state["topic"]

    try:
        page = wikipedia.page(topic)
        data = wikipedia.summary(page.title, sentences=5)
        state["pos_data"] += data
    except Exception as e:
        state["pos_data"] += "No positive data found."
