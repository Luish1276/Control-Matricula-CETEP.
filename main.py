import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILO PROFESIONAL
st.set_page_config(page_title="CETEP | Formación Técnica Profesional", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    /* Hero Section */
    .hero-full {
        background: linear-gradient(rgba(0,45,90,0.85), rgba(0,45,90,0.85)), 
                    url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&q=80&w=1920');
        background-size: cover;
        background-position: center;
        padding: 80px 20px;
        color: white;
        text-align: center;
        border-radius: 0px 0px 40px 40px;
        margin: -60px -20px 40px -20px;
    }
    
    .hero-title { font-size: 48px; font-weight: 800; margin-bottom: 5px; }
    .hero-sub { font-size: 20px; font-weight: 300; margin-bottom: 25px; opacity: 0.9; }

    /* Tarjetas de Programas */
    .program-card {
        background: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #eee;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        text-align: center;
        height: 100%;
    }
    
    .category-tag {
        background: #e3f2fd;
        color: #004a99;
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 10px;
        display: inline-block;
    }

    .footer { text-align: center; padding: 30px; color: #888; font-size: 13px; border-top: 1px solid #eee; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS ACADÉMICA (RESTABLECIDA AL 100%)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias": {
        "D": "6 Meses",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Plan": ["Sistemas Financieros", "Ética Bancaria", "Matemática", "Manejo de Efectivo", "Prevención de Fraude", "SUGEF", "Arqueos"]
    },
    "Técnico Asistente Legal": {
        "D": "9 Meses",
        "Inversion": "Consultar Plan",
        "Plan": ["Investigación Jurídica", "Redacción Documental", "Derecho Civil", "Legislación Migratoria", "Derecho Laboral", "Familia y Penal"]
    },
    "Asistente Contable Administrativo": {
        "D": "9 Meses",
        "Inversion": "Consultar Plan",
        "Plan": ["Principios Contables", "Legislación Comercial", "Excel Avanzado", "IVA y Renta", "Planillas y CCSS", "Análisis Financiero"]
    },
    "Gestión de Operaciones e Industria Médica": { # ENFOQUE COYOL
        "D": "9 Meses",
        "Inversion": "Consultar Plan",
        "Plan": ["ISO 13485", "GDP (Documentación)", "Metrología (Vernier)", "Lean Manufacturing", "Cuartos Limpios", "Pruebas Métricas y Entrevista STAR"]
    },
    "Inglés Global Conversacional": {
        "D": "12 Meses",
        "Inversion": "Consultar Plan",
        "Plan": ["Fonética", "Gramática", "Vocabulario", "Business English", "Fluidez Profesional", "Certificación"]
    },
    "Prep. Colegio de Abogados": {
        "D": "Intensivo",
        "Inversion": "Consultar Plan",
        "Plan": ["Civil/Mercantil", "Penal/Familia", "Público/Constitucional", "Deontología Jurídica"]
    }
}

# 3. PERSISTENCIA Y NAVEGACIÓN
if 'alumnos_db' not in st.session_state:
    st.session_state['alumnos_db'] = [{"Nombre": "Luis Varela", "Cédula": "1-0000-0000", "Curso": "Director", "Saldo_Pendiente": 0}]

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=60)
    st.title("SISTEMA CETEP")
    nav = st.radio("Navegación", ["⭐ Inicio", "📚 Programas", "📝 Matrícula", "🔐 Campus Virtual"])

# --- PÁGINAS ---

if nav == "⭐ Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">DEL AULA AL COYOL</h1>
            <p class="hero-sub">Técnicos especializados con el mejor modelo de pago en Costa Rica.</p>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='program-card'><div class='category-tag'>BANCA</div><h3>6 Meses</h3><p>Pagos semanales de ₡5,000.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='program-card'><div class='category-tag'>INDUSTRIA</div><h3>9 Meses</h3><p>Enfoque en Dispositivos Médicos.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='program-card'><div class='category-tag'>HORARIOS</div><h3>Mañana-Tarde-Noche</h3><p>Bloques de 9-11, 2-4 y 6-8.</p></div>", unsafe_allow_html=True)

elif nav == "📚 Programas":
    st.header("Nuestra Oferta Académica")
    sel = st.selectbox("Seleccione un técnico:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.metric("Duración", info["D"])
    st.write(f"**Inversión:** {info['Inversion']}")
    st.write("### Temario Principal:")
    for t in info["Plan"]: st.write(f"🔹 {t}")

elif nav == "📝 Matrícula":
    st.header("Inicie su Proceso")
    with st.form("registro"):
        n = st.text_input("Nombre Completo")
        c = st.text_input("Cédula")
        cur = st.selectbox("Técnico", list(OFFER_ACADEMICA.keys()))
        hor = st.selectbox("Horario", ["Mañana (9-11 am)", "Tarde (2-4 pm)", "Noche (6-8 pm)"])
        if st.form_submit_button("REGISTRAR MATRÍCULA"):
            st.session_state['alumnos_db'].append({"Nombre": n, "Cédula": c, "Curso": cur, "Horario": hor, "Saldo_Pendiente": 15000})
            st.success("Registro completado. Saldo inicial: ₡15,000.")

elif nav == "🔐 Campus Virtual":
    st.header("Acceso al Sistema")
    cl = st.text_input("Cédula de Estudiante")
    if st.button("Consultar Estado"):
        alu = next((x for x in st.session_state['alumnos_db'] if x['Cédula'] == cl), None)
        if alu:
            st.write(f"**Alumno:** {alu['Nombre']}")
            if alu['Saldo_Pendiente'] > 10000:
                st.error(f"⚠️ Saldo Pendiente: ₡{alu['Saldo_Pendiente']}. Favor cancelar para habilitar acceso.")
            else:
                st.success("✅ Acceso Habilitado al Aula Virtual.")
        else: st.error("Cédula no encontrada.")

st.markdown("<div class='footer'>© 2026 CETEP | Costa Rica - Educación Técnica para el Siglo XXI</div>", unsafe_allow_html=True)
