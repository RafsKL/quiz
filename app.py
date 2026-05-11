from flask import Flask
from routes.user_routes import user_bp
from routes.tema_route import tema_bp
from routes.quiz_route import quiz_bp
from routes.pergunta_route import question_bp
from routes.alternativa_route import answer_bp
from routes.tentativa_route import tentativa_bp
from routes.respostas_route import respostas_bp
from routes.sala_route import sala_bp
from routes.ranking_route import ranking_bp

# Inicia o Flask
app = Flask(__name__)

# Registra as rotas que criamos no outro arquivo
app.register_blueprint(user_bp)
app.register_blueprint(tema_bp)
app.register_blueprint(quiz_bp)
app.register_blueprint(question_bp)
app.register_blueprint(answer_bp)
app.register_blueprint(tentativa_bp)
app.register_blueprint(respostas_bp)
app.register_blueprint(sala_bp)
app.register_blueprint(ranking_bp)

# Rota de boas vindas só para testar se o servidor tá on
@app.route('/', methods=['GET'])
def home():
    return "Bem-vindo à API do meu Jogo!"

# Liga o servidor
if __name__ == '__main__':
    print("🚀 Servidor rodando na porta 5000...")
    app.run(debug=True)