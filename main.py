import streamlit as st
import pandas as pd

# Configuración de la página para que se vea moderna y ancha
st.set_page_config(page_title="CETEP - Formación Técnica", layout="wide", page_icon="🎓")

# Estilo CSS para mejorar la apariencia (Colores más sobrios y profesionales)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #004a99;
        color: white;
    }
    .titulo-principal {
        color: #002d5a;
        text-align: center;
        font-family: 'Arial';
    }
    </style>
    """, unsafe_allow_html=True)

# Menú de navegación en la barra lateral
with st.sidebar:
    st.image("https://www.freeiconspng.com/uploads/graduation-cap-icon-png-1.png", width=100) # Icono temporal
    st.title("CETEP")
    opcion = st.radio("Menú Principal", ["Inicio", "Oferta Académica", "Matrícula en Línea", "Portal Administrativo"])
    st.markdown("---")
    st.write("📍 Costa Rica")

# --- SECCIÓN: INICIO (Estilo similar a ipeacr.com) ---
if opcion == "Inicio":
    st.markdown("<h1 class='titulo-principal'>Centro de Estudios Técnicos y Especialidades Profesionales</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #555;'>Excelencia Académica para el Futuro Profesional</h4>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=1200", use_container_width=True) # Imagen profesional de estudio
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("💡 Nuestra Misión")
        st.write("Brindar formación técnica de alta calidad para insertar profesionales capacitados en el mercado laboral costarricense.")
    with col2:
        st.subheader("🎓 Títulos Técnicos")
        st.write("Nuestros programas están diseñados bajo los estándares de exigencia que el sector empresarial demanda hoy.")
    with col3:
        st.subheader("🤝 Convenios")
        st.write("Buscamos alianzas estratégicas para que nuestros estudiantes realicen sus prácticas en entornos reales.")

# --- SECCIÓN: OFERTA ACADÉMICA ---
elif opcion == "Oferta Académica":
    st.header("Explorá nuestros Programas Técnicos")
    
    tab1, tab2, tab3 = st.tabs(["Derecho y Legal", "Banca y Finanzas", "Industria"])
    
    with tab1:
        st.subheader("Asistente Legal")
        st.write("Formamos expertos en el apoyo de procesos judiciales y notariales.")
        st.markdown("""
        **Módulos Destacados:**
        * Derecho Procesal Civil y Laboral.
        * Cobro Judicial y Gestión de Cartera.
        * Derecho Notarial para Asistentes.
        """)
        
    with tab2:
        st.subheader("Gestor Bancario Bilingüe")
        st.write("Capacitación integral para el sector financiero público y privado.")
        st.markdown("""
        **Módulos Destacados:**
        * Legislación Bancaria Costarricense.
        * Técnicas de Conteo y Detección de Moneda.
        * Inglés Técnico para Finanzas.
        """)
    
    with tab3:
        st.subheader("Contabilidad y Procesos")
        st.write("Dominio de las herramientas contables y normativas tributarias vigentes.")

# --- SECCIÓN: MATRÍCULA ---
elif opcion == "Matrícula en Línea":
    st.header("📝 Proceso de Inscripción")
    st.info("Complete el formulario para reservar su espacio en el próximo ciclo lectivo.")
    
    with st.form("form_matricula"):
        nombre = st.text_input("Nombre Completo:")
        cedula = st.text_input("Número de Cédula:")
        correo = st.text_input("Correo Electrónico:")
        curso_interes = st.selectbox("Técnico de interés:", ["Asistente Legal", "Gestor Bancario", "Contabilidad"])
        
        if st.form_submit_button("Enviar Solicitud"):
            st.success("✅ Su solicitud ha sido enviada. Un asesor se pondrá en contacto pronto.")
            st.balloons()

# --- SECCIÓN: PORTAL ADMINISTRATIVO (Gestión para Luis y Profesores) ---
elif opcion == "Portal Administrativo":
    st.header("🔐 Acceso Administrativo")
    password = st.text_input("Contraseña de acceso:", type="password")
    
    if password == "cetep2026": # Tu clave privada
        st.success("Bienvenido al Panel de Control")
        
        modo = st.selectbox("Acción:", ["Ver Lista de Alumnos", "Ingresar Notas/Asistencia", "Gestionar Profesores"])
        
        if modo == "Ver Lista de Alumnos":
            # Aquí verías los datos que vienen del formulario
            data_simulada = {
                "Fecha": ["25/04/2026", "26/04/2026"],
                "Estudiante": ["Juan Pérez", "María Rodríguez"],
                "Curso": ["Asistente Legal", "Gestor Bancario"],
                "Estado": ["Pendiente de Pago", "Matriculado"]
            }
            st.table(pd.DataFrame(data_simulada))
    elif password != "":
        st.error("Acceso denegado.")
