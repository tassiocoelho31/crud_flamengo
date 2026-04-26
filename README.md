# 🔴⚫ Projeto CRUD - Flamengo

Projeto desenvolvido para praticar os fundamentos de **CRUD** (Create, Read, Update, Delete) utilizando Python, com evolução progressiva desde armazenamento em memória até banco de dados SQLite.

---

## 📁 Estrutura do Projeto

```
Projeto CRUD - Flamengo/
├── CRUD - Jogos/
│   ├── jogos.py          # CRUD em memória
│   ├── jogos_json.py     # CRUD com persistência em JSON
│   └── jogos_db.py       # CRUD com banco de dados SQLite
│
└── CRUD - Jogadores/
    └── jogadores_db.py   # CRUD com banco de dados SQLite
```

---

## 🚀 Funcionalidades

### CRUD - Jogos
Gerenciamento de jogos do Flamengo com os campos:
- Data do jogo
- Adversário
- Placar
- Competição
- Local (casa/fora)

### CRUD - Jogadores
Gerenciamento de jogadores do elenco com os campos:
- Nome
- Data de nascimento
- Clube anterior
- Convocações para a seleção
- Idade
- Data de contrato

Ambos os projetos possuem as operações:
- ✅ **Cadastrar**
- ✅ **Listar**
- ✅ **Atualizar**
- ✅ **Deletar**

---

## 📈 Evolução do Projeto

| Versão | Armazenamento | Arquivo |
|--------|--------------|---------|
| v1 | Memória (lista Python) | `jogos.py` |
| v2 | Arquivo JSON | `jogos_json.py` |
| v3 | Banco de dados SQLite | `jogos_db.py` / `jogadores_db.py` |

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **SQLite3** (embutido no Python)
- **JSON** (embutido no Python)

---

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/tassiocoelho31/crud_flamengo.git
```

2. Acesse a pasta do projeto desejado e execute:
```bash
python jogadores_db.py
```
ou
```bash
python jogos_db.py
```

> Nenhuma instalação de dependências externas necessária!

---

## 👨‍💻 Autor

**Tássio Marcel Hoffmann Coelho**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tássio-coelho/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tassiodev31@gmail.com)

---

> *Projeto desenvolvido durante o curso de Análise e Desenvolvimento de Sistemas, com foco em aprendizado prático de estruturas de dados e banco de dados com Python.* 🔴⚫
