import streamlit as st
import pandas as pd

# Configuración de página ancha y profesional
st.set_page_config(page_title="CETEP - Centro de Estudios Técnicos", layout="wide", page_icon="🎓")

# Estilo CSS para imitar la sobriedad de IPEA
st.markdown("""
    <style>
    .titulo-ipea { color: #002d5a; text-align: center; font-weight: bold; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #f0f2f6; border-radius: 4px; padding: 10px 20px; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Menú de Navegación idéntico a IPEA
with st.sidebar:
    st.image("https://www.freeiconspng.com/uploads/graduation-cap-icon-png-1.png", width=80)
    st.title("CETEP")
    # Estructura de menú solicitada
    opcion = st.radio("Navegación", [
        "Inicio", 
        "Técnicos", 
        "Inglés", 
        "Matrícula", 
        "Información", 
        "Campus Virtual"
    ])
    st.markdown("---")
    st.caption("© 2026 CETEP Costa Rica")

# --- 1. INICIO ---
if opcion == "Inicio":
    st.markdown("<h1 class='titulo-ipea'>Centro de Estudios Técnicos y Especialidades Profesionales</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.subheader("Líderes en Formación Técnica")
    st.write("Brindamos herramientas prácticas para una inserción laboral exitosa. Nuestra metodología se enfoca en el 'saber hacer', garantizando profesionales competentes desde el primer día.")

# --- 2. TÉCNICOS (LOS 4 ORIGINALES) ---
elif opcion == "Técnicos":
    st.header("Nuestros Programas Técnicos")
    tabs = st.tabs(["⚖️ Asistente Legal", "🏦 Gestor Bancario", "📊 Contabilidad", "⚙️ Procesos Industriales"])
    
    with tabs[0]:
        st.subheader("Técnico Superior en Asistente Legal")
        st.write("Especialización en procesos judiciales, cobro judicial, prescripción y derecho notarial.")
    with tabs[1]:
        st.subheader("Técnico en Gestión Bancaria")
        st.write("Formación integral en legislación financiera, SUGEF y operaciones de caja.")
    with tabs[2]:
        st.subheader("Técnico en Contabilidad Técnica")
        st.write("Manejo de ciclo contable, impuestos (ATV) y planillas de la CCSS.")
    with tabs[3]:
        st.subheader("Especialista en Procesos Industriales")
        st.write("Optimización de producción, control de calidad y seguridad industrial.")

# --- 3. INGLÉS (NUEVA SECCIÓN ESTILO IPEA) ---
elif opcion == "Inglés":
    st.header("Programa de Idioma Inglés")
    st.image("https://images.unsplash.com/photo-1543165796-5426273eaab3?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Inglés para el Éxito Profesional")
        st.write("Nuestro programa está diseñado para que el estudiante alcance fluidez conversacional y técnica, enfocada en los negocios y la industria.")
    with col2:
        st.info("""
        **Niveles:** Básico, Intermedio y Avanzado.
        **Enfoque:** Conversacional (70%) y Técnico (30%).
        **Certificación:** Alineada al Marco Común Europeo.
        """)

# --- 4. MATRÍCULA ---
elif opcion == "Matrícula":
    st.header("📝 Proceso de Matrícula")
    with st.form("form_ipea"):
        st.write("Ingrese sus datos para formalizar la inscripción.")
        nombre = st.text_input("Nombre Completo:")
        cedula = st.text_input("Cédula:")
        opcion_curs = st.selectbox("Programa de interés:", ["Asistente Legal", "Gestor Bancario", "Contabilidad", "Procesos Industriales", "Inglés"])
        if st.form_submit_button("Enviar Formulario"):
            st.success("✅ Datos recibidos. Un asesor le contactará pronto.")

# --- 5. INFORMACIÓN (NOSOTROS) ---
elif opcion == "Información":
    st.header("Sobre Nosotros")
    st.write("CETEP es una institución comprometida con el desarrollo profesional de Costa Rica.")
    st.subheader("Nuestra Sede")
    st.write("Ubicados en el corazón de Heredia, contamos con instalaciones modernas y laboratorios de alta tecnología.")
    st.markdown("""
    * **Visión:** Ser el referente nacional en educación técnica de ciclo corto.
    * **Valores:** Excelencia, Ética y Práctica Profesional.
    """)

# --- 6. CAMPUS VIRTUAL (ACCESO ADMINISTRATIVO/DOCENTE) ---
elif opcion == "Campus Virtual":
    st.header("🔐 Acceso al Campus")
    clave = st.text_input("Ingrese su contraseña de acceso:", type="password")
    
    if clave == "admin_cetep":
        st.success("Acceso como Director Luis Varela")
        st.selectbox("Gestión:", ["Reportes Financieros", "Control de Matrícula", "Configuración"])
    elif clave == "profe_cetep":
        st.success("Acceso como Cuerpo Docente")
        st.selectbox("Gestión:", ["Listas de Asistencia", "Registro de Notas"])
    elif clave != "":
        st.error("Credenciales incorrectas")
