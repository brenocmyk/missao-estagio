# Missao Estágio - Envio de mensagens no WhatsApp.

Projeto desenvolvido em Python usando Supabase e Z-API.

## Setup

Crie a tabela contacts no Supabase, vá no sql editor e cole:

sql
create table contacts (
  id        int,
  nome      text,
  telefone  text
);

Atençao: na hora de add o telefone, ele precisa estar no formato internacional sem "+", ex: "5521999999999", se não o z-api NÃO envia.

## Variáveis de ambiente

Crie um arquivo .env com essas informaçoes:

SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE=
ZAPI_TOKEN=

(Você pega essas infos pelo dashboard do supabase e abrindo qualquer instancia web no z-api)

## Instalação

pip install -r requirements.txt

## Executar

python main.py