from supabase import create_client
import os
from dotenv import load_dotenv
from zapi import enviar_msg
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

response = (
    supabase
    .table("contacts")
    .select("*")
    .execute()
)

for contato in response.data:
    nome = contato["nome"]
    telefone = contato["telefone"]
    mensagem = f"Olá, {nome} tudo bem com você?"
    try:
        resultado = enviar_msg(
            telefone,
            mensagem
        )
        print(
            f"Mensagem enviada para {nome}:",
            resultado
        )
    except Exception as erro:
        print(
            f"Erro ao enviar para {nome}:",
            erro
        )
    