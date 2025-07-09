# import streamlit as st
# import langchain_helper

# st.title("🍽️ Restaurant Name Recommender")
# cuisine = st.sidebar.selectbox("Pick a cuisine", ("Italian", "Mexican", "Indian", "Japanese", "American"))

# if cuisine:
#     response = langchain_helper.get_restaurants(cuisine)
#     st.header("🏷️ Name: " + response['restaurant_name'].strip())

#     menu = response['menu_items'].split('\n')
#     st.write("📜 **Menu**")
#     col1, col2 = st.columns(2)

#     for i, item in enumerate(menu):
#         if i % 2 == 0:
#             with col1:
#                 st.write("🍴", item)
#         else:
#             with col2:
#                 st.write("🍴", item)

import streamlit as st
import langchain_helper

st.title("🍽️ Restaurant Name Recommender")
# (Powered by Gemini ✨)
cuisine = st.sidebar.selectbox("Pick a cuisine", ("Italian", "Mexican", "Indian", "Japanese", "American"))

if cuisine:
    response = langchain_helper.get_restaurants(cuisine)
    st.header("🏷️" + response['restaurant_name'].replace('_', ' '))

    st.write("📜 **Menu**")
    menu_items = response['menu_items']
    # col1, col2 = st.columns(2)
    # for i, item in enumerate(menu_items):
    #     if i % 2 == 0:
    #         with col1:
    #             st.write("🍴", item)
    #     else:
    #         with col2:
    #             st.write("🍴", item)
    if len(menu_items) > 10:
        for item in range(10):
            st.write("🍴", menu_items[item + 1])
    else:
        for item in range(len(menu_items)):
            st.write("🍴", menu_items[item + 1])
