import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN DE PÁGINA (ESTILO ELITE)
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.7), rgba(0,30,60,0.9)), 
                    url('https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=1920');
        background-size: cover; background-position: center; padding: 100px 20px; color: white; text-align: center;
        border-radius: 0px 0px 50px 50px; margin: -60px -20px 40px -20px; box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    .hero-title { font-size: 50px; font-weight: 800; line-height: 1.1; margin-bottom: 10px; }
    
    .bloque-header {
        background: #002d5a; color: #ffcc00; padding: 12px 20px;
        border-radius: 10px 10px 0 0; font-weight: 700; margin-top: 20px;
    }
    .temario-box {
        background: #f8f9fa; padding: 20px; border: 1px solid #eee;
        border-radius: 0 0 10px 10px; margin-bottom: 10px;
    }
    .tema-line { padding: 8px 0; border-bottom: 1px solid #eef0f2; font-size: 15px; color: #333; }

    .card-financiera {
        background: white; padding: 20px; border-radius: 15px;
        border-left: 5px solid #28a745; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    .footer { text-align: center; padding: 40px; color: #888; border-top: 1px solid #eee; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. DATA ACADÉMICA (La Carnita)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "MES 1-2: Fundamentos": ["Sistemas Bancarios CR", "Legislación Financiera", "Ética Profesional"],
            "MES 3-4: Operativa": ["Manejo de Efectivo", "Detección de Falsos", "Prevención de Fraude"],
            "MES 5-6: Especialización": ["Normativa SUGEF", "Arqueos de Caja", "Empleabilidad"]
        }
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses", "Inv": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Malla": {
            "CUATRIMESTRE I": ["Intro Industria Médica", "GDP (Documentación)", "Metrología e Instrumentación"],
            "CUATRIMESTRE II": ["ISO 13485:2016", "Cuarto Limpio", "Lean Manufacturing"],
            "CUATRIMESTRE III": ["Lectura de Planos", "Pruebas Métricas", "Entrevista STAR"]
        }
    }
}

# 3. SIDEBAR
with st.sidebar:
    if os.path.exists("LOGO CETEP.jpg"):
        st.image("LOGO CETEP.jpg", use_container_width=True)
    else:
        st.markdown("<h2 style='text-align:center; color:#002d5a;'>CETEP</h2>", unsafe_allow_html=True)
    st.write("---")
    nav = st.radio("MENÚ", ["🏠 Inicio", "📚 Oferta Académica", "📝 Matrícula", "🔐 Campus Virtual"])

# 4. PÁGINAS
if nav == "🏠 Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">TU FUTURO PROFESIONAL<br>COMIENZA HOY</h1>
            <p style="font-size: 20px; opacity: 0.9;">Técnicos especializados con mensualidad única de ₡20,000.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("### Meta de Apertura (Ciclo 2026)")
    col1, col2 = st.columns([3, 1])
    col1.progress(65)
    col2.write("40/60 Cupos")
    
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.info("🏦 **Banca:** ₡5,000 semanales")
    c2.info("🏭 **Médica:** Especialización Coyol")
    c3.info("⚖️ **Legal:** Asistencia y Excelencia")

elif nav == "📚 Oferta Académica":
    sel = st.selectbox("Seleccione el programa:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.subheader(f"⏱️ {info['D']} | 💰 {info['Inv']}")
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div>", unsafe_allow_html=True)
        st.markdown("<div class='temario-box'>", unsafe_allow_html=True)
        for t in temas: st.markdown(f"<div class='tema-line'>✅ {t}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "📝 Matrícula":
    st.header("Formulario de Admisión")
    with st.form("reg"):
        st.text_input("Nombre"), st.text_input("WhatsApp")
        st.selectbox("Carrera", list(OFFER_ACADEMICA.keys()))
        if st.form_submit_button("RESERVAR MI CUPO"):
            st.balloons()
            st.success("¡Recibido! Nos comunicaremos para formalizar la matrícula.")

elif nav == "🔐 Campus Virtual":
    st.header("Área Estudiantil")
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        with st.container():
            col_l, col_r = st.columns(2)
            u = col_l.text_input("Usuario (Cédula)")
            p = col_r.text_input("Contraseña", type="password")
            if st.button("INGRESAR AL CAMPUS"):
                if u == "admin" and p == "123": # Simulación
                    st.session_state.logged_in = True
                    st.rerun()
                else: st.error("Credenciales incorrectas")
    else:
        tab1, tab2, tab3 = st.tabs(["📊 Notas", "💰 Estado Financiero", "📂 Material"])
        
        with tab1:
            st.subheader("Rendimiento Académico")
            data_notas = {"Módulo": ["Módulo I", "Módulo II"], "Nota": [95, 88], "Estado": ["Aprobado", "En curso"]}
            st.table(pd.DataFrame(data_notas))
            
        with tab2:
            st.subheader("Control de Pagos")
            st.markdown("""
                <div class='card-financiera'>
                    <h4>Saldo Actual: ₡0.00</h4>
                    <p>Próximo pago: ₡5,000 (Lunes)</p>
                    <small>Estado: Al día ✅</small>
                </div>
                """, unsafe_allow_html=True)
            st.write("### Historial de Pagos")
            st.write("- Matrícula: ₡10,000 (Pagado)")
            st.write("- Semana 1: ₡5,000 (Pagado)")
            
        with tab3:
            st.subheader("Recursos de Clase")
            st.write("📖 [PDF] Manual de Operaciones Bancarias")
            st.write("🎥 [VIDEO] Uso de Micrómetro y Vernier")
        
        if st.button("Cerrar Sesión"):
            st.session_state.logged_in = False
            st.rerun()

st.markdown("<div class='footer'>© 2026 CETEP | Costa Rica</div>", unsafe_allow_html=True)
