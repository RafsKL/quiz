from utils.json_db import read_data, write_data
from models.resposta_model import RespostaModel
import uuid

RESPOSTA_FILE = 'data/respostas.json'
ANSWER_FILE = 'data/alternativas.json'
TENTATIVA_FILE = 'data/tentativas.json'

class RespostasController:
    @staticmethod
    def salvar_resposta(dados):
        tentativa_id = dados.get("tentativa_id")
        pergunta_id = dados.get("pergunta_id")
        alternativa_id = dados.get("alternativa_id")

        # 1. Carrega as alternativas do JSON para conferir a correta
        alternativas = read_data(ANSWER_FILE)
        alternativa = next((a for a in alternativas if a["id"] == alternativa_id), None)
        
        if not alternativa:
            return {"erro": "Alternativa não encontrada no sistema!"}, 404

        e_correta = alternativa.get("correta", False)

        # 2. Registra a resposta no arquivo respostas.json
        respostas = read_data(RESPOSTA_FILE)
        nova_resposta = RespostaModel.criar_molde_resposta(
            tentativa_id, pergunta_id, alternativa_id, e_correta
        )
        respostas.append(nova_resposta)
        write_data(RESPOSTA_FILE, respostas)

        # 3. Se estiver correta, soma 10 pontos na TENTATIVA ativa lá no JSON
        if e_correta:
            tentativas = read_data(TENTATIVA_FILE)
            for t in tentativas:
                if t["id"] == tentativa_id:
                    # Garante que pontuacao exista e soma 10
                    t["pontuacao"] = t.get("pontuacao", 0) + 10
                    break
            write_data(TENTATIVA_FILE, tentativas)

        return {
            "correta": e_correta,
            "mensagem": "Resposta registrada!",
            "pontos_ganhos": 10 if e_correta else 0
        }, 201