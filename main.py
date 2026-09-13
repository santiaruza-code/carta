import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Para vos ❤️",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

NOMBRE_NOVIA = "Mi amor"

# Trivia personalizada
TRIVIA = [
    {
        "pregunta": "¿Cuál de estas palabras digo más? 🥺",
        "opciones": [
            "gordita",
            "te amo",
            "chichi",
            "sos hermosa"
        ],
        "correcta": "chichi"
    },
    {
        "pregunta": "¿Qué fue lo primero que hicimos cuando nos vimos?",
        "opciones": [
            "comer un dos corazones",
            "ir al cine agarrados de la mano",
            "ir a la ribera a dar vueltas",
            "tomar mates"
        ],
        "correcta": "ir al cine agarrados de la mano"
    },
    {
        "pregunta": "Sinceramente... ¿quién es el más caprichoso y consentido de los dos? 😜",
        "opciones": [
            "Vos, sin duda",
            "Yo (tu nene caprichoso)",
            "Los dos por igual cuando queremos mimos",
            "Ninguno, somos re serios"
        ],
        "correcta": "Yo (tu nene caprichoso)"
    },
    {
        "pregunta": "¿Qué es lo que NUNCA puede faltar cuando estamos juntos?",
        "opciones": [
            "estar abrazados",
            "besos",
            "hacer cosas q no son de dios",
            "todas son correctas"
        ],
        "correcta": "todas son correctas"
    },
    {
        "pregunta": "¿Qué es lo que más me gusta de vos?",
        "opciones": [
            "tus chichis",
            "tu orto",
            "q me cumplas los caprichos",
            "tus ojazos"
        ],
        "correcta": "tus ojazos"
    }
]

# ============================================================
# ESTILOS MODO OSCURO
# ============================================================

st.markdown("""
<style>
    .stApp {
        background-color: #0b0b0d !important;
    }

    .stApp p, .stApp label, .stMarkdown, h1, h2, h3, span {
        color: #ffffff !important;
    }

    .tarjeta {
        background: #16161a;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        border: 1px solid #ff2e63;
        box-shadow: 0px 4px 20px rgba(255, 46, 99, 0.2);
    }

    .tarjeta h2 {
        color: #ff2e63 !important;
        text-align: center;
    }

    .mensaje {
        text-align: center;
        font-size: 19px;
        color: #e0e0e0 !important;
        line-height: 1.6;
    }

    .titulo {
        text-align: center;
        color: #ff2e63 !important;
        font-size: 40px;
        font-weight: 800;
        margin-top: 10px;
    }

    .subtitulo {
        text-align: center;
        color: #ff85a2 !important;
        font-size: 18px;
        margin-bottom: 20px;
    }

    .corazones {
        text-align: center;
        font-size: 26px;
        letter-spacing: 8px;
        margin: 10px 0;
    }

    .carta {
        background: #1f1f24;
        border-radius: 15px;
        padding: 25px;
        margin-top: 15px;
        color: #f1f1f1 !important;
        font-size: 17px;
        line-height: 1.8;
        border: 1px solid #ff2e63;
    }

    .firma {
        text-align: right;
        margin-top: 20px;
        font-weight: bold;
        color: #ff2e63 !important;
    }

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        min-height: 48px;
        font-size: 16px;
        font-weight: bold;
        background-color: #ff2e63 !important;
        color: white !important;
        border: none !important;
    }

    #MainMenu, footer, header {
        visibility: hidden;
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

if "acepto" not in st.session_state:
    st.session_state.acepto = False

if "intentos_no" not in st.session_state:
    st.session_state.intentos_no = 0

# ============================================================
# PORTADA
# ============================================================

st.markdown('<div class="titulo">💌 Para vos</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitulo">Una pequeña sorpresa para {NOMBRE_NOVIA} ❤️</div>', unsafe_allow_html=True)
st.markdown('<div class="corazones">❤️ 💗 💕 💖 💘</div>', unsafe_allow_html=True)

# ============================================================
# BOTÓN DE INICIO
# ============================================================

if not st.session_state.inicio:
    st.markdown("""
    <div class="tarjeta">
        <div class="mensaje">
            Preparé esto especialmente para vos.<br><br>
            No es una página cualquiera...<br>
            es un pequeño recorrido por nuestra historia. 💕
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
        y cada recuerdo que fuimos creando juntos.<br><br>
        A veces no hace falta hacer algo enorme para que
        un momento sea especial. Alcanza con estar con la persona correcta. ❤️
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CONTADOR EN VIVO (21 de Junio de 2026)
# ============================================================

st.markdown('<div class="tarjeta"><h2>⏳ Tiempo de nuestra historia</h2></div>', unsafe_allow_html=True)

reloj_html = """
<div id="contador" style="
    text-align: center;
    background: linear-gradient(135deg, #ff2e63, #c2185b);
    color: white;
    border-radius: 20px;
    padding: 20px;
    font-family: sans-serif;
    box-shadow: 0px 4px 15px rgba(255,46,99,0.3);
">
    <div style="font-size: 16px; margin-bottom: 8px;">Llevamos juntos exactos:</div>
    <div id="tiempo" style="font-size: 26px; font-weight: bold; letter-spacing: 1px;">Cargando...</div>
    <div style="font-size: 16px; margin-top: 8px;">❤️</div>
</div>

<script>
    const fechaInicio = new Date("2026-06-21T00:00:00").getTime();

    function actualizarContador() {
        const ahora = new Date().getTime();
        const diferencia = ahora - fechaInicio;

        if (diferencia < 0) {
            document.getElementById("tiempo").innerHTML = "¡Falta muy poco!";
            return;
        }

        const dias = Math.floor(diferencia / (1000 * 60 * 60 * 24));
        const horas = Math.floor((diferencia % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutos = Math.floor((diferencia % (1000 * 60 * 60)) / (1000 * 60));
        const segundos = Math.floor((diferencia % (1000 * 60)) / 1000);

        document.getElementById("tiempo").innerHTML = 
            dias + "d " + horas + "h " + minutos + "m " + segundos + "s";
    }

    setInterval(actualizarContador, 1000);
    actualizarContador();
</script>
"""
components.html(reloj_html, height=140)

# ============================================================
# TRIVIA
# ============================================================

st.markdown('<div class="tarjeta"><h2>🧠 Trivia de nuestra historia</h2><p style="text-align:center;">A ver cuánto te acordás de nosotros 😌❤️</p></div>', unsafe_allow_html=True)

if not st.session_state.trivia_terminada:
    pregunta_num = st.session_state.pregunta_actual
    pregunta = TRIVIA[pregunta_num]

    st.markdown(f"### Pregunta {pregunta_num + 1} de {len(TRIVIA)}")
    respuesta = st.radio(pregunta["pregunta"], pregunta["opciones"], key=f"pregunta_{pregunta_num}")

    if st.button("💗 Responder"):
        if respuesta == pregunta["correcta"]:
            st.session_state.puntos += 1
            st.success("¡Correcto! ❤️")
        else:
            st.info(f"La respuesta era: {pregunta['correcta']} 💕")

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
            🥰 ¡Terminaste la trivia!<br><br>
            Tu resultado fue: <strong>{puntos}/{total}</strong> ❤️<br><br>
            Igual, lo importante no es el puntaje sino todo lo que vivimos juntos.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# PREGUNTA ESPECIAL CON BOTÓN ESCAPISTA
# ============================================================

st.markdown("""
<div class="tarjeta">
    <h2>💞 Una pregunta importante</h2>
    <div class="mensaje">¿Querés seguir creando recuerdos conmigo?</div>
</div>
""", unsafe_allow_html=True)

if not st.session_state.acepto:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("❤️ ¡SÍ!"):
            st.session_state.acepto = True
            st.balloons()
            st.rerun()

    with col2:
        textos_no = [
            "🥺 No",
            "¿Segura? 😜",
            "¡Ey, esa opción no vale!",
            "Epa... apretá el SÍ 😂",
            "Imposible decir que no 💖"
        ]
        texto_boton_no = textos_no[min(st.session_state.intentos_no, len(textos_no)-1)]

        if st.button(texto_boton_no):
            st.session_state.intentos_no += 1
            st.rerun()
else:
    st.markdown("""
    <div class="tarjeta">
        <div class="mensaje">
            ¡Sabía que ibas a decir que sí! 😍<br>
            Seguimos sumando momentos, risas y recuerdos juntos. ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# CARTA FINAL CON CONTRASEÑA
# ============================================================

st.markdown("""
<div class="tarjeta">
    <h2>🔒 La carta secreta</h2>
    <p style="text-align:center;">Para leer la carta necesitás ingresar la clave secreta.</p>
</div>
""", unsafe_allow_html=True)

clave_ingresada = st.text_input("🔑 Ingresá la contraseña:", type="password", help="Pista: Una palabra que digo mucho 😉")

if clave_ingresada.lower().strip() == "chichi":
    st.success("¡Contraseña correcta! ❤️")
    st.markdown(f"""
    <div class="carta">
        <h2>Para {NOMBRE_NOVIA} ❤️</h2>
        Quería hacerte algo diferente y por eso terminé haciendo esta pequeña página para vos.<br><br>
        No sé si existe una forma perfecta de explicar lo mucho que significás para mí, pero sí sé que me encanta compartir cada día con vos.<br><br>
        Gracias por las risas, por las conversaciones, por los momentos lindos y también por estar en los momentos que no son tan fáciles.<br><br>
        Espero que podamos seguir sumando recuerdos, haciendo planes y viviendo muchas cosas juntos.<br><br>
        Esta página puede terminar acá, pero nuestra historia todavía tiene muchísimas páginas por escribir.
        <div class="firma">
            Con mucho cariño ❤️<br>
            Tu nene caprichoso
        </div>
    </div>
    """, unsafe_allow_html=True)
elif clave_ingresada != "":
    st.error("Contraseña incorrecta... Pensá en una palabra que te diga muy seguido 😜")

# ============================================================
# FINAL
# ============================================================

st.markdown('<div class="corazones">💗 ❤️ 💕 💖 💗</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; color:#ff85a2;">Fin de la sorpresa ✨</div>', unsafe_allow_html=True)
