# from langchain.llms import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, SequentialChain
# import os
# from keys import openai_api_key

# os.environ['OPENAI_API_KEY'] = openai_api_key

# llm = OpenAI(temperature=0.7)

# def get_restaurants(cuisine):
#     # chain-1: restaurant name
#     prompt_template_name = PromptTemplate(
#         input_variables=['cuisine'],
#         template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this restaurant."
#     )

#     name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

#     # chain-2: menu items
#     prompt_template_items = PromptTemplate(
#         input_variables=['restaurant_name'],
#         template="Suggest a list of 10 items that would be under {restaurant_name}'s menu."
#     )

#     food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

#     # chain-3: restaurant name and menu items
#     chain = SequentialChain(
#         chains=[name_chain, food_items_chain],
#         input_variables=['cuisine'],
#         output_variables=['restaurant_name', 'menu_items'],
#         verbose=True
#     )

#     response = chain({'cuisine': cuisine})
#     return response

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, SequentialChain
# from keys import gemini_api_key
# import os

# os.environ["GOOGLE_API_KEY"] = gemini_api_key

# llm = ChatGoogleGenerativeAI(model="models/chat-bison", temperature=0.7)

# def get_restaurants(cuisine):
#     # Chain 1: Get Restaurant Name
#     prompt_template_name = PromptTemplate(
#         input_variables=["cuisine"],
#         template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this restaurant."
#     )
#     name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

#     # Chain 2: Generate Menu
#     prompt_template_items = PromptTemplate(
#         input_variables=["restaurant_name"],
#         template="Suggest a list of 10 delicious items that would be on the menu of a restaurant named {restaurant_name}."
#     )
#     food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

#     # Combine Chains
#     chain = SequentialChain(
#         chains=[name_chain, food_items_chain],
#         input_variables=["cuisine"],
#         output_variables=["restaurant_name", "menu_items"],
#         verbose=True
#     )

#     response = chain({"cuisine": cuisine})
#     return response

# import google.generativeai as genai
# from keys import gemini_api_key

# genai.configure(api_key=gemini_api_key)

# def get_restaurants(cuisine):
#     model = genai.GenerativeModel("gemini-pro")

#     name_prompt = f"I want to open a restaurant for {cuisine} food. Suggest a fancy name for this restaurant."
#     name_response = model.generate_content(name_prompt)
#     restaurant_name = name_response.text.strip()

#     menu_prompt = f"Suggest a list of 10 items that would be under {restaurant_name}'s menu."
#     menu_response = model.generate_content(menu_prompt)
#     menu_items = [item.strip(" -") for item in menu_response.text.strip().split('\n') if item.strip()]

#     return {
#         "restaurant_name": restaurant_name,
#         "menu_items": menu_items
#     }

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Get the key
gemini_api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

def get_restaurants(cuisine):
    model = genai.GenerativeModel("models/gemini-1.5-flash-8b-latest")

    # Step 1: Get restaurant name
    name_prompt = f"I want to open a restaurant for {cuisine} food. Suggest a fancy name for this restaurant."
    name_response = model.generate_content(name_prompt)
    restaurant_name = name_response.text.strip()

    # Step 2: Get menu items
    menu_prompt = f"Suggest a list of 10 items that would be under {restaurant_name}'s menu."
    menu_response = model.generate_content(menu_prompt)
    menu_items = [line.strip("•- ") for line in menu_response.text.strip().split('\n') if line.strip()]

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }
