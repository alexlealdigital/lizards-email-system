# Sistema de Envio de Emails - Lizards Games

## Descrição
Solução Python Flask para envio de emails através do formulário de contato do site da Lizards Games. O sistema substitui o formulário Netlify original por um backend Python que utiliza SMTP do Zoho Mail para enviar emails para gameslizards@gmail.com.

## Características
- ✅ Backend Flask com CORS configurado
- ✅ Envio de emails via SMTP Zoho Mail
- ✅ Formulário HTML responsivo mantido intacto
- ✅ Validação de dados do formulário
- ✅ Feedback visual para o usuário
- ✅ Tratamento de erros

## Estrutura do Projeto
```
lizards-email-system/
├── email-backend/
│   ├── src/
│   │   ├── main.py              # Aplicação principal Flask
│   │   ├── routes/
│   │   │   ├── email.py         # Rota para envio de emails
│   │   │   └── user.py          # Rotas de usuário (padrão)
│   │   ├── static/
│   │   │   └── index.html       # Site da Lizards Games modificado
│   │   └── models/              # Modelos de banco (não utilizados)
│   ├── venv/                    # Ambiente virtual Python
│   └── requirements.txt         # Dependências Python
├── index.html                   # Arquivo HTML original
├── mail.txt                     # Configurações de email
└── README.md                    # Esta documentação
```

## Configurações de Email
- **Servidor SMTP:** smtp.zoho.com
- **Porta:** 587
- **Email Remetente:** lab.leal.jornal@zohomail.com
- **Email Destinatário:** gameslizards@gmail.com
- **Senha:** Chat2025$

## Como Executar Localmente

### 1. Navegar para o diretório do backend
```bash
cd email-backend
```

### 2. Ativar o ambiente virtual
```bash
source venv/bin/activate
```

### 3. Instalar dependências (se necessário)
```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação
```bash
python src/main.py
```

### 5. Acessar no navegador
```
http://localhost:5000
```

## API Endpoints

### POST /api/send-email
Endpoint para envio de emails através do formulário.

**Parâmetros (JSON):**
- `name` (string, obrigatório): Nome do remetente
- `email` (string, obrigatório): Email do remetente
- `subject` (string, opcional): Assunto da mensagem
- `message` (string, obrigatório): Conteúdo da mensagem

**Resposta de Sucesso:**
```json
{
    "success": true,
    "message": "Email enviado com sucesso!"
}
```

**Resposta de Erro:**
```json
{
    "success": false,
    "message": "Mensagem de erro"
}
```

## Modificações Realizadas

### 1. Formulário HTML
- Removido atributo `netlify` do formulário original
- Adicionado ID `contact-form` para JavaScript
- Implementado JavaScript para envio via AJAX
- Adicionado feedback visual com mensagens de sucesso/erro

### 2. Backend Flask
- Criada rota `/api/send-email` para processar formulário
- Configurado CORS para permitir requisições do frontend
- Implementada validação de dados obrigatórios
- Configurado envio de email via SMTP

### 3. Segurança
- Validação de dados de entrada
- Tratamento de erros SMTP
- Headers CORS configurados adequadamente

## Deploy em Produção

### Opção 1: Render.com (Recomendado)
1. Fazer upload do diretório `email-backend` para um repositório Git
2. Conectar o repositório ao Render.com
3. Configurar as variáveis de ambiente:
   - `EMAIL_SENDER=lab.leal.jornal@zohomail.com`
   - `EMAIL_PASSWORD=Chat2025$`
   - `EMAIL_RECIPIENT=gameslizards@gmail.com`

### Opção 2: Heroku
1. Instalar Heroku CLI
2. Fazer login: `heroku login`
3. Criar app: `heroku create lizards-email-system`
4. Configurar variáveis: `heroku config:set EMAIL_SENDER=...`
5. Deploy: `git push heroku main`

### Opção 3: VPS/Servidor Próprio
1. Instalar Python 3.11+
2. Copiar arquivos do projeto
3. Instalar dependências: `pip install -r requirements.txt`
4. Configurar servidor web (nginx + gunicorn)
5. Configurar SSL/HTTPS

## Teste da Solução
✅ **Formulário testado com sucesso!**
- Preenchimento de todos os campos funcionando
- Envio de email realizado com sucesso
- Feedback visual funcionando corretamente
- Responsividade mantida em dispositivos móveis

## Suporte
Para dúvidas ou problemas, entre em contato com a equipe de desenvolvimento.

---
**Desenvolvido para Lizards Games**
Data: Junho 2025
