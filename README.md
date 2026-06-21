# Missao Estágio - Envio de mensagens no WhatsApp.

Projeto desenvolvido em Python usando Supabase e Z-API.

## Setup

Criar tabela contacts no Supabase:

| id | int |
| nome | text |
| telefone | text |

Atençao: o telefone precisa estar no formato internacional sem "+", ex: "5521999999999"

## Variáveis de ambiente

Criar um arquivo .env:

SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE=
ZAPI_TOKEN=

(Você pega essas infos pelo dashboard do supabase e abrindo qualquer instancia no z-api)

## Instalação

pip install -r requirements.txt

## Executar

python main.py