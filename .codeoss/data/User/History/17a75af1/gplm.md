# Historical Court Multi-Agent System

## 📌 Project Description

This project is a Multi-Agent System that analyzes historical figures using Wikipedia data.

The system works like a "historical courtroom" by collecting both positive and negative perspectives before generating a final report.

---

## ⚙️ Agents in the System

The system contains 5 agents:

1. Inquiry Agent  
   - Gets data from Wikipedia

2. Admirer Agent  
   - Finds positive achievements

3. Critic Agent  
   - Finds negative aspects and controversies

4. Judge Agent  
   - Checks if both sides have enough data
   - Loops until balanced

5. Verdict Agent  
   - Generates final report file

---

## 🧠 State Variables

The system uses a shared state dictionary:

- topic → historical subject
- wiki_text → Wikipedia content
- pos_data → positive information
- neg_data → negative information
- loop_done → loop control flag

---

## ▶️ How to Run

1. Install library:

2. Run program:

3. Output will be saved as:

---

## 📊 Example Topic

Tested with:
Genghis Khan

The system successfully produced balanced historical analysis.

---

## 🎯 Learning Outcome

This project demonstrates:

- Multi-Agent Architecture
- Parallel processing
- Loop decision logic
- State management
