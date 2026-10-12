
import streamlit as st
from openai import OpenAI
import openai

st.title("Multi-model Chat")
st.write("HAMKI Assignment #13")
st.write("Chat with different AI models")

st.subheader("Model selection")

model = st.selectbox(
    "Select AI model",
    ["gpt-4o-mini", "gpt-4o"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


prompt = st.chat_input("Write your message here")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)


    try:
        client = OpenAI()

        with st.spinner("AI is thinking..."):
            response = client.responses.create(
                model=model,
                input=st.session_state.messages
            )
        answer = response.output_text

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

          
        with st.chat_message("assistant"):
            st.write(answer)

    except openai.APIError as error:
        st.error(f"API error: {error}")




