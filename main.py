from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)


response = (
    supabase
    .table("contacts")
    .select("*")
    .limit(3)
    .execute()
)

contacts = response.data

for contato in contacts:
    print(contato["nome"], contato["telefone"])