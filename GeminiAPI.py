from google import genai

client = genai.Client(api_key="AIzaSyA-nAttBmcx__qJtdt1lpLacg2SNmoIIsY")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how opec works in a few words"
)
print(response.text)