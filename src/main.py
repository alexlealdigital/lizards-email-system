import os
from flask import Flask, jsonify
from flask_cors import CORS
from routes.email import email_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Configurar CORS para permitir requisições apenas do Netlify
CORS(app, origins=['https://lzgamestech.netlify.app'])

# Registrar blueprint de email
app.register_blueprint(email_bp, url_prefix='/api')

@app.route('/')
def index():
    return jsonify({
        "message": "Lizards Games Email Service", 
        "status": "running",
        "version": "1.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)

