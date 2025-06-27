from flask import Blueprint, request, jsonify
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_bp = Blueprint('email', __name__)

@email_bp.route('/send-email', methods=['POST', 'OPTIONS'])
def send_email():
    # Permitir CORS preflight
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', 'https://lzgamestech.netlify.app')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response
    
    try:
        # Obter dados do formulário
        data = request.get_json() if request.is_json else request.form
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        # Validação básica
        if not all([name, email, message]):
            response = jsonify({
                'success': False, 
                'message': 'Nome, email e mensagem são obrigatórios.'
            })
            response.headers.add('Access-Control-Allow-Origin', 'https://lzgamestech.netlify.app')
            return response, 400
        
        # Configurações de email usando variáveis de ambiente
        smtp_server = "smtp.zoho.com"
        smtp_port = 587
        email_sender = os.environ.get('EMAIL_SENDER', 'lab.leal.jornal@zohomail.com')
        email_password = os.environ.get('EMAIL_PASSWORD', 'Chat2025$')
        email_recipient = os.environ.get('EMAIL_RECIPIENT', 'gameslizards@gmail.com')
        
        # Criar mensagem de email
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_recipient
        msg['Subject'] = f"Contato do site - {subject if subject else 'Sem assunto'}"
        
        # Corpo do email
        email_body = f"""Nova mensagem recebida através do formulário de contato do site:

Nome: {name}
Email: {email}
Assunto: {subject if subject else 'Não informado'}

Mensagem:
{message}

---
Esta mensagem foi enviada automaticamente através do formulário de contato do site da Lizards Games."""
        
        msg.attach(MIMEText(email_body, 'plain', 'utf-8'))
        
        # Enviar email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_sender, email_password)
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        server.quit()
        
        response = jsonify({
            'success': True, 
            'message': 'Email enviado com sucesso!'
        })
        response.headers.add('Access-Control-Allow-Origin', 'https://lzgamestech.netlify.app')
        return response
        
    except Exception as e:
        print(f"Erro ao enviar email: {str(e)}")
        response = jsonify({
            'success': False, 
            'message': 'Erro interno do servidor. Tente novamente mais tarde.'
        })
        response.headers.add('Access-Control-Allow-Origin', 'https://lzgamestech.netlify.app')
        return response, 500

