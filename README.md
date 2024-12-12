# 🎬 Sistema de Gerenciamento de Cinema

## Descrição
Sistema web para gerenciar filmes, atores, categorias, plataformas, ingressos e avaliações. O projeto foi desenvolvido utilizando o framework Django, implementando operações de CRUD completas, autenticação de usuários e uma interface estilizada.

---

## 🎯 Funcionalidades
- Gerenciamento de Filmes, Atores, Categorias, Plataformas, Ingressos e Avaliações.
- Autenticação de usuários (Login, Logout e Registro).
- Controle de acesso para páginas sensíveis.
- Interface responsiva e estilizada com HTML, CSS e JavaScript.

---

## 🚀 Tecnologias Utilizadas
- **Framework**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Banco de Dados**: SQLite (padrão do Django)
- **Autenticação**: Sistema de autenticação nativo do Django

---

## 📂 Estrutura do Projeto
```bash

├── nucleo/
│   ├── migrations/
│   ├── static/
│   │   ├── css/styles.css
│   │   ├── js/scripts.js
│   └── templates/
│       ├── base.html
│       ├── auth/
│       │   ├── login.html
│       │   ├── register.html
│       ├── filme/
│       ├── ator/
│       ├── categoria/
│       ├── plataforma/
│       ├── ingresso/
│       └── avaliacao/
├── cinema_projeto/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── manage.py
└── requirements.txt
```

---

## 🛠️ Como Configurar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Niconfisk/DW-Django-gp.git
   cd DW-Django-gp
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Realize as migrações do banco de dados:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

5. Acesse o sistema em [http://localhost:8000](http://localhost:8000).

---

## 👥 Equipe
- **Nicolas Tavares**
- **João Victor**
- **Gabrielle Feitosa**
- **Pedro Lucas**