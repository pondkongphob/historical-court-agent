import wikipedia

def admirer_agent(state):
    topic = state["topic"]

    try:
        # ใช้ page() ตรง ๆ (ไม่ต้อง search)
        page = wikipedia.page(topic, auto_suggest=True)

        data = wikipedia.summary(page.title, sentences=5)

        state["pos_data"] += data + "\n\n"

    except Exception as e:
        print("Admirer error:", e)
