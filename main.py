import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CETEP - Campus Virtual", layout="wide", page_icon="🎓")

# Estilo profesional tipo IPEA
st.markdown("""
    <style>
    .titulo-ipea { color: #002d5a; text-align: center; font-weight: bold; font-family: 'Arial'; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    .card-academica { background-color: #ffffff; padding: 20px; border: 1px solid #e0e0e0; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); margin-bottom: 15px; }
    .nota-aprobada { color: #28a745; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. NAVEGACIÓN
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", ["Inicio", "Técnicos", "Inglés", "Matrícula", "Información", "Campus Virtual"])
    st.markdown("---")
    st.subheader("📱 Soporte")
    st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50686302333)")

# --- BASE DE DATOS ACADÉMICA (Simulada) ---
base_datos = {
    "1-1111-1111": {
        "Nombre": "Juan Pérez",
        "Carrera": "Técnico en Asistente Legal",
        "Cursos_Inscritos": ["Derecho Civil I", "Cobro Judicial", "Derecho Notarial"],
        "Temario": [
            "Módulo 1: Introducción al Ordenamiento Jurídico CR",
            "Módulo 2: Gestión de Cobro y Plazos de Prescripción",
            "Módulo 3: Actos Notariales y Protocolo",
            "Módulo 4: Plataformas Digitales del Poder Judicial"
        ],
        "Notas": [
            {"Materia": "Derecho Civil I", "Nota": 92, "Estado": "Aprobado"},
            {"Materia": "Cobro Judicial", "Nota": 88, "Estado": "Aprobado"},
            {"Materia": "Derecho Notarial", "Nota": 0, "Estado": "En Curso"}
        ]
    }
}

# --- 3. LÓGICA DE SECCIONES ---

if opcion == "Inicio":
    st.markdown("<h1 class='titulo-ipea'>CETEP: Formación Técnica Superior</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)

elif opcion == "Matrícula":
    st.header("📝 Registro de Nuevo Estudiante")
    with st.form("registro"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Nombre Completo:")
            st.text_input("Cédula:")
        with col2:
            st.text_input("Teléfono:")
            st.selectbox("Técnico:", ["Asistente Legal", "Bancario", "Contabilidad", "Industrial", "Inglés"])
        st.text_area("Dirección:")
        st.form_submit_button("Matricular")

elif opcion == "Campus Virtual":
    st.markdown("<h2 style='text-align: center;'>🔐 Campus Virtual CETEP</h2>", unsafe_allow_html=True)
    
    perfil = st.selectbox("Acceder como:", ["Estudiante", "Docente", "Administración"])
    
    if perfil == "Estudiante":
        cedula_log = st.text_input("Ingrese su número de cédula:", placeholder="1-1111-1111")
        if st.button("Ingresar a mi Panel"):
            if cedula_log in base_datos:
                alumno = base_datos[cedula_log]
                st.success(f"Bienvenido(a), {alumno['Nombre']}")
                
                # Pestañas de Estudiante
                tab_cursos, tab_temario, tab_notas = st.tabs(["📚 Mis Cursos", "📖 Temarios", "📊 Mis Notas"])
                
                with tab_cursos:
                    st.subheader("Cursos Activos")
                    for curso in alumno['Cursos_Inscritos']:
                        st.markdown(f"<div class='card-academica'>🔹 {curso}</div>", unsafe_allow_html=True)
                
                with tab_temario:
                    st.subheader(f"Plan de Estudios - {alumno['Carrera']}")
                    for item in alumno['Temario']:
                        st.write(item)
                    st.button("📥 Descargar Guía Académica (PDF)")
                
                with tab_notas:
                    st.subheader("Reporte de Calificaciones")
                    df_notas = pd.DataFrame(alumno['Notas'])
                    st.table(df_notas)
            else:
                st.error("Cédula no encontrada. Por favor verifique o contacte a soporte.")

    elif perfil == "Docente":
        st.text_input("Clave Docente:", type="password")
        if st.button("Entrar"): st.info("Panel Docente habilitado.")

    elif perfil == "Administración":
        clave = st.text_input("Clave Director:", type="password")
        if st.button("Entrar"): 
            if clave == "admin_cetep": st.success("Acceso concedido, Luis.")
