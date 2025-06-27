# 🦎 Lizards Games - Backend Email Service

Sistema de envio de emails para o formulário de contato do site da Lizards Games.

## 🚀 Deploy no Render.com

### **Configurações:**
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn --bind 0.0.0.0:$PORT main:app`

### **Variáveis de Ambiente:**
```
EMAIL_SENDER=lab.leal.jornal@zohomail.com
EMAIL_PASSWORD=Chat2025$
EMAIL_RECIPIENT=gameslizards@gmail.com
```

## 📁 Estrutura do Projeto

```
├── src/
│   ├── main.py              # Aplicação Flask principal
│   └── routes/
│       └── email.py         # Rota de envio de emails
├── main.py                  # Entry point para Render
├── requirements.txt         # Dependências Python
├── build.sh                 # Script de build
└── .gitignore              # Arquivos a ignorar
```

## 🔧 Endpoints

### **GET /**
Retorna status do serviço
```json
{
  "message": "Lizards Games Email Service",
  "status": "running",
  "version": "1.0"
}
```

### **POST /api/send-email**
Envia email do formulário de contato
```json
{
  "name": "Nome do usuário",
  "email": "email@exemplo.com",
  "subject": "Assunto (opcional)",
  "message": "Mensagem do usuário"
}
```

## ✅ Teste Local

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar
python main.py
```

Acesse: http://localhost:5000

## 🌐 Produção

- **URL:** https://lizards-mail-service.onrender.com
- **Frontend:** https://lzgamestech.netlify.app
- **CORS:** Configurado apenas para o domínio do Netlify

---
**🎯 Backend limpo e otimizado para produção!**

