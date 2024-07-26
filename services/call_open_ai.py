from openai import OpenAI
import streamlit as st


def call_open_ai(city_name, num_days):

    client = OpenAI(
        api_key=st.secrets['OPEN_AI']['APIKEY']

    )

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", 
         "content": "You are a helping in planning the vacation. Give me day by day and hour by hour schedule by including major tourist attractions and make it kid friendly. Start at 9 am and give schedule till 7pm. No late nights."},
        {"role": "user", 
         "content": f"For city {city_name} plan holiday for {num_days} days"}
    ]
    
    )
    
    st.write(response.choices[0].message.content)