import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CETEP - Gestión Integral", layout="wide", page_icon="🎓")

# Estilo profesional tipo IPEA
st.markdown("""
    <style>
    .titulo-principal { color: #002d5a; text-align: center; font-weight: bold; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    .bloque-derecho { background-color: #f1f4f9; padding: 15px; border-radius: 8px; border-left: 5px solid #002d5a; margin-bottom: 10px; }
    .metric-card { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. PERSISTENCIA DE DATOS (Base de datos en sesión)
if 'lista_alumnos' not in st.session_state:
    st.session_state['lista_alumnos'] = [
        {"Nombre": "Juan Pérez", "Cédula": "1-1111-1111", "Tel": "8630-0000", "Curso": "Asistente Legal"},
        {"Nombre": "Ana Mora", "Cédula": "2-2222-2222", "Tel": "7000-0000", "Curso": "Prep. Colegio de Abogados"}
    ]

# 3. MENÚ LATERAL
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", [
        "Inicio", 
        "Técnicos", 
        "Inglés", 
        "Prep. Colegio de Abogados", 
        "Matrícula", 
        "Información", 
        "Campus Virtual"
    ])
    st.markdown("---")
    st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50686302333)")

# --- SECCIONES DE INFORMACIÓN ---

if opcion == "Inicio":
    st.markdown("<h1 class='titulo-principal'>CETEP: Formación Técnica Superior</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.write("### Excelencia Académica y Profesional en Heredia")

elif opcion == "Técnicos":
    st.header("Programas Técnicos Disponibles")
    t1, t2, t3, t4 = st.tabs(["⚖️ Asistente Legal", "🏦 Gestión Bancaria", "📊 Contabilidad", "⚙️ Procesos Industriales"])
    with t1: st.write("Especialista en Cobro Judicial, Prescripción y Derecho Notarial.")
    with t2: st.write("Normativa SUGEF, Ley Bancaria y Operaciones de Caja.")
    with t3: st.write("Ciclo Contable, Impuestos (ATV) y Planillas.")
    with t4: st.write("Control de Calidad, Logística y Lean Manufacturing.")

elif opcion == "Inglés":
    st.header("Programa de Inglés Técnico y Conversacional")
    st.image("https://images.unsplash.com/photo-1543165796-5426273eaab3?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.info("Niveles: Básico, Intermedio y Avanzado. Enfoque en empleabilidad.")

elif opcion == "Prep. Colegio de Abogados":
    st.header("Curso de Preparación: Examen de Excelencia Académica")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='bloque-derecho'><strong>⚖️ Civil y Mercantil</strong><br>Sustantivo y Procesal Civil.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>⚖️ Penal</strong><br>Sustantivo y Procesal Penal.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>⚖️ Familia</strong><br>Sustantivo y Procesal de Familia.</div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='bloque-derecho'><strong>🏛️ Público</strong><br>Contencioso, Admin. Pública y Contratación.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>📜 Constitucional</strong><br>Derecho de la Constitución y Jurisprudencia.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>📕 Ética y Ley Orgánica</strong><br>Deontología jurídica.</div>", unsafe_allow_html=True)

elif opcion == "Matrícula":
    st.header("📝 Formulario de Matrícula Oficial")
    with st.form("f_mat"):
        c1, c2 = st.columns(2)
        with c1:
            nom = st.text_input("Nombre Completo:")
            ced = st.text_input("Número de Cédula:")
        with c2:
            tel = st.text_input("Número de Teléfono:")
            cur = st.selectbox("Programa:", ["Asistente Legal", "Bancario", "Contabilidad", "Industrial", "Inglés", "Prep. Colegio de Abogados"])
        dir = st.text_area("Dirección Exacta:")
        if st.form_submit_button("Formalizar Matrícula"):
            if nom and ced and tel:
                st.session_state['lista_alumnos'].append({"Nombre": nom, "Cédula": ced, "Tel": tel, "Curso": cur})
                st.success(f"✅ ¡Registro exitoso para {nom}!")
            else:
                st.error("Complete los campos obligatorios.")

elif opcion == "Información":
    st.header("Sobre el CETEP")
    st.info("Sede central en Heredia. Convenios con el sector legal e industrial.")

# --- CAMPUS VIRTUAL (RESTAURADO AL 100%) ---
elif opcion == "Campus Virtual":
    st.markdown("<h2 style='text-align: center;'>🔐 Acceso al Campus Virtual</h2>", unsafe_allow_html=True)
    perfil = st.selectbox("Ingresar como:", ["Director", "Profesor", "Estudiante"])
    
    if perfil == "Director":
        clave_adm = st.text_input("Contraseña Maestro:", type="password")
        if clave_adm == "admin_cetep":
            st.success(f"Bienvenido, Luis Varela")
            t_adm1, t_adm2 = st.tabs(["📊 Dashboard y Finanzas", "👥 Control de Alumnos"])
            with t_adm1:
                col_f1, col_f2 = st.columns(2)
                with col_f1:
                    st.metric("Ingresos Proyectados", "₡1,250,000")
                with col_f2:
                    st.metric("Total de Alumnos", len(st.session_state['lista_alumnos']))
            with t_adm2:
                st.subheader("Lista de Matrícula Activa")
                st.dataframe(pd.DataFrame(st.session_state['lista_alumnos']), use_container_width=True)

    elif perfil == "Profesor":
        clave_pro = st.text_input("Contraseña Docente:", type="password")
        if clave_pro == "profe_cetep":
            st.success("Panel Docente Activo")
            st.subheader("Registro de Calificaciones")
            st.selectbox("Seleccione Grupo:", ["Asistente Legal", "Bancario", "Inglés", "Prep. Colegio de Abogados"])
            st.number_input("Nota del Estudiante:", 0, 100)
            st.button("Subir Nota al Sistema")

    elif perfil == "Estudiante":
        ced_log = st.text_input("Número de Cédula:", placeholder="1-1111-1111")
        if st.button("Consultar Mi Perfil"):
            st.info("Mostrando Notas y Temario del Estudiante...")
            st.table(pd.DataFrame([{"Materia": "Módulo I", "Nota": 95, "Estado": "Aprobado"}]))
