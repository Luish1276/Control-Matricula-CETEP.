import streamlit as st
import pandas as pd

# Configuración profesional
st.set_page_config(page_title="CETEP - Gestión Académica", layout="wide", page_icon="🎓")

# Menú lateral
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", ["Inicio", "Oferta Académica", "Matrícula en Línea", "Portal Administrativo"])
    st.markdown("---")
    st.write("v1.6 - Control de Accesos")

# --- SECCIONES PÚBLICAS (Se mantienen igual) ---
if opcion == "Inicio":
    st.title("Centro de Estudios Técnicos y Especialidades Profesionales")
    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1200", use_container_width=True)

elif opcion == "Oferta Académica":
    st.header("Nuestros Programas Técnicos")
    tabs = st.tabs(["⚖️ Asistente Legal", "🏦 Gestor Bancario", "📊 Contabilidad Técnica", "⚙️ Procesos Industriales"])
    # Aquí va el contenido que ya definimos...

elif opcion == "Matrícula en Línea":
    st.header("📝 Inscripción Oficial")
    with st.form("form_matricula"):
        nombre = st.text_input("Nombre Completo:")
        cedula = st.text_input("Cédula:")
        tecnico = st.selectbox("Carrera:", ["Asistente Legal", "Gestor Bancario Bilingüe", "Contabilidad Técnica", "Especialista en Procesos Industriales"])
        if st.form_submit_button("Confirmar Solicitud"):
            st.success(f"✅ ¡Registro para {tecnico} recibido!")

# --- SECCIÓN: PORTAL ADMINISTRATIVO CON DOBLE NIVEL ---
elif opcion == "Portal Administrativo":
    st.header("🔐 Acceso Restringido")
    
    # Usamos una sola caja de texto para la clave, el sistema sabrá quién es según lo que escriban
    clave = st.text_input("Ingrese su clave de acceso:", type="password")
    
    # 1. NIVEL LUIS (ADMINISTRADOR TOTAL)
    if clave == "admin_cetep": 
        st.success("Bienvenido, Director Luis Varela")
        
        menu_admin = st.selectbox("Panel de Control General:", [
            "Resumen Financiero y Reportes", 
            "Gestión de Matrícula Global",
            "Configuración de Profesores"
        ])
        
        if menu_admin == "Resumen Financiero y Reportes":
            st.subheader("📊 Reporte de Ingresos y Proyecciones")
            col1, col2 = st.columns(2)
            col1.metric("Ingresos Mes Actual", "₡1,250,000", "+5%")
            col2.metric("Matrículas Pendientes", "8 Estudiantes")
            
            st.write("### Gráfico de Crecimiento por Técnico")
            datos_finanzas = pd.DataFrame({
                "Técnico": ["Asistente Legal", "Bancario", "Contabilidad", "Industrial"],
                "Ingresos": [450000, 300000, 250000, 250000]
            })
            st.bar_chart(datos_finanzas.set_index("Técnico"))

        elif menu_admin == "Gestión de Matrícula Global":
            st.subheader("Lista Maestra de Estudiantes")
            # Aquí verías a TODOS los alumnos de todos los técnicos
            df_total = pd.DataFrame({
                "Estudiante": ["Juan Pérez", "Ana Mora", "Luis Brenes"],
                "Técnico": ["Asistente Legal", "Gestor Bancario", "Contabilidad"],
                "Pago": ["Al día", "Pendiente", "Al día"]
            })
            st.table(df_total)

    # 2. NIVEL PROFESOR (SOLO ACADÉMICO)
    elif clave == "profe_cetep":
        st.success("Bienvenido al Portal Docente")
        
        # El profesor NO VE las finanzas. Solo ve estas opciones:
        menu_profe = st.selectbox("Funciones Docentes:", [
            "Mis Listas de Clase", 
            "Registro de Calificaciones",
            "Control de Asistencia"
        ])
        
        if menu_profe == "Mis Listas de Clase":
            st.subheader("Estudiantes Asignados")
            # El profe solo ve nombres y cédulas, nada de pagos ni dinero
            df_profe = pd.DataFrame({
                "Estudiante": ["Juan Pérez", "María Castro"],
                "Cédula": ["1-1111-1111", "2-2222-2222"],
                "Curso": ["Asistente Legal", "Asistente Legal"]
            })
            st.dataframe(df_profe, use_container_width=True)
            
        elif menu_profe == "Registro de Calificaciones":
            st.subheader("Ingreso de Notas")
            with st.expander("Módulo: Cobro Judicial"):
                st.number_input("Nota Juan Pérez:", 0, 100)
                st.number_input("Nota María Castro:", 0, 100)
                st.button("Guardar Notas del Módulo")
    
    elif clave != "":
        st.error("Clave no reconocida. Verifique sus credenciales.")
