# 📂 Sistema de Gestão de Documentos

Aplicação web desenvolvida com **Flask (Python)** para envio, visualização e gerenciamento de documentos com histórico de comentários vinculados a cada arquivo.

🔗 **Deploy:** https://gestao-de-documentos-t1ig.onrender.com

---

## 🚀 Funcionalidades

-  Upload de documentos  
-  Cadastro de título e descrição  
-  Visualização de documentos enviados  
-  Histórico de comentários por documento  
-  Registro automático de data e hora  

---

## 🛠️ Tecnologias Utilizadas

- Python 3  
- Flask
- SQLite
- Gunicorn  
- HTML5  
- CSS3  
- JavaScript  
- Render (Deploy)  

---
## 🗄️ Banco de Dados

A aplicação utiliza **SQLite** como banco de dados relacional.

O banco é criado automaticamente na primeira execução do projeto.

### 📄 Tabela: `documentos`

| Campo        | Tipo     | Descrição |
|-------------|----------|-----------|
| id          | INTEGER  | Chave primária (PK) |
| titulo      | TEXT     | Título do documento |
| descricao   | TEXT     | Descrição opcional |
| nome_arquivo| TEXT     | Nome do arquivo salvo |
| data        | TEXT     | Data e hora do envio |

---
### 💬 Tabela: `comentarios`

| Campo          | Tipo     | Descrição |
|---------------|----------|-----------|
| id            | INTEGER  | Chave primária (PK) |
| texto         | TEXT     | Conteúdo do comentário |
| data          | TEXT     | Data e hora do comentário |
| documento_id  | INTEGER  | Chave estrangeira (FK) |

---

## 📁 Estrutura do Projeto

gestao-de-documentos/  
│  
├── app.py  
├── database.db  
├── requirements.txt  
├── Procfile  
│  
├── templates/  
│   └── index.html  
│  
├── static/  
│   ├── style.css  
│   └── script.js  
│  
└── uploads/  

---

## ⚙️ Como Executar Localmente

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/iicaroll/Gestao-de-documentos.git
cd SEU-REPOSITORIO
````
### 2️⃣ (Opcional) Crie um ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```
### 3️⃣ Instale as dependências
``` bash
pip install -r requirements.txt
```
### 4️⃣ Execute o projeto
``` bash
python app.py
````
A aplicação estará disponível em:
http://127.0.0.1:5000

## ☁️ Deploy no Render
Configuração utilizada:

Build Command:
```bash
pip install -r requirements.txt
```
Start Command:
```bash
gunicorn app:app
```

# Regras Implementadas
## Documentos
Cada documento possui:
- ID único
- Título (obrigatório)
- Descrição (opcional)
- Nome do arquivo
- Data e hora de envio
- Lista de comentários vinculados

## Comentários
Cada comentário:
- Está vinculado corretamente ao respectivo documento
- Contém texto
- Registra automaticamente data e hora
- É exibido no histórico do documento correspondente

## ⚠️ Observações Técnicas
- Os dados estão armazenados em memória (lista Python).
- Caso o servidor reinicie, os dados são resetados.
- Para produção real, recomenda-se integração com banco de dados (SQLite ou PostgreSQL).

## 🎯 Objetivo do Projeto
- Demonstrar conhecimentos em:
- Desenvolvimento backend com Flask
- Manipulação de arquivos
- Estruturação de rotas
- Organização e estilização de interface
- Deploy em ambiente cloud

## 👩‍💻 Desenvolvido por
Ana Caroline Dantas


