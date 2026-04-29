import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN E IDENTIDAD VISUAL DE ALTO NIVEL
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    .hero-full {
        background: linear-gradient(rgba(0,30,60,0.8), rgba(0,30,60,0.95)), 
                    url('https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1920');
        background-size: cover; background-position: center; padding: 100px 20px; color: white; text-align: center;
        border-radius: 0px 0px 50px 50px; margin: -60px -20px 40px -20px; box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }
    
    .hero-title { font-size: 50px; font-weight: 800; line-height: 1.1; margin-bottom: 10px; }
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
    .tema-line { padding: 8px 0; border-bottom: 1px solid #eef0f2; font-size: 15px; color: #333; }
    .footer { text-align: center; padding: 40px; color: #888; border-top: 1px solid #eee; margin-top: 50px; }
    
    .metric-card {
        background: #f8f9fa; border-top: 4px solid #002d5a; padding: 20px;
        border-radius: 10px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DATA ACADÉMICA RESTAURADA (NOMBRES CORRECTOS Y TEMARIO EXTENDIDO)
OFFER_ACADEMICA = {
    "Global Learning: English Mastery (24 Meses)": {
        "D": "24 Meses (Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Año 1: Nivel I - Cimentación": ["Fonética Correcta", "Gramática en Uso", "Listening de Contextos Diarios", "Conversación Inicial"],
            "Año 2: Nivel II - Perfeccionamiento": ["Business English Corporativo", "Negociación de Alto Nivel", "Inglés Técnico Sectorial", "Dominio Nativo C1"]
        }
    },
    "Técnico en Operaciones Bancarias (Gestor Bancario)": {
        "D": "6 Meses (Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "MÓDULO I: Marco Legal": ["Legislación Bancaria CR", "Ley 8204: Prevención de Lavado", "Ética y Deontología Bancaria"],
            "MÓDULO II: Operativa": ["Detección de Billetaje Falso (Dólar, Euro, Colones)", "Arqueos y Cuadres de Caja", "Seguridad Bancaria"],
            "Global Learning": ["Inglés Técnico Bancario Integrado"]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses (Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Contabilidad": ["Ciclo Contable Completo", "IVA y Renta en Costa Rica", "Conciliaciones Bancarias"],
            "Gestión": ["Planillas CCSS e INS", "Facturación Electrónica (ATV/TICA)", "Excel Financiero Avanzado"],
            "Global Learning": ["Inglés para Negocios Integrado"]
        }
    },
    "Gestión de Operaciones e Industria Médica": {
        "D": "9 Meses (Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Calidad": ["Normativa ISO 13485:2016", "GDP: Buenas Prácticas de Documentación", "Validación de Procesos"],
            "Manufactura": ["Protocolos de Cuarto Limpio (Gowning)", "Metrología (Vernier, Micrómetro)", "Lectura de Planos"],
            "Global Learning": ["Inglés para Manufactura Médica Integrado"]
        }
    },
    "Preparación Examen Excelencia Académica (Abogados)": {
        "D": "Curso Intensivo Virtual", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Áreas Jurídicas": ["Derecho Civil y Mercantil", "Derecho Público y Laboral", "Derecho Notarial", "Deontología"],
            "Simulacros": ["Análisis de Votos Sala IV", "Práctica de Exámenes de Excelencia Real"]
        }
    }
}

# 3. BASE DE DATOS PARA DIRECCIÓN
if 'db_estudiantes' not in st.session_state:
    st.session_state.db_estudiantes = pd.DataFrame([
        {"Nombre": "Carlos Varela", "Carrera": "Gestor Bancario", "Nota": 92, "Mensualidad": "Pagado"},
        {"Nombre": "Ana Jackson", "Carrera": "Industria Médica", "Nota": 88, "Mensualidad": "Pagado"},
        {"Nombre": "Luis Vargas", "Carrera": "Contabilidad", "Nota": 95, "Mensualidad": "Pendiente"}
    ])

# 4. NAVEGACIÓN
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#002d5a;'>CETEP</h2>", unsafe_allow_html=True)
    st.write("---")
    nav = st.radio("NAVEGACIÓN PRINCIPAL", ["🏠 Inicio", "📚 Oferta Académica", "📝 Matrícula", "🔐 Campus Virtual"])

if nav == "🏠 Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">FORMACIÓN TÉCNICA<br>DE ALTO NIVEL</h1>
            <p style="font-size: 20px; opacity: 0.9;">Excelencia Académica y Global Learning (Inglés).</p>
            <div class="price-badge">₡15,000 AL MES</div>
            <p>Matrícula ₡5,000 (Única vez) | 100% Virtual Autodirigido</p>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    c1.info("🌍 **Bilingüismo:** 24 meses de inglés incluidos.")
    c2.info("⚖️ **Garantía:** Respaldo de profesionales activos.")
    c3.info("🛡️ **Seguridad:** Certificación bajo estándares legales.")

elif nav == "📚 Oferta Académica":
    st.header("Detalle de Programas 2026")
    sel = st.selectbox("Seleccione una carrera para ver el temario extendido:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.subheader(f"⏱️ Duración: {info['D']} | 💰 {info['Inv']}")
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div>", unsafe_allow_html=True)
        st.markdown("<div class='temario-box'>", unsafe_allow_html=True)
        for t in temas: st.markdown(f"<div class='tema-line'>🔹 {t}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif nav == "📝 Matrícula":
    st.header("Reserva de Cupo")
    with st.form("mat"):
        st.text_input("Nombre Completo"), st.text_input("Cédula"), st.text_input("WhatsApp")
        st.selectbox("Programa de Interés", list(OFFER_ACADEMICA.keys()))
        if st.form_submit_button("RESERVAR MI LUGAR"):
            st.success("¡Datos enviados! Pronto recibirás el link de pago de matrícula.")

elif nav == "🔐 Campus Virtual":
    if 'auth' not in st.session_state: st.session_state.auth = False
    
    if not st.session_state.auth:
        st.subheader("Acceso al Sistema")
        u = st.text_input("Usuario")
        p = st.text_input("Contraseña", type="password")
        if st.button("INGRESAR"):
            if u == "admin_cetep" and p == "Luis2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Acceso denegado")
    else:
        # VISTA DEL DIRECTOR LUIS HUMBERTO
        st.subheader("👨‍💼 PANEL DE DIRECCIÓN (admin_cetep)")
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state.auth = False
            st.rerun()
            
        t1, t2, t3 = st.tabs(["📊 Control de Carrera (Notas)", "💰 Matrícula y Ganancias", "🎥 Video-Lecciones"])
        
        with t1:
            st.write("### Revisión de Notas y Rendimiento Académico")
            st.dataframe(st.session_state.db_estudiantes[["Nombre", "Carrera", "Nota"]], use_container_width=True)
        
        with t2:
            cant = len(st.session_state.db_estudiantes)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"<div class='metric-card'><h4>Matrícula Actual</h4><h2>{cant} Alumnos</h2></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div class='metric-card'><h4>Ganancia Mensual</h4><h2>₡{cant*15000:,.0f}</h2></div>", unsafe_allow_html=True)
            st.write("---")
            st.write("### Detalle de Pagos")
            st.table(st.session_state.db_estudiantes)

        with t3:
            st.subheader("Control de Material Multimedia")
            st.info("Vista previa de las lecciones grabadas para los estudiantes.")
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.markdown("<div class='footer'>© 2026 CETEP | Costa Rica</div>", unsafe_allow_html=True)
