import wikipedia

def critic_agent(state):
    topic = state["topic"]

    try:
        page = wikipedia.page(topic, auto_suggest=True)

        # เพิ่ม keyword controversy
        data = wikipedia.summary(page.title + " controversy", sentences=5)

        state["neg_data"] += data + "\n\n"

    except Exception as e:
        print("Critic error:", e)
