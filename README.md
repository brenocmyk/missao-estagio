# Envio de mensagens no WhatsApp

Script Python que lê contatos do Supabase e dispara mensagens via Z-API.

## Setup

Crie a tabela 'contacts' no Supabase pelo SQL Editor:

```sql
create table contacts (
  id       int,
  nome     text,
  telefone text
);
```

> **Atenção:** o telefone precisa estar no formato internacional sem '+', ex: '5521999999999' caso contrário a Z-API não envia!!

## Variáveis de ambiente

Crie um arquivo '.env' na raiz do projeto:

```env
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE=
ZAPI_TOKEN=
```

> Você encontra essas infos no dashboard do Supabase e abrindo qualquer instância web no Z-API.

## Instalação

```
pip install -r requirements.txt
```

## Executar

```
python main.py
```
