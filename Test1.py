from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType

# 1. กำหนด LLM ที่ต้องการใช้ (ชี้ไปที่ Ollama ในเครื่อง)
llm = ChatOllama(model="llama3.2", temperature=0)

# 2. กำหนดเครื่องมือ (Tool) ให้ Agent ใช้
search_tool = DuckDuckGoSearchRun()
tools = [
    search_tool
    # ในอนาคตสามารถเพิ่มฟังก์ชันอื่นๆ ได้ที่นี่ เช่น เครื่องมืออ่านไฟล์, คำนวณเลข
]

# 3. สร้าง Agent โดยเชื่อม LLM เข้ากับเครื่องมือ
agent = initialize_agent(
    tools=tools, 
    llm=llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, # ให้โมเดลคิดและตัดสินใจเองว่าจะใช้เครื่องมือไหม
    verbose=True # เปิดให้แสดงขั้นตอนการคิดของ Agent
)

# 4. สั่งงาน Agent
question = "สรุปข่าวล่าสุดเกี่ยวกับเทคโนโลยี Windows on ARM ให้หน่อย"
print(f"คำถาม: {question}\n")

response = agent.invoke(question)
print("\n--- สรุปผล ---")
print(response['output'])