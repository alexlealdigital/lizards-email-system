from flask import Blueprint, request, jsonify
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_bp = Blueprint('email', __name__)

# Configurações de email do arquivo mail.txt
SMTP_SERVER = "smtp.zoho.com"
SMTP_PORT = 587
EMAIL_SENDER = "lab.leal.jornal@zohomail.com"
EMAIL_PASSWORD = "Chat2025$"
EMAIL_RECIPIENT = "gameslizards@gmail.com"

@email_bp.route('/send-email', methods=['POST', 'OPTIONS'])
def send_email():
    # Permitir CORS
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
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
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 400
        
        # Criar mensagem de email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECIPIENT
        msg['Subject'] = f"Contato do site - {subject if subject else 'Sem assunto'}"
        
        # Corpo do email
        email_body = f"""
        Nova mensagem recebida através do formulário de contato do site:
        
        Nome: {name}
        Email: {email}
        Assunto: {subject if subject else 'Não informado'}
        
        Mensagem:
        {message}
        
        ---
        Esta mensagem foi enviada automaticamente através do formulário de contato do site da Lizards Games.
        """
        
        msg.attach(MIMEText(email_body, 'plain', 'utf-8'))
        
        # Enviar email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, text)
        server.quit()
        
        response = jsonify({
            'success': True, 
            'message': 'Email enviado com sucesso!'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        
    except Exception as e:
        print(f"Erro ao enviar email: {str(e)}")
        response = jsonify({
            'success': False, 
            'message': 'Erro interno do servidor. Tente novamente mais tarde.'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 500

