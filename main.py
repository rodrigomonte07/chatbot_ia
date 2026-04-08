import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="#########################")

st.write("# Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Escreva sua mensagem")
# arquivo = st.file_uploader() - Se quiser incluir envio de arquivos

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content":texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    
    resposta_ia = modelo_ia.chat.completions.create(
        messages= st.session_state["lista_mensagens"],
        model="gpt-5.4"
    )

    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)





