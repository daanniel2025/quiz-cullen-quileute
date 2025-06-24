import streamlit as st

st.title("Quiz: Você seria um Cullen ou um Quileute?")

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

respostas = {}

for i, p in enumerate(perguntas):
    respostas[i] = st.radio(p["texto"], options=list(p["opcoes"].keys()), format_func=lambda x: p["opcoes"][x])

if st.button("Ver Resultado"):
    total_cullen = sum(respostas[i] in ['A', 'C'] for i in respostas)
    total_quileute = sum(respostas[i] in ['B', 'D'] for i in respostas)

    if total_cullen > total_quileute:
        st.markdown("### 🧛 Você tem o perfil de um Cullen! Discreto, observador e com uma força interna poderosa.")
    else:
        st.markdown("### 🐺 Você se parece com um Quileute! Intenso, impulsivo e guiado por laços profundos com os outros.")
