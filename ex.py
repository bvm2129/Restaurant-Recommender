import google.generativeai as genai
genai.configure(api_key="GEMINI_API_KEY")
print(genai.list_models())
