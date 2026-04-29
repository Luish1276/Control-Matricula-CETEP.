import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN E IDENTIDAD VISUAL DE ALTO NIVEL
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.85), rgba(0,30,60,0.95)), 
                    url('https://images.unsplash.com/photo-1501504905252-473c47e087f8?auto=format&fit=crop&q=80&w=1920');
        background-size: cover; background-position: center; padding: 100px 20px; color: white; text-align: center;
        border-radius: 0px 0px 50px 50px; margin: -60px -20px 40px -20px; box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }
    
    .price-badge {
        background: #ffcc00; color: #002d5a; padding: 15px 30px;
        border-radius: 15px; font-weight: 800; font-size: 28px; display: inline-block;
        margin: 20px 0; border: 2px solid #fff;
    }

    .bloque-header {
        background: #002d5a; color: #ffcc00; padding: 12px 20px;
        border-radius: 10px 10px 0 0; font-weight: 700; margin-top: 20px;
    }
    .temario-box {
        background: #fdfdfd; padding: 20px; border: 1px solid #eee;
        border-radius: 0 0 10px 10px; margin-bottom: 10px;
    }
    .video-container {
        background: #000; border-radius: 15px; padding: 10px; margin: 20px 0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .footer { text-align: center; padding: 40px; color: #888; border-top: 1px solid #eee; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. ESTRUCTURA ACADÉMICA Y VIDEOS (MODALIDAD 100% VIRTUAL)
# Aquí podés ir actualizando los IDs de los videos de YouTube o Vimeo
CURSOS_VIDEOS = {
    "Gestor Bancario": [
        {"modulo": "Módulo 1: Legislación y Ley 8204", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "desc": "Marco legal del sistema bancario costarricense."},
        {"modulo": "Módulo 2: Operativa de Caja", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "desc": "Detección de billetes y arqueos."}
    ],
    "Industria Médica": [
        {"modulo": "Módulo 1: Introducción a ISO 13485", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "desc": "Sistemas de gestión de calidad médica."},
        {"modulo": "Módulo 2: Protocolos de Cuarto Limpio", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "desc": "Gowning y control de contaminación."}
    ],
    "Asistente Contable": [
        {"modulo": "Módulo 1: Ciclo Contable y Tributación", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "desc": "Introducción al IVA y Renta CR."}
    ]
}

OFFER_ACADEMICA = {
    "Global Learning: English Mastery (24 Meses)": {
        "D": "24 Meses (Virtual Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Año 1: Cimentación": ["Fonética Correcta", "Gramática en Uso", "Conversación Inicial"],
            "Año 2: Perfeccionamiento": ["Business English", "Negociación", "Dominio C1"]
        }
    },
    "Técnico en Operaciones Bancarias (Gestor Bancario)": {
        "D": "6 Meses (Virtual Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "MÓDULOS": ["Ley 8204", "Detección de Billetaje", "Arqueos de Caja", "Inglés Técnico"]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses (Virtual Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "TEMARIO": ["Ciclo Contable CR", "IVA y Renta", "Planillas CCSS/INS", "Excel Financiero"]
        }
    }
}

# 3. NAVEGACIÓN
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>CETEP</h2>", unsafe_allow_html=True)
    st.write("---")
    nav = st.radio("MENÚ", ["🏠 Inicio", "📚 Oferta Académica", "💻 Mis Lecciones (Estudiantes)", "🔐 Panel de Dirección"])

# 4. PÁGINAS
if nav == "🏠 Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1>MODALIDAD 100% VIRTUAL</h1>
            <p>Aprendé a tu ritmo con lecciones interactivas y material de apoyo.</p>
            <div class="price-badge">₡15,000 AL MES</div>
        </div>
        """, unsafe_allow_html=True)
    st.info("💡 **Sistema Autodirigido:** Clases grabadas disponibles las 24 horas del día.")

elif nav == "📚 Oferta Académica":
    st.header("Programas Técnicos 2026")
    sel = st.selectbox("Elegí una carrera:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.subheader(f"⏱️ {info['D']} | 💰 {info['Inv']}")
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div><div class='temario-box'>", unsafe_allow_html=True)
        for t in temas: st.write(f"🔹 {t}")
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "💻 Mis Lecciones (Estudiantes)":
    st.header("Centro de Aprendizaje")
    curso_sel = st.selectbox("Seleccioná tu curso matriculado:", list(CURSOS_VIDEOS.keys()))
    
    lecciones = CURSOS_VIDEOS[curso_sel]
    leccion_sel = st.selectbox("Seleccioná el módulo a estudiar:", [l["modulo"] for l in lecciones])
    
    # Buscar data de la lección seleccionada
    data_leccion = next(item for item in lecciones if item["modulo"] == leccion_sel)
    
    st.markdown(f"### {data_leccion['modulo']}")
    st.write(data_leccion['desc'])
    
    st.markdown("<div class='video-container'>", unsafe_allow_html=True)
    st.video(data_leccion['url'])
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.button("Marcar como completada y ver examen")

elif nav == "🔐 Panel de Direction":
    if 'auth' not in st.session_state: st.session_state.auth = False
    
    if not st.session_state.auth:
        u = st.text_input("Director")
        p = st.text_input("Clave", type="password")
        if st.button("Acceder"):
            if u == "admin_cetep" and p == "Luis2026":
                st.session_state.auth = True
                st.rerun()
    else:
        st.subheader("Control de Dirección: Luis Humberto")
        t1, t2 = st.tabs(["📊 Métricas y Notas", "⚙️ Gestión de Videos"])
        with t1:
            c1, c2 = st.columns(2)
            c1.metric("Ingresos Proyectados", "₡7.5M", "Meta 500 alumnos")
            c2.metric("Matrículas", "40", "Abril 2026")
            st.write("### Notas de Estudiantes")
            st.table(pd.DataFrame({"Alumno": ["Carlos V.", "Ana J."], "Nota": [92, 88], "Curso": ["Banca", "Médica"]}))
        with t2:
            st.info("Desde aquí podés supervisar el orden de los videos que ven los alumnos.")
            st.write("Actualmente hay 5 módulos de video activos en la plataforma.")

st.markdown("<div class='footer'>© 2026 CETEP | Costa Rica</div>", unsafe_allow_html=True)
