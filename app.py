from flask import Flask
from routes.user_routes import user_bp
from routes.tema_route import tema_bp
from routes.quiz_route import quiz_bp
from routes.pergunta_route import question_bp
from routes.alternativa_route import answer_bp

# Inicia o Flask
app = Flask(__name__)

# Registra as rotas que criamos no outro arquivo
app.register_blueprint(user_bp)
app.register_blueprint(tema_bp)
app.register_blueprint(quiz_bp)
app.register_blueprint(question_bp)
app.register_blueprint(answer_bp)

# Rota de boas vindas só para testar se o servidor tá on
@app.route('/', methods=['GET'])
def home():
    return "Bem-vindo à API do meu Jogo!"

# Liga o servidor
if __name__ == '__main__':
    print("🚀 Servidor rodando na porta 5000...")
    app.run(debug=True)