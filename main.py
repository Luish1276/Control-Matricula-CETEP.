import streamlit as st
import pandas as pd

# Configuración profesional
st.set_page_config(page_title="CETEP - Gestión Académica", layout="wide", page_icon="🎓")

# Menú lateral
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", ["Inicio", "Oferta Académica", "Matrícula en Línea", "Portal Administrativo"])
    st.markdown("---")
    st.write("v1.5 - Control Interno")

# --- SECCIONES ANTERIORES (INICIO, OFERTA, MATRÍCULA) ---
if opcion == "Inicio":
    st.title("Centro de Estudios Técnicos y Especialidades Profesionales")
    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1200", use_container_width=True)

elif opcion == "Oferta Académica":
    st.header("Nuestros Programas Técnicos")
    tabs = st.tabs(["⚖️ Asistente Legal", "🏦 Gestor Bancario", "📊 Contabilidad Técnica", "⚙️ Procesos Industriales"])
    # (El contenido detallado de los técnicos va aquí como en el código anterior)

elif opcion == "Matrícula en Línea":
    st.header("📝 Inscripción Oficial")
    with st.form("form_matricula"):
        nombre = st.text_input("Nombre Completo:")
        cedula = st.text_input("Número de Cédula:")
        tecnico = st.selectbox("Carrera:", ["Asistente Legal", "Gestor Bancario Bilingüe", "Contabilidad Técnica", "Especialista en Procesos Industriales"])
        if st.form_submit_button("Confirmar Solicitud"):
            st.success(f"✅ ¡Registro para {tecnico} recibido!")

# --- SECCIÓN: PORTAL ADMINISTRATIVO (ACTUALIZADA CON "PÁGINAS" INTERNAS) ---
elif opcion == "Portal Administrativo":
    st.header("🔐 Acceso Administrativo")
    password = st.text_input("Clave de acceso:", type="password")
    
    if password == "cetep2026":
        st.success("Acceso Concedido")
        st.write("---")
        
        # Aquí es donde "entramos" a la oficina virtual
        menu_interno = st.selectbox("Seleccione una función:", [
            "Panel General", 
            "Gestión de Estudiantes", 
            "Registro de Notas (Profesores)",
            "Reportes de Matrícula"
        ])
        
        if menu_interno == "Panel General":
            st.subheader("Estado del Instituto")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Estudiantes", "154")
            col2.metric("Grupos Activos", "8")
            col3.metric("Solicitudes Nuevas", "12")
            
        elif menu_interno == "Gestión de Estudiantes":
            st.subheader("Base de Datos de Alumnos")
            # Aquí se mostraría la lista que antes iba al Excel
            df_alumnos = pd.DataFrame({
                "Nombre": ["Luis Varela", "Carlos Alonso", "Ana Mora"],
                "Cédula": ["1-0123-0456", "2-0345-0678", "4-0123-0890"],
                "Técnico": ["Asistente Legal", "Contabilidad", "Gestor Bancario"],
                "Estado": ["Activo", "Pendiente", "Activo"]
            })
            st.dataframe(df_alumnos, use_container_width=True)
            
        elif menu_interno == "Registro de Notas (Profesores)":
            st.subheader("Portal para el Cuerpo Docente")
            curso = st.selectbox("Curso a calificar:", ["Asistente Legal - Módulo Cobro Judicial", "Procesos Industriales - Calidad"])
            st.text_input("Nombre del Estudiante:")
            st.number_input("Nota Final:", min_value=0, max_value=100)
            if st.button("Guardar Nota"):
                st.success("Nota registrada en el sistema central.")
                
    elif password != "":
        st.error("Clave incorrecta. Intente de nuevo.")
