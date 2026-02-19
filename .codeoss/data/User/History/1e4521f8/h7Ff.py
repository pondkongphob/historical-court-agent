from agents.inquiry_agent import inquiry_agent
from agents.admirer_agent import admirer_agent
from agents.critic_agent import critic_agent
from agents.judge_agent import judge_agent
from agents.verdict_agent import verdict_agent

state = {
    "topic": "",
    "pos_data": "",
    "neg_data": "",
    "loop_done": False
}

topic = "Genghis Khan"

inquiry_agent(topic, state)

admirer_agent(state)
critic_agent(state)

while not state["loop_done"]:
    result = judge_agent(state)

    if result == "positive":
        admirer_agent(state)

    elif result == "negative":
        critic_agent(state)

verdict_agent(state)

print("Report created!")
