import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN
st.set_page_config(page_title="CETEP - Administración Central", layout="wide", page_icon="🎓")

# Estilo para que se vea serio y profesional
st.markdown("""
    <style>
    .titulo-ipea { color: #002d5a; text-align: center; font-weight: bold; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    .metric-box { background-color: #f0f2f6; padding: 15px; border-radius: 10px; border: 1px solid #d1d1d1; }
    </style>
    """, unsafe_allow_html=True)

# 2. MENÚ LATERAL
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", ["Inicio", "Técnicos", "Matrícula", "Información", "Campus Virtual"])
    st.markdown("---")
    st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50686302333)")

# --- DATOS DEL SISTEMA ---
if 'db_alumnos' not in st.session_state:
    st.session_state['db_alumnos'] = [
        {"Nombre": "Juan Pérez", "Cédula": "1-1111-1111", "Tel": "8888-0000", "Curso": "Asistente Legal"},
        {"Nombre": "Ana Mora", "Cédula": "2-2222-2222", "Tel": "7777-0000", "Curso": "Gestión Bancaria"}
    ]

# --- 3. LÓGICA DE SECCIONES ---

if opcion == "Inicio":
    st.markdown("<h1 class='titulo-ipea'>CETEP: Sistema de Gestión Académica</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)

elif opcion == "Matrícula":
    st.header("📝 Registro de Estudiantes")
    with st.form("form_registro"):
        col1, col2 = st.columns(2)
        with col1:
            n = st.text_input("Nombre Completo:")
            c = st.text_input("Cédula:")
        with col2:
            t = st.text_input("Teléfono:")
            cur = st.selectbox("Programa:", ["Asistente Legal", "Bancario", "Contabilidad", "Industrial", "Inglés"])
        d = st.text_area("Dirección Exacta:")
        if st.form_submit_button("Registrar en Sistema"):
            st.session_state['db_alumnos'].append({"Nombre": n, "Cédula": c, "Tel": t, "Curso": cur})
            st.success("Alumno guardado correctamente.")

elif opcion == "Campus Virtual":
    st.markdown("<h2 style='text-align: center;'>🔐 Control de Acceso</h2>", unsafe_allow_html=True)
    perfil = st.selectbox("Ingresar como:", ["Director", "Estudiante", "Profesor"])
    
    # --- PANEL DEL DIRECTOR (TU PANEL) ---
    if perfil == "Director":
        clave = st.text_input("Contraseña Maestro:", type="password")
        if clave == "admin_cetep":
            st.success("👨‍⚖️ Bienvenido, Director Luis Varela")
            
            t_adm1, t_adm2, t_adm3 = st.tabs(["📊 Dashboard Financiero", "👥 Lista de Alumnos", "🎥 Gestión de Videos"])
            
            with t_adm1:
                col_m1, col_m2 = st.columns(2)
                with col_m1:
                    st.metric("Ingresos Totales", "₡1,250,000", "+12%")
                with col_m2:
                    st.metric("Matrículas Activas", len(st.session_state['db_alumnos']))
                
            with t_adm2:
                st.subheader("Base de Datos de Estudiantes")
                df = pd.DataFrame(st.session_state['db_alumnos'])
                st.dataframe(df, use_container_width=True)
                
            with t_adm3:
                st.subheader("Subir Enlaces de Clases")
                st.text_input("Título de la clase:")
                st.text_input("Link de Google Meet / YouTube:")
                st.button("Publicar en Videoteca")
        elif clave != "":
            st.error("Contraseña incorrecta.")

    # --- PANEL DEL ESTUDIANTE ---
    elif perfil == "Estudiante":
        ced = st.text_input("Cédula:")
        if st.button("Entrar a mis cursos"):
            st.info("Aquí el estudiante verá sus notas y temario.")

    # --- PANEL DEL PROFESOR ---
    elif perfil == "Profesor":
        if st.text_input("Clave Profe:", type="password") == "profe_cetep":
            st.write("Panel para subir notas.")
