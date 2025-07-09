import google.generativeai as genai
genai.configure(api_key="***REMOVED***")
print(genai.list_models())
