import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN E IDENTIDAD VISUAL (CETEP)
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
    .metric-card {
        background: #ffffff; border-left: 5px solid #002d5a; padding: 20px;
        border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;
    }
    .price-badge {
        background: #ffcc00; color: #002d5a; padding: 10px 25px;
        border-radius: 10px; font-weight: 800; font-size: 24px; display: inline-block; margin: 15px 0;
    }
    .footer { text-align: center; padding: 30px; color: #888; border-top: 1px solid #eee; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS DE CONTROL (DIRECCIÓN)
# Simulamos una base de datos para que el panel no aparezca vacío
if 'db_estudiantes' not in st.session_state:
    st.session_state.db_estudiantes = pd.DataFrame([
        {"Nombre": "Carlos Varela", "Curso": "Gestor Bancario", "Nota": 92, "Matrícula": "Paga", "Mensualidad": "Paga"},
        {"Nombre": "Ana Jackson", "Curso": "Industria Médica", "Nota": 88, "Matrícula": "Paga", "Mensualidad": "Paga"},
        {"Nombre": "Luis G. Vargas", "Curso": "Asistente Contable", "Nota": 95, "Matrícula": "Paga", "Mensualidad": "Pendiente"},
        {"Nombre": "María Carranza", "Curso": "English Mastery", "Nota": 85, "Matrícula": "Paga", "Mensualidad": "Paga"}
    ])

# 3. CONTENIDO DE LECCIONES (MODALIDAD VIRTUAL)
CURSOS_VIDEOS = {
    "Gestor Bancario": [
        {"modulo": "Módulo 1: Ley 8204 y Marco Legal", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
        {"modulo": "Módulo 2: Detección de Billetaje", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
    ],
    "Industria Médica": [
        {"modulo": "Módulo 1: ISO 13485 e Industria", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
    ],
    "Asistente Contable": [
        {"modulo": "Módulo 1: Ciclo Contable y Tributación", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
    ]
}

# 4. NAVEGACIÓN
with st.sidebar:
    st.markdown("## CETEP 2026")
    nav = st.radio("IR A:", ["🏠 Inicio", "📚 Carreras", "💻 Campus Estudiante", "🔐 Panel de Dirección"])

# 5. LÓGICA DE PÁGINAS
if nav == "🏠 Inicio":
    st.markdown("""
        <div class="hero-full">
            <h1>CENTRO DE ESTUDIOS TÉCNICOS</h1>
            <p>Excelencia Académica | Modalidad 100% Virtual Autodirigida</p>
            <div class="price-badge">Mensualidad: ₡15,000</div>
            <p>Matrícula Única: ₡5,000</p>
        </div>
        """, unsafe_allow_html=True)

elif nav == "📚 Carreras":
    st.header("Nuestra Oferta Académica")
    st.write("Técnicos diseñados para la inserción laboral inmediata.")
    # Aquí irían los temarios detallados que ya tenemos definidos

elif nav == "💻 Campus Estudiante":
    st.header("🎥 Mis Lecciones Virtuales")
    c_sel = st.selectbox("Curso:", list(CURSOS_VIDEOS.keys()))
    l_sel = st.selectbox("Módulo:", [l["modulo"] for l in CURSOS_VIDEOS[c_sel]])
    video_url = next(item for item in CURSOS_VIDEOS[c_sel] if item["modulo"] == l_sel)["url"]
    
    st.video(video_url)
    st.button("Marcar como completado")

elif nav == "🔐 Panel de Dirección":
    if 'auth' not in st.session_state: st.session_state.auth = False
    
    if not st.session_state.auth:
        st.subheader("Acceso Restringido")
        u = st.text_input("Usuario Director")
        p = st.text_input("Contraseña", type="password")
        if st.button("Ingresar"):
            if u == "admin_cetep" and p == "Luis2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Credenciales Inválidas")
    else:
        st.markdown("## 👨‍💼 Panel de Control de Dirección")
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state.auth = False
            st.rerun()

        # MÉTRICAS FINANCIERAS REALES
        total_alumnos = len(st.session_state.db_estudiantes)
        ingresos_mensuales = total_alumnos * 15000
        ingresos_matricula = total_alumnos * 5000

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"<div class='metric-card'><h3>Alumnos</h3><h2>{total_alumnos}</h2></div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='metric-card'><h3>Mensualidades</h3><h2>₡{ingresos_mensuales:,.0f}</h2></div>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<div class='metric-card'><h3>Matrículas</h3><h2>₡{ingresos_matricula:,.0f}</h2></div>", unsafe_allow_html=True)

        st.write("---")
        
        tab1, tab2 = st.tabs(["📝 Revisión Académica (Notas)", "🎥 Supervisión de Módulos"])
        
        with tab1:
            st.subheader("Control de Notas por Estudiante")
            st.dataframe(st.session_state.db_estudiantes, use_container_width=True)
        
        with tab2:
            st.subheader("Estado de Lecciones Virtuales")
            st.write("Actualmente hay lecciones cargadas para 3 carreras técnicas.")
            st.info("Recordá que podés subir nuevos videos actualizando el diccionario CURSOS_VIDEOS en el código.")

st.markdown("<div class='footer'>© 2026 CETEP | Gestión Luis Humberto V.</div>", unsafe_allow_html=True)
