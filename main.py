import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN E IDENTIDAD VISUAL (ELEGANTE)
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

# 1. CONFIGURACIÓN E IDENTIDAD VISUAL (ELEGANTE)
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }
    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.85), rgba(0,30,60,0.95)), 
                    url('https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1920');
        background-size: cover; background-position: center; padding: 100px 20px; color: white; text-align: center;
        border-radius: 0px 0px 50px 50px; margin: -60px -20px 40px -20px; box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }
    .price-badge { background: #ffcc00; color: #002d5a; padding: 15px 30px; border-radius: 15px; font-weight: 800; font-size: 28px; display: inline-block; margin: 20px 0; border: 2px solid #fff; }
    .bloque-header { background: #002d5a; color: #ffcc00; padding: 12px 20px; border-radius: 10px 10px 0 0; font-weight: 700; margin-top: 20px; }
    .temario-box { background: #fdfdfd; padding: 20px; border: 1px solid #eee; border-radius: 0 0 10px 10px; margin-bottom: 10px; }
    .tema-line { padding: 8px 0; border-bottom: 1px solid #eef0f2; font-size: 15px; color: #333; }
    .metric-card { background: #ffffff; border-top: 5px solid #002d5a; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. DATA ACADÉMICA (RESTAURADA TOTALMENTE)
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
            "MÓDULO I: Marco Legal": ["Legislación Bancaria CR", "Ley 8204: Prevención de Lavado", "Ética Bancaria"],
            "MÓDULO II: Operativa": ["Detección de Billetaje Falso", "Arqueos y Cuadres de Caja", "Seguridad Bancaria"],
            "Global Learning": ["Inglés Técnico Bancario Integrado"]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses (Virtual Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Contabilidad": ["Ciclo Contable Completo", "IVA y Renta Costa Rica", "Conciliaciones"],
            "Gestión": ["Planillas CCSS e INS", "Facturación Electrónica (ATV/TICA)", "Excel Financiero"],
            "Global Learning": ["Inglés para Negocios Integrado"]
        }
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses (Virtual Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Calidad": ["ISO 13485:2016", "GDP: Buenas Prácticas de Documentación", "Validación QMS"],
            "Manufactura": ["Protocolos Cuarto Limpio (Gowning)", "Metrología (Vernier/Micrómetro)", "Lectura de Planos"],
            "Global Learning": ["Inglés Industrial Médico Integrado"]
        }
    },
    "Preparación Examen Excelencia Académica (Abogados)": {
        "D": "Intensivo Virtual", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Áreas": ["Civil/Mercantil", "Público/Laboral", "Notarial/Deontología"],
            "Práctica": ["Análisis Votos Sala IV", "Simulacros de Examen Real"]
        }
    }
}

# 3. VIDEOS PARA MODALIDAD VIRTUAL
CURSOS_VIDEOS = {
    "Gestor Bancario": [{"modulo": "Módulo 1: Ley 8204", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}],
    "Asistente Contable": [{"modulo": "Módulo 1: IVA y Renta", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}],
    "Industria Médica": [{"modulo": "Módulo 1: ISO 13485", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}]
}

# 4. BASE DE DATOS DE DIRECCIÓN
if 'db_estudiantes' not in st.session_state:
    st.session_state.db_estudiantes = pd.DataFrame([
        {"Nombre": "Carlos Varela", "Curso": "Gestor Bancario", "Nota": 92, "Mensualidad": "Pagado"},
        {"Nombre": "Ana Jackson", "Curso": "Industria Médica", "Nota": 88, "Mensualidad": "Pagado"},
        {"Nombre": "Luis Vargas", "Curso": "Asistente Contable", "Nota": 95, "Mensualidad": "Pendiente"}
    ])

# 5. NAVEGACIÓN
with st.sidebar:
    st.markdown("## CETEP 2026")
    nav = st.radio("MENÚ", ["🏠 Inicio", "📚 Carreras", "💻 Campus Estudiante", "🔐 Panel Director"])

if nav == "🏠 Inicio":
    st.markdown("""<div class="hero-full"><h1>FORMACIÓN TÉCNICA PROFESIONAL</h1><p>Modalidad 100% Virtual Autodirigida</p><div class="price-badge">₡15,000 MENSUALES</div><p>Matrícula Única: ₡5,000</p></div>""", unsafe_allow_html=True)

elif nav == "📚 Carreras":
    sel = st.selectbox("Seleccione un programa:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.subheader(f"⏱️ {info['D']} | 💰 {info['Inv']}")
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div><div class='temario-box'>", unsafe_allow_html=True)
        for t in temas: st.markdown(f"<div class='tema-line'>✅ {t}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "💻 Campus Estudiante":
    st.header("🎥 Mis Lecciones Virtuales")
    c_sel = st.selectbox("Curso:", list(CURSOS_VIDEOS.keys()))
    l_sel = st.selectbox("Módulo:", [l["modulo"] for l in CURSOS_VIDEOS[c_sel]])
    st.video(next(item for item in CURSOS_VIDEOS[c_sel] if item["modulo"] == l_sel)["url"])

elif nav == "🔐 Panel Director":
    if 'auth' not in st.session_state: st.session_state.auth = False
    if not st.session_state.auth:
        u, p = st.text_input("Usuario"), st.text_input("Clave", type="password")
        if st.button("Ingresar"):
            if u == st.secrets["ADMIN_USER"] and p == st.secrets["ADMIN_PASSWORD"]:
    st.session_state.auth = True
    st.rerun()
    else:
        st.subheader("👨‍💼 Panel del Director Luis Humberto")
        cant = len(st.session_state.db_estudiantes)
        c1, c2 = st.columns(2)
        c1.markdown(f"<div class='metric-card'><h4>Matrículas (₡5k)</h4><h2>₡{cant*5000:,.0f}</h2></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='metric-card'><h4>Mensualidades (₡15k)</h4><h2>₡{cant*15000:,.0f}</h2></div>", unsafe_allow_html=True)
        st.write("### Control Académico")
        st.table(st.session_state.db_estudiantes)
        if st.sidebar.button("Cerrar Sesión"): st.session_state.auth = False; st.rerun()

st.markdown("<center style='color:#888; margin-top:50px;'>© 2026 CETEP | Costa Rica</center>", unsafe_allow_html=True)
