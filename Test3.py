import feedparser
import ollama
import schedule
import time
from datetime import datetime

# 1. ฟังก์ชันดึงข่าว IT (ตัวอย่างใช้ RSS ของ TechCrunch)
def fetch_it_news():
    print("[Agent] กำลังดึงข่าว IT ล่าสุด...")
    rss_url = "https://feeds.feedburner.com/TechCrunch/"
    feed = feedparser.parse(rss_url)
    
    news_items = []
    # เอาแค่ 3 ข่าวล่าสุด
    for entry in feed.entries[:3]:
        news_items.append(f"Title: {entry.title}\nSummary: {entry.summary}")
    
    return "\n\n".join(news_items)

# 2. ฟังก์ชันใช้ Ollama สรุปข่าว
def summarize_news(news_text):
    print("[Agent] กำลังส่งให้ Ollama (Llama 3) สรุปและแปลเป็นภาษาไทย...")
    
    # กำหนด System Prompt ให้ AI ทำตัวเป็นนักข่าว IT
    prompt = f"""
    คุณคือนักข่าว IT มืออาชีพ หน้าที่ของคุณคืออ่านข่าวภาษาอังกฤษด้านล่างนี้ 
    แล้วสรุปเป็นภาษาไทยให้กระชับ อ่านง่าย และน่าติดตาม เรียงลำดับเป็นข้อๆ:
    
    {news_text}
    """
    
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ])
    return response['message']['content']

# 3. ฟังก์ชันหลักในการรัน Agent
def job_daily_news():
    print(f"\n=== เริ่มทำงาน: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    
    # Step A: ดึงข้อมูล (Perception)
    raw_news = fetch_it_news()
    
    if not raw_news:
        print("ไม่พบข่าวใหม่")
        return

    # Step B: ประมวลผลและตัดสินใจ (Cognition)
    summary = summarize_news(raw_news)
    
    # Step C: ลงมือทำ (Action) - ในที่นี้คือพิมพ์ออกมา
    print("\n📰 สรุปข่าว IT ประจำวัน 📰")
    print("-" * 30)
    print(summary)
    print("-" * 30)
    print("ส่งข่าวเรียบร้อย!\n")

# ทดลองรันแบบทันที 1 ครั้ง (ลบ comment ออกหากต้องการเทสทันที)
# job_daily_news()

# 4. ตั้งเวลาทำงานทุกวัน (ตัวอย่าง: เวลา 08:00 น.)
print("🤖 เริ่มเดินระบบ Agentic AI ตั้งเวลารันทุกวันตอน 08:00 น. ...")
schedule.every().day.at("20:50").do(job_daily_news)

while True:
    schedule.run_pending()
    time.sleep(60) # เช็คเวลาทุกๆ 1 นาที