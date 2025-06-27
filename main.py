import os
import sys

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Importar a aplicação Flask
from src.main import app

if __name__ == '__main__':
    # Para desenvolvimento local
    app.run(host='0.0.0.0', port=5000, debug=True)
else:
    # Para produção (Render, Heroku, etc.)
    application = app

