import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CETEP - Plataforma Integral", layout="wide", page_icon="🎓")

# Estilo profesional
st.markdown("""
    <style>
    .titulo-principal { color: #002d5a; text-align: center; font-weight: bold; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    .seccion-info { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #004a99; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS EN SESIÓN (Para persistencia de datos)
if 'lista_alumnos' not in st.session_state:
    st.session_state['lista_alumnos'] = [
        {"Nombre": "Juan Pérez", "Cédula": "1-1111-1111", "Tel": "8630-0000", "Curso": "Asistente Legal"},
        {"Nombre": "Ana Mora", "Cédula": "2-2222-2222", "Tel": "7000-0000", "Curso": "Inglés"}
    ]

# 3. MENÚ LATERAL
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", ["Inicio", "Técnicos", "Inglés", "Prep. Colegio Abogados", "Matrícula", "Información", "Campus Virtual"])
    st.markdown("---")
    st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50686302333)")

# --- 4. SECCIÓN: INICIO ---
if opcion == "Inicio":
    st.markdown("<h1 class='titulo-principal'>CETEP: Formación Técnica Superior</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.write("### Excelencia Académica en Heredia")
    st.write("Líderes en capacitación técnica y profesional con enfoque en resultados laborales.")

# --- 5. SECCIÓN: TÉCNICOS ---
elif opcion == "Técnicos":
    st.header("Nuestros Programas Técnicos")
    t1, t2, t3, t4 = st.tabs(["⚖️ Asistente Legal", "🏦 Gestión Bancaria", "📊 Contabilidad", "⚙️ Procesos Industriales"])
    
    with t1:
        st.subheader("Técnico Superior en Asistente Legal")
        st.write("Módulos: Cobro Judicial, Prescripción, Derecho Notarial y Procesal.")
    with t2:
        st.subheader("Técnico en Gestión Bancaria Bilingüe")
        st.write("Módulos: Normativa SUGEF, Ley Bancaria y Operaciones de Caja.")
    with t3:
        st.subheader("Técnico en Contabilidad Técnica")
        st.write("Módulos: Ciclo Contable, Impuestos (ATV) y Planillas CCSS/INS.")
    with t4:
        st.subheader("Especialista en Procesos Industriales")
        st.write("Módulos: Calidad, Logística, Seguridad y Lean Manufacturing.")

# --- 6. SECCIÓN: INGLÉS (RESTAURADA) ---
elif opcion == "Inglés":
    st.header("Programa de Inglés")
    st.image("https://images.unsplash.com/photo-1543165796-5426273eaab3?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.subheader("Inglés Técnico y Conversacional")
    st.write("Enfoque práctico para el mundo de los negocios y servicios.")
    st.info("Niveles: Básico, Intermedio y Avanzado.")

# --- 7. SECCIÓN: PREPARACIÓN COLEGIO ABOGADOS (NUEVA) ---
elif opcion == "Prep. Colegio Abogados":
    st.header("Curso de Preparación para el Colegio de Abogados")
    st.write("Programa intensivo diseñado para el éxito en el Examen de Excelencia Académica.")
    st.markdown("""
    **Contenidos Principales:**
    * Derecho Civil y Mercantil.
    * Derecho Penal y Constitucional.
    * Ética Profesional y Ley Orgánica.
    * Simulacros de examen basados en jurisprudencia reciente de Costa Rica.
    """)
    st.warning("📅 Consulte por las próximas fechas de inicio para el bloque 2026.")

# --- 8. SECCIÓN: MATRÍCULA ---
elif opcion == "Matrícula":
    st.header("📝 Formulario de Matrícula")
    with st.form("form_mat"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nombre Completo:")
            ced = st.text_input("Cédula:")
        with col2:
            tel = st.text_input("Teléfono:")
            cur = st.selectbox("Programa:", ["Asistente Legal", "Bancario", "Contabilidad", "Industrial", "Inglés", "Prep. Colegio Abogados"])
        dir = st.text_area("Dirección:")
        if st.form_submit_button("Formalizar Matrícula"):
            if nom and ced and tel:
                st.session_state['lista_alumnos'].append({"Nombre": nom, "Cédula": ced, "Tel": tel, "Curso": cur})
                st.success(f"✅ ¡Registro completo para {nom}!")
            else:
                st.error("Campos obligatorios faltantes.")

# --- 9. SECCIÓN: INFORMACIÓN ---
elif opcion == "Información":
    st.header("Sobre el CETEP")
    st.markdown("<div class='seccion-info'><h3>Convenios y Ubicación</h3><p>Sede Heredia. Alianzas estratégicas con el sector legal e industrial.</p></div>", unsafe_allow_html=True)

# --- 10. SECCIÓN: CAMPUS VIRTUAL (DIRECTOR Y ESTUDIANTE) ---
elif opcion == "Campus Virtual":
    st.header("🔐 Acceso Privado")
    perfil = st.selectbox("Perfil:", ["Director", "Estudiante"])
    
    if perfil == "Director":
        if st.text_input("Clave Maestro:", type="password") == "admin_cetep":
            st.success("Panel Luis Varela")
            st.metric("Total Alumnos", len(st.session_state['lista_alumnos']))
            st.dataframe(pd.DataFrame(st.session_state['lista_alumnos']))

    elif perfil == "Estudiante":
        ced_log = st.text_input("Cédula:")
        if st.button("Ver Mi Progreso"):
            st.info("Cargando notas y temarios específicos...")
