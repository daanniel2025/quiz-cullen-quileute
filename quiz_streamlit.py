import streamlit as st

st.title("Você seria um Vampiro ou um Lobo?")

st.markdown("""
Você já se perguntou de que lado da história estaria?  
Será que você se encaixa mais no mundo misterioso dos vampiros Cullen ou no espírito livre e protetor dos lobisomens Quileute?  
Descubra agora respondendo este quiz divertido!
""")

perguntas = [
    {
        "texto": "1. Qual ambiente você prefere?",
        "opcoes": {
            "A": "Um lugar frio e nublado, cercado por florestas",
            "B": "Uma praia ensolarada com o som do mar ao fundo",
            "C": "Um campo aberto com montanhas ao redor",
            "D": "Uma biblioteca silenciosa em qualquer lugar do mundo"
        }
    },
    {
        "texto": "2. Como você reage a um problema difícil?",
        "opcoes": {
            "A": "Penso bem antes de agir, buscando uma solução lógica",
            "B": "Sigo meus instintos, mesmo que cometa erros",
            "C": "Converso com pessoas próximas para buscar apoio",
            "D": "Me isolo por um tempo até encontrar equilíbrio"
        }
    },
    {
        "texto": "3. Qual dessas qualidades combina mais com você?",
        "opcoes": {
            "A": "Autocontrole e paciência",
            "B": "Lealdade e coragem",
            "C": "Empatia e sensibilidade",
            "D": "Paixão e intensidade"
        }
    },
    {
        "texto": "4. Como seria seu estilo de vida ideal?",
        "opcoes": {
            "A": "Um lugar tranquilo e refinado, longe do caos",
            "B": "Uma vida em grupo, em conexão com a natureza",
            "C": "Aventuras constantes, sem rotina",
            "D": "Um lar aconchegante com quem eu amo"
        }
    },
    {
        "texto": "5. Que superpoder você escolheria?",
        "opcoes": {
            "A": "Ler pensamentos",
            "B": "Se transformar em um animal",
            "C": "Curar rapidamente ou ser imortal",
            "D": "Ser superveloz e forte"
        }
    }
]

# Função para calcular resultado
def calcular_resultado(respostas):
    total_cullen = sum(r in ['A', 'C'] for r in respostas.values())
    total_quileute = sum(r in ['B', 'D'] for r in respostas.values())
    if total_cullen > total_quileute:
        return "cullen"
    elif total_quileute > total_cullen:
        return "quileute"
    else:
        return "empate"

# Inicializar session_state para respostas
if 'respostas' not in st.session_state:
    st.session_state['respostas'] = {}

# Exibir perguntas e salvar respostas no session_state
for i, p in enumerate(perguntas):
    st.session_state['respostas'][i] = st.radio(
        p["texto"], 
        options=list(p["opcoes"].keys()), 
        format_func=lambda x, p=p: p["opcoes"][x],  # evita late binding
        key=f"pergunta_{i}"
    )

# Botão para calcular resultado
if st.button("Ver Resultado"):
    respostas = st.session_state['respostas']

    # Verificar se todas as perguntas foram respondidas
    if None in respostas.values() or len(respostas) < len(perguntas):
        st.warning("Por favor, responda todas as perguntas antes de ver o resultado.")
    else:
        resultado = calcular_resultado(respostas)
        if resultado == "cullen":
            st.markdown("### 🧛 Você tem o perfil de um Vampiro! Discreto, observador e com uma força interna poderosa.")
            st.image("https://recreio.com.br/wp-content/uploads/filmes/crepusculo_edward_capa.jpg", caption="Edward Cullen")
        elif resultado == "quileute":
            st.markdown("### 🐺 Você se parece com um Lobo! Intenso, impulsivo e guiado por laços profundos com os outros.")
            st.image("https://preview.redd.it/0homd9i7h7r91.jpg?auto=webp&s=933591cf94b4427a903bddbb4bf4c8afe585eb49", caption="Quileute")
        else:
            st.markdown("### 🤝 Resultado equilibrado! Você tem características dos dois lados.")
