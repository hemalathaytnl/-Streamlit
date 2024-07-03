#  Streamlit python framework


"""""

It looks like you are setting up a virtual environment for your Streamlit application. 
Here are the steps with the corresponding commands to create a virtual environment, activate it, and install Streamlit:


1.Create a virtual environment:
                                
                 python -m venv startapp

2.Activate the virtual environment:
                
                 .\startapp\Scripts\activate

 3.Install Streamlit 
                                     
                                             
                 pip install streamlit

4.Run your Streamlit app:
               
                streamlit run app.py

This will start a local Streamlit server, and you can open your web browser to the provided URL (usually http://localhost:8501) to see and interact with your calculator app.



Create your Streamlit app:
o	Create a new Python file, e.g., app.py.
o	Write your Streamlit code in app.py.


"""""


# Example Chatbot openAI Project


from openai import OpenAI
import streamlit as st


 openai_api_key=st.text_input("OpenAI API Key",key="chatbot_api_key",type="password")


with st.sidebar:
    openai_api_key=st.text_input("OpenAI API Key",key="chatbot_api_key",type="password")

st.title("✨ Chatbot")

st.caption("🚀 A Streamlit chatbot done by Vani")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI key to continue.")
        st.stop()
    client = OpenAI(api_key=openai_api_key)

    st.session_state.messages.append({"role" : "user", "content" : prompt})

    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(model="gpt-3.5-turbo",messages=st.session_state.messages)

    msg=response.choices[0].message.content

    st.session_state.messages.append({"role":"assistant","Session":msg})
    
    st.chat_message("assistant").write(msg)  
