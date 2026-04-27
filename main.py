import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA (ESTILO PROFESIONAL)
st.set_page_config(page_title="CETEP - Centro de Estudios Técnicos", layout="wide", page_icon="🎓")

# Estilo CSS para imitar la sobriedad y profesionalismo de IPEA
st.markdown("""
    <style>
    .titulo-ipea { color: #002d5a; text-align: center; font-weight: bold; font-family: 'Arial'; margin-bottom: 20px; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #f0f2f6; border-radius: 4px; padding: 10px 20px; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    .sidebar-text { font-size: 14px; color: #555; }
    </style>
    """, unsafe_allow_html=True)

# 2. MENÚ DE NAVEGACIÓN (ESTRUCTURA IPEA)
with st.sidebar:
    st.image("https://www.freeiconspng.com/uploads/graduation-cap-icon-png-1.png", width=80)
    st.title("CETEP")
    opcion = st.radio("Menú Principal", [
        "Inicio", 
        "Técnicos", 
        "Inglés", 
        "Matrícula", 
        "Información", 
        "Campus Virtual"
    ])
    st.markdown("---")
    st.subheader("📱 Soporte Inmediato")
    # Enlace a WhatsApp (Sustituye el número por el tuyo)
    st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50680000000)")
    st.markdown("---")
    st.caption("© 2026 CETEP - Heredia, Costa Rica")

# --- 3. LÓGICA DE LAS SECCIONES ---

# SECCIÓN: INICIO
if opcion == "Inicio":
    st.markdown("<h1 class='titulo-ipea'>Centro de Estudios Técnicos y Especialidades Profesionales</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🚀 Nuestra Propuesta")
        st.write("En CETEP, nos enfocamos en la formación técnica de ciclo corto con alta salida laboral. Nuestros programas están diseñados por expertos activos en cada industria.")
    with col2:
        st.subheader("🎓 Excelencia Académica")
        st.write("Ubicados en Heredia, ofrecemos modalidades flexibles (Presencial, Híbrida y Virtual) para que podás estudiar sin dejar de trabajar.")

# SECCIÓN: TÉCNICOS (LOS 4 ORIGINALES)
elif opcion == "Técnicos":
    st.header("Programas Técnicos Disponibles")
    st.write("Haga clic en cada pestaña para ver los detalles del programa:")
    
    tab1, tab2, tab3, tab4 = st.tabs(["⚖️ Asistente Legal", "🏦 Gestor Bancario", "📊 Contabilidad", "⚙️ Procesos Industriales"])
    
    with tab1:
        st.subheader("Técnico Superior en Asistente Legal")
        st.markdown("""
        **Módulos Destacados:**
        * Derecho Procesal Civil y Mercantil.
        * **Cobro Judicial y Prescripción** (Enfoque Radar Legal).
        * Gestión de Escrituras y Derecho Notarial.
        * Uso de Plataformas del Poder Judicial.
        """)
        
    with tab2:
        st.subheader("Técnico en Gestión Bancaria Bilingüe")
        st.markdown("""
        **Módulos Destacados:**
        * Normativa SUGEF y Ley Bancaria Nacional.
        * Operaciones de Caja y Detección de Billetes.
        * Servicio al Cliente Bancario de Alto Nivel.
        * Inglés Técnico Financiero.
        """)
        
    with tab3:
        st.subheader("Técnico en Contabilidad Técnica")
        st.markdown("""
        **Módulos Destacados:**
        * Ciclo Contable Completo.
        * Legislación Tributaria (IVA, Renta, ATV).
        * Planillas, CCSS e INS.
        * Contabilidad de Costos Industriales.
        """)
        
    with tab4:
        st.subheader("Especialista en Procesos Industriales")
        st.markdown("""
        **Módulos Destacados:**
        * Control Estadístico de Procesos.
        * Seguridad Industrial e Higiene Ocupacional.
        * Optimización de la Producción y Logística.
        * Introducción a Lean Manufacturing.
        """)

# SECCIÓN: INGLÉS
elif opcion == "Inglés":
    st.header("Programa de Idioma Inglés")
    st.image("https://images.unsplash.com/photo-1543165796-5426273eaab3?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.subheader("Inglés Conversacional y Técnico")
    st.write("Programa diseñado para alcanzar fluidez en ambientes de negocios y servicios.")
    st.info("**Niveles:** Básico, Intermedio y Avanzado. Certificación alineada al Marco Común Europeo.")

# SECCIÓN: MATRÍCULA
elif opcion == "Matrícula":
    st.header("📝 Proceso de Inscripción")
    st.write("Complete el siguiente formulario para reservar su espacio:")
    with st.form("form_registro"):
        nombre = st.text_input("Nombre Completo:")
        cedula = st.text_input("Número de Cédula:")
        correo = st.text_input("Correo Electrónico:")
        programa = st.selectbox("Programa de Interés:", [
            "Asistente Legal", 
            "Gestor Bancario", 
            "Contabilidad Técnica", 
            "Especialista en Procesos Industriales", 
            "Inglés"
        ])
        if st.form_submit_button("ENVIAR SOLICITUD"):
            if nombre and cedula:
                st.success(f"✅ ¡Gracias {nombre}! Hemos recibido su solicitud para el programa de {programa}.")
                st.balloons()
            else:
                st.error("Por favor, complete los campos obligatorios.")

# SECCIÓN: INFORMACIÓN (NOSOTROS)
elif opcion == "Información":
    st.header("Sobre el CETEP")
    col_inf1, col_inf2 = st.columns(2)
    with col_inf1:
        st.subheader("Nuestra Identidad")
        st.write("Somos una institución dedicada a la formación práctica y técnica.")
        st.markdown("📍 **Sede:** Heredia, Costa Rica")
        st.markdown("🕒 **Horarios:** Flexibles para trabajadores")
    
    with col_inf2:
        st.subheader("🤝 Convenios y Respaldo")
        st.write("Contamos con alianzas en el sector legal e industrial para facilitar las prácticas profesionales.")
    
    st.write("---")
    st.subheader("❓ Preguntas Frecuentes")
    with st.expander("¿Los cursos son certificados?"):
        st.write("Sí, todos nuestros programas emiten un certificado de aprovechamiento técnico.")
    with st.expander("¿Puedo pagar por tractos?"):
        st.write("Sí, contamos con planes de financiamiento interno y pago vía Sinpe Móvil.")

# SECCIÓN: CAMPUS VIRTUAL (ACCESO PRIVADO)
elif opcion == "Campus Virtual":
    st.markdown("<h2 style='text-align: center;'>🔐 Acceso Privado al Campus</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # Formulario de Login
    col_l1, col_l2, col_l3 = st.columns([1,2,1])
    with col_l2:
        st.info("Solo personal autorizado.")
        clave_input = st.text_input("Contraseña de Acceso:", type="password")
        if st.button("Iniciar Sesión"):
            clave_limpia = clave_input.strip()
            if clave_limpia == "admin_cetep":
                st.session_state["perfil"] = "admin"
            elif clave_limpia == "profe_cetep":
                st.session_state["perfil"] = "profe"
            else:
                st.error("Credenciales incorrectas")

    # Mostrar contenido según el perfil logueado
    if "perfil" in st.session_state:
        st.write("---")
        if st.session_state["perfil"] == "admin":
            st.subheader("📊 Panel de Dirección (Luis Varela)")
            menu_adm = st.selectbox("Herramientas:", ["Reportes Financieros", "Gestión de Matrícula"])
            if menu_adm == "Reportes Financieros":
                st.metric("Ingresos Mes Abril", "₡1,250,000", "+5%")
        
        elif st.session_state["perfil"] == "profe":
            st.subheader("👨‍🏫 Panel Docente")
            menu_doc = st.selectbox("Acciones:", ["Lista de Alumnos", "Registro de Notas"])
            if menu_doc == "Lista de Alumnos":
                st.write("Seleccione su grupo para ver la lista oficial.")
