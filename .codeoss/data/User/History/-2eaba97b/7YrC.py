import wikipedia

wikipedia.set_lang("en")

def inquiry_agent(topic, state):
    state["topic"] = topic

    try:
        # 🔹 Step 1: search ก่อน
        results = wikipedia.search(topic)

        if not results:
            print("No Wikipedia results found")
            return

        # 🔹 Step 2: ใช้ผลลัพธ์ตัวแรก
        page = wikipedia.page(results[0])

        state["wiki_text"] = page.content

    except Exception as e:
        print("Inquiry error:", e)
        state["wiki_text"] = ""
