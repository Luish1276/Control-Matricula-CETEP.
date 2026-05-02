import streamlit as st
import pandas as pd
from datetime import datetime
import os

# =========================
# CONFIGURACIÓN GENERAL
# =========================

st.set_page_config(
    page_title="CETEP | Campus Virtual",
    layout="wide",
    page_icon="🎓"
)

ARCHIVO_ESTUDIANTES = "estudiantes.csv"

ADMIN_USER = "admin_cetep"
ADMIN_PASSWORD = "Luis2026"

# =========================
# ESTILOS
# =========================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.hero-full {
    background: linear-gradient(rgba(0,30,60,0.88), rgba(0,30,60,0.95)),
                url('https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1920');
    background-size: cover;
    background-position: center;
    padding: 90px 25px;
    color: white;
    text-align: center;
    border-radius: 0px 0px 45px 45px;
    margin: -60px -20px 40px -20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.25);
}

.price-badge {
    background: #ffcc00;
    color: #002d5a;
    padding: 15px 30px;
    border-radius: 15px;
    font-weight: 800;
    font-size: 28px;
    display: inline-block;
    margin: 20px 0;
    border: 2px solid #fff;
}

.course-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.10);
    margin-bottom: 20px;
    border-left: 8px solid #002d5a;
}

.bloque-header {
    background: #002d5a;
    color: #ffcc00;
    padding: 12px 20px;
    border-radius: 10px 10px 0 0;
    font-weight: 700;
    margin-top: 20px;
}

.temario-box {
    background: #fdfdfd;
    padding: 20px;
    border: 1px solid #eee;
    border-radius: 0 0 10px 10px;
    margin-bottom: 10px;
}

.tema-line {
    padding: 8px 0;
    border-bottom: 1px solid #eef0f2;
    font-size: 15px;
    color: #333;
}

.metric-card {
    background: #ffffff;
    border-top: 5px solid #002d5a;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =========================
# OFERTA ACADÉMICA
# =========================

OFFER_ACADEMICA = {
    "Global Learning: English Mastery": {
        "duracion": "24 meses",
        "modalidad": "Virtual autodirigido",
        "matricula": 5000,
        "mensualidad": 15000,
        "descripcion": "Programa progresivo para desarrollar dominio del idioma inglés desde nivel básico hasta avanzado.",
        "malla": {
            "Año 1: Cimentación": [
                "Fonética correcta",
                "Gramática en uso",
                "Conversación inicial"
            ],
            "Año 2: Perfeccionamiento": [
                "Business English",
                "Negociación",
                "Dominio C1"
            ]
        }
    },
    "Técnico en Operaciones Bancarias": {
        "duracion": "6 meses",
        "modalidad": "Virtual autodirigido",
        "matricula": 5000,
        "mensualidad": 15000,
        "descripcion": "Formación técnica orientada a labores bancarias, caja, cumplimiento y operación financiera.",
        "malla": {
            "Módulo I: Marco Legal": [
                "Legislación bancaria costarricense",
                "Ley 8204: prevención de legitimación de capitales",
                "Ética bancaria"
            ],
            "Módulo II: Operativa Bancaria": [
                "Detección de billetaje falso",
                "Arqueos y cuadres de caja",
                "Seguridad bancaria"
            ],
            "Global Learning": [
                "Inglés técnico bancario integrado"
            ]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "duracion": "9 meses",
        "modalidad": "Virtual autodirigido",
        "matricula": 5000,
        "mensualidad": 15000,
        "descripcion": "Programa técnico para apoyar procesos contables, administrativos y financieros.",
        "malla": {
            "Contabilidad": [
                "Ciclo contable completo",
                "IVA y renta en Costa Rica",
                "Conciliaciones bancarias"
            ],
            "Gestión Administrativa": [
                "Planillas CCSS e INS",
                "Facturación electrónica",
                "Excel financiero"
            ],
            "Global Learning": [
                "Inglés para negocios integrado"
            ]
        }
    },
    "Gestión de Operaciones e Industria Médica": {
        "duracion": "9 meses",
        "modalidad": "Virtual autodirigido",
        "matricula": 5000,
        "mensualidad": 15000,
        "descripcion": "Formación técnica para ambientes de manufactura médica, calidad y operaciones.",
        "malla": {
            "Calidad": [
                "ISO 13485:2016",
                "Buenas prácticas de documentación",
                "Validación QMS"
            ],
            "Manufactura": [
                "Protocolos de cuarto limpio",
                "Metrología",
                "Lectura de planos"
            ],
            "Global Learning": [
                "Inglés industrial médico integrado"
            ]
        }
    },
    "Preparación Examen Excelencia Académica para Abogados": {
        "duracion": "Intensivo virtual",
        "modalidad": "Virtual autodirigido",
        "matricula": 5000,
        "mensualidad": 15000,
        "descripcion": "Programa de preparación para profesionales en Derecho orientado a repaso, análisis y simulacros.",
        "malla": {
            "Áreas Jurídicas": [
                "Civil y mercantil",
                "Público y laboral",
                "Notarial y deontología"
            ],
            "Práctica": [
                "Análisis de votos",
                "Simulacros de examen",
                "Técnica de respuesta"
            ]
        }
    }
}

CURSOS_VIDEOS = {
    "Técnico en Operaciones Bancarias": [
        {
            "modulo": "Módulo 1: Ley 8204",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
    ],
    "Asistente Contable y Gestión Administrativa": [
        {
            "modulo": "Módulo 1: IVA y Renta",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
    ],
    "Gestión de Operaciones e Industria Médica": [
        {
            "modulo": "Módulo 1: ISO 13485",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
    ]
}

# =========================
# FUNCIONES
# =========================

def cargar_estudiantes():
    if os.path.exists(ARCHIVO_ESTUDIANTES):
        return pd.read_csv(ARCHIVO_ESTUDIANTES)
    else:
        return pd.DataFrame(columns=[
            "Fecha",
            "Nombre",
            "Cedula",
            "Telefono",
            "Correo",
            "Curso",
            "Estado",
            "Matricula",
            "Mensualidad"
        ])

def guardar_estudiante(nombre, cedula, telefono, correo, curso):
    estudiantes = cargar_estudiantes()

    nuevo = pd.DataFrame([{
        "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "Nombre": nombre,
        "Cedula": cedula,
        "Telefono": telefono,
        "Correo": correo,
        "Curso": curso,
        "Estado": "Pendiente de contacto",
        "Matricula": OFFER_ACADEMICA[curso]["matricula"],
        "Mensualidad": OFFER_ACADEMICA[curso]["mensualidad"]
    }])

    estudiantes = pd.concat([estudiantes, nuevo], ignore_index=True)
    estudiantes.to_csv(ARCHIVO_ESTUDIANTES, index=False)

def formato_colones(monto):
    return f"₡{monto:,.0f}".replace(",", ".")

# =========================
# MENÚ LATERAL
# =========================

with st.sidebar:
    st.markdown("## 🎓 CETEP 2026")
    nav = st.radio(
        "MENÚ",
        [
            "🏠 Inicio",
            "📚 Programas",
            "📝 Matrícula",
            "💻 Campus Estudiante",
            "🔐 Panel Director"
        ]
    )

# =========================
# INICIO
# =========================

if nav == "🏠 Inicio":
    st.markdown("""
    <div class="hero-full">
        <h1>FORMACIÓN TÉCNICA PROFESIONAL</h1>
        <p>Programas virtuales autodirigidos para impulsar tu futuro laboral.</p>
        <div class="price-badge">₡15.000 MENSUALES</div>
        <p>Matrícula única: ₡5.000</p>
    </div>
    """, unsafe_allow_html=True)

    st.header("¿Por qué estudiar en CETEP?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="course-card">
            <h3>💻 Modalidad virtual</h3>
            <p>Estudiá desde cualquier lugar, a tu ritmo y con acceso a contenidos digitales.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="course-card">
            <h3>💰 Precio accesible</h3>
            <p>Programas diseñados para facilitar el acceso a educación técnica profesional.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="course-card">
            <h3>🎯 Enfoque laboral</h3>
            <p>Contenidos orientados a habilidades prácticas para el mercado de trabajo.</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("Para iniciar, ingresá en la sección de Matrícula y completá tus datos.")

# =========================
# PROGRAMAS
# =========================

elif nav == "📚 Programas":
    st.title("📚 Programas disponibles")

    curso = st.selectbox("Seleccione un programa:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[curso]

    st.markdown(f"""
    <div class="course-card">
        <h2>{curso}</h2>
        <p>{info["descripcion"]}</p>
        <p><strong>Duración:</strong> {info["duracion"]}</p>
        <p><strong>Modalidad:</strong> {info["modalidad"]}</p>
        <p><strong>Matrícula:</strong> {formato_colones(info["matricula"])}</p>
        <p><strong>Mensualidad:</strong> {formato_colones(info["mensualidad"])}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Malla académica")

    for bloque, temas in info["malla"].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div><div class='temario-box'>", unsafe_allow_html=True)

        for tema in temas:
            st.markdown(f"<div class='tema-line'>✅ {tema}</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# =========================
# MATRÍCULA
# =========================

elif nav == "📝 Matrícula":
    st.title("📝 Formulario de matrícula")

    st.info("Complete los datos del estudiante. La matrícula quedará registrada para contacto y seguimiento.")

    with st.form("form_matricula"):
        nombre = st.text_input("Nombre completo")
        cedula = st.text_input("Cédula")
        telefono = st.text_input("Teléfono / WhatsApp")
        correo = st.text_input("Correo electrónico")
        curso = st.selectbox("Curso de interés", list(OFFER_ACADEMICA.keys()))

        aceptar = st.checkbox("Declaro que deseo ser contactado para finalizar el proceso de matrícula.")

        enviar = st.form_submit_button("Enviar matrícula")

        if enviar:
            if not nombre or not cedula or not telefono or not correo:
                st.error("Por favor complete todos los campos obligatorios.")
            elif not aceptar:
                st.warning("Debe aceptar ser contactado para continuar.")
            else:
                guardar_estudiante(nombre, cedula, telefono, correo, curso)
                st.success("✅ Matrícula registrada correctamente. CETEP podrá contactarle para finalizar el proceso.")

# =========================
# CAMPUS ESTUDIANTE
# =========================

elif nav == "💻 Campus Estudiante":
    st.title("💻 Campus Estudiante")

    st.warning("Esta sección es una versión inicial del campus virtual.")

    curso = st.selectbox("Seleccione su curso:", list(CURSOS_VIDEOS.keys()))
    modulo = st.selectbox("Seleccione el módulo:", [x["modulo"] for x in CURSOS_VIDEOS[curso]])

    video_url = next(item for item in CURSOS_VIDEOS[curso] if item["modulo"] == modulo)["url"]

    st.subheader(modulo)
    st.video(video_url)

# =========================
# PANEL DIRECTOR
# =========================

elif nav == "🔐 Panel Director":
    st.title("🔐 Panel Director")

    if "auth" not in st.session_state:
        st.session_state.auth = False

    if not st.session_state.auth:
        usuario = st.text_input("Usuario")
        clave = st.text_input("Clave", type="password")

        if st.button("Ingresar"):
            if usuario == ADMIN_USER and clave == ADMIN_PASSWORD:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Usuario o clave incorrectos.")

    else:
        st.success("Sesión iniciada como Director.")

        estudiantes = cargar_estudiantes()
        cantidad = len(estudiantes)

        total_matriculas = estudiantes["Matricula"].sum() if cantidad > 0 else 0
        total_mensualidades = estudiantes["Mensualidad"].sum() if cantidad > 0 else 0

        c1, c2, c3 = st.columns(3)

        c1.markdown(f"""
        <div class='metric-card'>
            <h4>Estudiantes registrados</h4>
            <h2>{cantidad}</h2>
        </div>
        """, unsafe_allow_html=True)

        c2.markdown(f"""
        <div class='metric-card'>
            <h4>Total matrículas</h4>
            <h2>{formato_colones(total_matriculas)}</h2>
        </div>
        """, unsafe_allow_html=True)

        c3.markdown(f"""
        <div class='metric-card'>
            <h4>Mensualidades proyectadas</h4>
            <h2>{formato_colones(total_mensualidades)}</h2>
        </div>
        """, unsafe_allow_html=True)

        st.write("### Lista de estudiantes")

        if cantidad > 0:
            st.dataframe(estudiantes, use_container_width=True)

            csv = estudiantes.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Descargar estudiantes en CSV",
                data=csv,
                file_name="estudiantes_cetep.csv",
                mime="text/csv"
            )
        else:
            st.info("Aún no hay estudiantes registrados.")

        if st.button("Cerrar sesión"):
            st.session_state.auth = False
            st.rerun()

# =========================
# PIE DE PÁGINA
# =========================

st.markdown(
    "<center style='color:#888; margin-top:50px;'>© 2026 CETEP | Costa Rica</center>",
    unsafe_allow_html=True
)
