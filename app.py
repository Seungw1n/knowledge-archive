import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Prompt")
    selected_size = st.selectbox("Size", ["1024 x 1024", "512 x 512", "256 x 256"] ,index=0)
    submit_button = st.form_submit_button(label="Submit")

if submit_button and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the ditail appeareance of the input. Response it shortly around 20 words."
    }]
    
    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })
    
    with st.spinner("Waiting for chatGPT"):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)
    
    with st.spinner("Wating for DALL-E..."):
        dalle_response = openai.Image.create(
            prompt = prompt,
            size = selected_size
        )
    
    
    st.image(dalle_response["data"][0]["url"])
        
