import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN E IDENTIDAD VISUAL (CETEP 2026)
st.set_page_config(page_title="CETEP | Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    * { font-family: 'Poppins', sans-serif; }
    .main-header { background-color: #002d5a; color: white; padding: 2rem; border-radius: 10px; text-align: center; margin-bottom: 2rem; }
    .metric-card { background-color: #f8f9fa; border-left: 5px solid #ffcc00; padding: 1.5rem; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .bloque-header { background: #002d5a; color: #ffcc00; padding: 10px 15px; border-radius: 8px 8px 0 0; font-weight: 700; margin-top: 15px; }
    .temario-box { background: #fdfdfd; padding: 15px; border: 1px solid #eee; border-radius: 0 0 8px 8px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. DATA ACADÉMICA EXTENDIDA (LA CARNITA)
OFFER_ACADEMICA = {
    "Global Learning: English Mastery (24 Meses)": {
        "D": "24 Meses (Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "AÑO 1: Cimentación": ["Fonética y Sonidos", "Estructuras Gramaticales", "Fluidez Inicial"],
            "AÑO 2: Perfeccionamiento": ["Business English", "Negociación Bilingüe", "Dominio C1"]
        }
    },
    "Técnico en Operaciones Bancarias": {
        "D": "6 Meses (Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Módulos": ["Legislación Bancaria CR", "Ley 8204 (Lavado)", "Detección de Billetaje", "Arqueos de Caja"]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses (Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Contabilidad": ["Ciclo Contable", "IVA y Renta CR", "Conciliaciones"],
            "Gestión": ["Planillas CCSS/INS", "Facturación ATV/TICA", "Excel Financiero"]
        }
    },
    "Gestión de Industria Médica": {
        "D": "9 Meses (Autodirigido)", "Inv": "Matrícula ₡5,000 / Mensual ₡15,000",
        "Malla": {
            "Módulos": ["ISO 13485:2016", "Cuarto Limpio", "Metrología", "Lectura de Planos"]
        }
    }
}

# 3. BASE DE DATOS INTERNA PARA EL DIRECTOR
if 'db_estudiantes' not in st.session_state:
    st.session_state.db_estudiantes = pd.DataFrame([
        {"Nombre": "Carlos Varela", "Carrera": "Banca", "Nota": 92, "Pago": "Al día"},
        {"Nombre": "Ana Jackson", "Carrera": "Industria Médica", "Nota": 88, "Pago": "Al día"},
        {"Nombre": "Luis G. Vargas", "Carrera": "Contabilidad", "Nota": 95, "Pago": "Pendiente"}
    ])

# 4. SISTEMA DE NAVEGACIÓN
if 'autenticado' not in st.session_state: st.session_state.autenticado = False

menu = st.sidebar.radio("MENÚ", ["🏠 Inicio", "📚 Oferta Académica", "🔐 Campus Virtual (Director)"])

if menu == "🏠 Inicio":
    st.markdown("<div class='main-header'><h1>CETEP 2026</h1><p>Excelencia Técnica al alcance de todos</p></div>", unsafe_allow_html=True)
    st.markdown("<center><div style='font-size:30px; font-weight:800; color:#002d5a;'>MENSUALIDAD: ₡15,000</div></center>", unsafe_allow_html=True)
    st.info("🎯 **Meta Institucional:** 500 Estudiantes activos.")

elif menu == "📚 Oferta Académica":
    st.header("Programas Técnicos Profesionales")
    sel = st.selectbox("Seleccione una carrera:", list(OFFER_ACADEMICA.keys()))
    info = OFFER_ACADEMICA[sel]
    st.subheader(f"⏱️ {info['D']} | 💰 {info['Inv']}")
    for bloque, temas in info['Malla'].items():
        st.markdown(f"<div class='bloque-header'>{bloque}</div>", unsafe_allow_html=True)
        with st.container():
            for t in temas: st.write(f"✅ {t}")

elif menu == "🔐 Campus Virtual (Director)":
    if not st.session_state.autenticado:
        st.subheader("Acceso Administrativo")
        u = st.text_input("Usuario")
        p = st.text_input("Contraseña", type="password")
        if st.button("Ingresar"):
            if u == "admin_cetep" and p == "Luis2026":
                st.session_state.autenticado = True
                st.rerun()
            else: st.error("Acceso denegado")
    else:
        # VISTA DEL DIRECTOR LUIS
        st.markdown("<div class='main-header'><h1>Panel de Control del Director</h1></div>", unsafe_allow_html=True)
        
        # MÉTRICAS
        cant = len(st.session_state.db_estudiantes)
        c1, c2, c3 = st.columns(3)
        c1.metric("Matrícula Total", cant)
        c2.metric("Ganancia Mensual (₡15k/u)", f"₡{cant * 15000:,.0f}")
        c3.metric("Recaudación Matrícula", f"₡{cant * 5000:,.0f}")
        
        tab1, tab2, tab3 = st.tabs(["📊 Notas", "📋 Estudiantes", "🎥 Videos"])
        with tab1:
            st.write("### Revisión de Notas")
            st.dataframe(st.session_state.db_estudiantes[["Nombre", "Carrera", "Nota"]], use_container_width=True)
        with tab2:
            st.write("### Control de Pagos y Matrícula")
            st.table(st.session_state.db_estudiantes)
        with tab3:
            st.subheader("Planteamiento de Clases Autodirigidas")
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Ejemplo de video
            
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state.autenticado = False
            st.rerun()
