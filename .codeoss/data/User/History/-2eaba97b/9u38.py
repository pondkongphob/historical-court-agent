import wikipedia

wikipedia.set_lang("en")

def inquiry_agent(topic, state):
    state["topic"] = topic

    try:
        # ใช้ page ตรง ๆ ไม่ต้อง search
        page = wikipedia.page(topic, auto_suggest=True)

        state["wiki_text"] = page.content

        print("✅ Inquiry SUCCESS")
        print("Loaded text length:", len(state["wiki_text"]))

    except Exception as e:
        print("❌ Inquiry error:", e)
        state["wiki_text"] = ""
