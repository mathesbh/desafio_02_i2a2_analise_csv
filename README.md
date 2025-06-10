# Projeto: Processador de Notas Fiscais (.zip com CSVs)

Este projeto em Python tem como objetivo ler um arquivo `.zip` contendo dois arquivos CSV com dados de notas fiscais, descompactar, processar e enviar essas informações para uma API REST (mock).

---

## Estrutura do Projeto

```
nfs_projeto/
├── .venv/                      # Ambiente virtual Python (recomendado)
├── dados_extraidos/            # Diretório onde os CSVs são extraídos
├── 202401_NFs.zip              # Arquivo .zip com os CSVs (cabeçalho e itens)
├── main.py                     # Arquivo principal que roda o processo
├── leitor_zip.py               # Classe que processa os dados do .zip e monta os objetos
├── integrador_api.py           # Classe que envia os dados para a API REST
├── db.json                     # Base de dados usada pelo json-server (API mock em JS)
├── requirements.txt            # Dependências Python
└── README.md                   # Documentação do projeto
```

---

## Requisitos Python

* Python 3.10+
* pip
* Ambiente virtual (opcional, mas recomendado)

### Instalar dependências:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Como executar o projeto

Com o ambiente ativo e os arquivos preparados:

```bash
python main.py
```

Isso fará:

1. A leitura do arquivo `.zip`
2. A extração dos dois arquivos `.csv`
3. A montagem dos dados em objetos Python
4. O envio dos dados para uma API REST

---

## Mock da API REST

### ✅ Simples com `json-server` (JavaScript)

#### 1. Instale o json-server

```bash
npm install -g json-server
```

#### 2. Crie um arquivo `db.json` com:

```json
{
  "notas": []
}
```

#### 3. Rode o mock:

```bash
json-server --watch db.json --port 8000
```

A API estará disponível em `http://localhost:8000/notas`

## 📌 Observações

* Os arquivos CSV devem seguir a estrutura de cabeçalho e itens com coluna comum `chave_de_acesso`
* Os dados são convertidos para objetos e enviados em JSON para a API

---