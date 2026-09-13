import streamlit as st
from datetime import date

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Para vos ❤️",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# DATOS PARA PERSONALIZAR
# ============================================================

NOMBRE_NOVIA = "Mi amor"

# Cambiá esta fecha por el día que empezaron a estar juntos
FECHA_INICIO = date(2025, 1, 1)

# Preguntas de la trivia
TRIVIA = [
    {
        "pregunta": "¿Cuál fue nuestro primer plan juntos?",
        "opciones": [
            "Ir a comer",
            "Mirar una película",
            "Salir a caminar",
            "Quedarnos hablando horas"
        ],
        "correcta": "Quedarnos hablando horas"
    },
    {
        "pregunta": "¿Qué es algo que más me gusta de vos?",
        "opciones": [
            "Tu forma de ser",
            "Tu sonrisa",
            "Cómo me hacés reír",
            "Todo lo anterior"
        ],
        "correcta": "Todo lo anterior"
    },
    {
        "pregunta": "¿Qué prefiero hacer con vos?",
        "opciones": [
            "Salir",
            "Mirar películas",
            "Hablar durante horas",
            "Cualquier cosa, mientras sea con vos"
        ],
        "correcta": "Cualquier cosa, mientras sea con vos"
    }
]

# ============================================================
# ESTILOS
# ============================================================

st.markdown("""
<style>

    /* Fondo general */
    .stApp {
        background: linear-gradient(
            180deg,
            #fff0f5 0%,
            #ffe4ec 50%,
            #fff5f7 100%
        );
    }

    /* Contenedor principal */
    .main {
        max-width: 700px;
        padding: 20px;
    }

    /* Título */
    .titulo {
        text-align: center;
        color: #c2185b;
        font-size: 42px;
        font-weight: 800;
        margin-top: 15px;
        margin-bottom: 5px;
    }

    .subtitulo {
        text-align: center;
        color: #8e3658;
        font-size: 19px;
        margin-bottom: 25px;
    }

    /* Tarjetas */
    .tarjeta {
        background: rgba(255,255,255,0.85);
        border-radius: 22px;
        padding: 25px;
        margin: 18px 0;
        box-shadow: 0px 6px 20px rgba(194, 24, 91, 0.12);
        border: 1px solid rgba(194, 24, 91, 0.10);
    }

    .tarjeta h2 {
        color: #c2185b;
    }

    .mensaje {
        text-align: center;
        font-size: 21px;
        color: #6d2141;
        line-height: 1.6;
    }

    /* Contador */
    .contador {
        text-align: center;
        background: linear-gradient(135deg, #e91e63, #c2185b);
        color: white;
        border-radius: 25px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0px 8px 25px rgba(194,24,91,0.25);
    }

    .numero {
        font-size: 45px;
        font-weight: bold;
    }

    /* Carta */
    .carta {
        background: #fffaf0;
        border-radius: 15px;
        padding: 30px;
        margin-top: 20px;
        color: #4a3030;
        font-size: 18px;
        line-height: 1.8;
        box-shadow: 0px 5px 18px rgba(80,40,40,0.12);
        border: 1px solid #f2d7b5;
    }

    .firma {
        text-align: right;
        margin-top: 25px;
        font-weight: bold;
        color: #c2185b;
    }

    /* Corazones */
    .corazones {
        text-align: center;
        font-size: 27px;
        letter-spacing: 8px;
        margin: 15px 0;
    }

    /* Botones */
    .stButton > button {
        width: 100%;
        border-radius: 15px;
        min-height: 50px;
        font-size: 17px;
        font-weight: 600;
    }

    /* Ocultar menú y footer */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Mobile */
    @media (max-width: 600px) {

        .main {
            padding: 12px;
        }

        .titulo {
            font-size: 32px;
        }

        .subtitulo {
            font-size: 17px;
        }

        .tarjeta {
            padding: 20px;
        }

        .mensaje {
            font-size: 18px;
        }

        .numero {
            font-size: 38px;
        }

        .carta {
            padding: 22px;
            font-size: 17px;
        }
    }

</style>
""", unsafe_allow_html=True)

# ============================================================
# ESTADO DE LA APLICACIÓN
# ============================================================

if "inicio" not in st.session_state:
    st.session_state.inicio = False

if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0

if "puntos" not in st.session_state:
    st.session_state.puntos = 0

if "trivia_terminada" not in st.session_state:
    st.session_state.trivia_terminada = False

if "respuesta_final" not in st.session_state:
    st.session_state.respuesta_final = False

# ============================================================
# PORTADA
# ============================================================

st.markdown(
    '<div class="titulo">💌 Para vos</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="subtitulo">Una pequeña sorpresa para {NOMBRE_NOVIA} ❤️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="corazones">❤️ 💗 💕 💖 💘</div>',
    unsafe_allow_html=True
)

# ============================================================
# BOTÓN DE INICIO
# ============================================================

if not st.session_state.inicio:

    st.markdown("""
    <div class="tarjeta">
        <div class="mensaje">
            Preparé esto especialmente para vos.<br><br>
            No es una página cualquiera...<br>
            es un pequeño recorrido por algunas cosas
            que hacen especial nuestra historia. 💕
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💖 Abrir mi sorpresa"):

        st.session_state.inicio = True
        st.rerun()

    st.stop()

# ============================================================
# MENSAJE INICIAL
# ============================================================

st.markdown("""
<div class="tarjeta">

<h2>🌷 Primero quiero decirte algo</h2>

<div class="mensaje">

Gracias por cada momento, cada charla, cada risa
y cada recuerdo que fuimos creando juntos.

A veces no hace falta hacer algo enorme para que
un momento sea especial.

Muchas veces alcanza con estar con la persona correcta. ❤️

</div>

</div>
""", unsafe_allow_html=True)

# ============================================================
# CONTADOR DE DÍAS
# ============================================================

hoy = date.today()

dias_juntos = (hoy - FECHA_INICIO).days

st.markdown(f"""
<div class="contador">

<div>📅 Llevamos juntos</div>

<div class="numero">{dias_juntos}</div>

<div>días de nuestra historia ❤️</div>

</div>
""", unsafe_allow_html=True)

# ============================================================
# TRIVIA
# ============================================================

st.markdown("""
<div class="tarjeta">

<h2>🧠 Trivia de nuestra historia</h2>

<p>
Ahora viene una pequeña prueba...
A ver cuánto te acordás de nosotros 😌❤️
</p>

</div>
""", unsafe_allow_html=True)

if not st.session_state.trivia_terminada:

    pregunta_num = st.session_state.pregunta_actual
    pregunta = TRIVIA[pregunta_num]

    st.markdown(
        f"### Pregunta {pregunta_num + 1} de {len(TRIVIA)}"
    )

    respuesta = st.radio(
        pregunta["pregunta"],
        pregunta["opciones"],
        key=f"pregunta_{pregunta_num}"
    )

    if st.button("💗 Responder"):

        if respuesta == pregunta["correcta"]:
            st.session_state.puntos += 1
            st.success("¡Correcto! ❤️")
        else:
            st.info(
                f"La respuesta era: {pregunta['correcta']} 💕"
            )

        if pregunta_num + 1 < len(TRIVIA):
            st.session_state.pregunta_actual += 1
            st.rerun()
        else:
            st.session_state.trivia_terminada = True
            st.rerun()

else:

    puntos = st.session_state.puntos
    total = len(TRIVIA)

    st.markdown(f"""
    <div class="tarjeta">
        <div class="mensaje">
            🥰 Terminaste la trivia.<br><br>
            Tu resultado fue:
            <strong>{puntos}/{total}</strong>
            ❤️<br><br>
            Igual, la verdad es que no importa cuánto
            hayas acertado... lo importante es todo
            lo que vivimos juntos.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# PREGUNTA ESPECIAL
# ============================================================

st.markdown("""
<div class="tarjeta">

<h2>💞 Una pregunta importante</h2>

<div class="mensaje">

¿Querés seguir creando recuerdos conmigo?

</div>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("❤️ Sí"):
        st.session_state.respuesta_final = True
        st.balloons()

with col2:
    if st.button("🥺 No"):
        st.session_state.respuesta_final = True

if st.session_state.respuesta_final:

    st.markdown("""
    <div class="tarjeta">

    <div class="mensaje">

    Entonces seguimos sumando momentos,
    risas, charlas y recuerdos. ❤️

    <br><br>

    Y todavía quedan muchísimas cosas por vivir.

    </div>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# CARTA FINAL
# ============================================================

st.markdown("""
<div class="tarjeta">

<h2>💌 La carta final</h2>

</div>
""", unsafe_allow_html=True)

if st.button("🎁 Abrir la carta"):

    st.markdown(f"""
    <div class="carta">

    <h2>Para {NOMBRE_NOVIA} ❤️</h2>

    Quería hacerte algo diferente y por eso terminé
    haciendo esta pequeña página para vos.

    <br><br>

    No sé si existe una forma perfecta de explicar
    lo mucho que significás para mí, pero sí sé que
    me encanta compartir momentos con vos.

    <br><br>

    Gracias por las risas, por las conversaciones,
    por los momentos lindos y también por estar
    en los momentos que no son tan fáciles.

    <br><br>

    Espero que podamos seguir sumando recuerdos,
    haciendo planes y viviendo muchas cosas juntos.

    <br><br>

    Esta página puede terminar acá, pero nuestra
    historia todavía tiene muchísimas páginas por escribir.

    <div class="firma">
    Con mucho cariño ❤️<br>
    Tu novio
    </div>

    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FINAL
# ============================================================

st.markdown("""
<div class="corazones">
    💗 ❤️ 💕 💖 💗
</div>

<div style="text-align:center; color:#8e3658;">
    Fin de la sorpresa ✨
</div>
""", unsafe_allow_html=True)