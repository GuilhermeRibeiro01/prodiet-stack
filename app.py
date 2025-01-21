import streamlit as st
import requests
import base64
import os

ENDPOINT_URL = "https://w6ij5jby9b.execute-api.us-east-1.amazonaws.com"

st.title("Upload de documento")

# product_id = st.selectbox("Tipo de seguro", ["Vida", "Automóvel"])
# caloric = st.selectbox("Calorias", ["normocalorica", "hipercalorica"])
# age = st.selectbox("Idade", ["adulto", "criança"])
# unid = st.selectbox("Unidade", ["litro", "grama", "mililitro"])
# document_type = st.selectbox("Tipo de Documento", ["txt","pdf"])

arquivo = st.file_uploader("Escolha um arquivo", type=['pdf'])

if arquivo:
    nome_arquivo = os.path.basename(arquivo.name)
    st.write("Nome do arquivo:", nome_arquivo)

    if st.button("Enviar"):
        # Dados para a requisição da URL assinada
        dados_requisicao = {
            "object_key": nome_arquivo,  # Adicionar object_key aqui
            "documentType": "pdf"
        }

        # 1. Obter URL assinada da API (incluindo metadados na requisição)
        url_assinada_resposta = requests.post(
            ENDPOINT_URL + "/edital", json=dados_requisicao 
        )

        if url_assinada_resposta.status_code == 200:
            url_assinada = url_assinada_resposta.json().get("uploadURL")
            print(url_assinada)

            headers = {'Content-Type': 'text/plain'}
            
            upload_resposta = requests.put(url_assinada, data=arquivo, headers=headers)

            if upload_resposta.status_code == 200:
                st.success("Arquivo enviado com sucesso!")
            else:
                st.error(f"Erro ao enviar arquivo: {upload_resposta.text}")
        else:
            st.error(f"Erro ao obter URL assinada: {url_assinada_resposta.text}")


            
WEBHOOK_URL = "https://webhook.site/a6053780-221d-4a61-94ed-dcbf37c6d7d2"
st.page_link(WEBHOOK_URL, label="WEBHOOK")
