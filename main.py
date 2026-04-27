import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CETEP - Gestión Académica", layout="wide", page_icon="🎓")

# Estilos profesionales (Azul IPEA)
st.markdown("""
    <style>
    .titulo-principal { color: #002d5a; text-align: center; font-weight: bold; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    .bloque-temario { background-color: #f8f9fa; padding: 12px; border-radius: 8px; border-left: 5px solid #004a99; margin-bottom: 8px; font-size: 14px; }
    .header-bloque { color: #004a99; font-weight: bold; margin-top: 15px; border-bottom: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS DE TEMARIOS (Cargada de tus documentos)
TEMARIOS = {
    "Asistente Legal": {
        "Plan": {
            "I Cuatrimestre": ["Métodos de Investigación jurídica y procedimientos", "Paquete de cómputo para la oficina legal", "Redacción de Documentos Jurídicos", "Inteligencia artificial y herramientas digitales"],
            "II Cuatrimestre": ["Servicio al Cliente y Ética profesional", "Introducción al Derecho", "Derecho Civil (Obligaciones y Responsabilidades)", "Legislación Migratoria y procedimientos"],
            "III Cuatrimestre": ["Legislación Laboral (Conflictos y resoluciones)", "Derecho Inmobiliario", "Generalidades del Derecho de Familia", "Aplicaciones del Derecho Penal"]
        }
    },
    "Cajero Bancario": {
        "Plan": {
            "Mes 1": ["Fundamentos Bancarios", "Matemáticas Financieras", "Servicio al Cliente", "Ética y Conducta"],
            "Mes 2": ["Manejo de Efectivo", "Operaciones de Caja", "Seguridad y Prevención de Fraude"],
            "Mes 3": ["Antilavado (PLD/FT)", "KYC (Know Your Customer)", "Banca Digital y E-Banking"],
            "Mes 4": ["Taller de Empleabilidad", "Simulación de Escenarios", "Práctica Profesional"]
        }
    },
    "Ingeniería Industrial": {
        "Plan": {
            "Mes 1-3": ["Fundamentos y Productividad", "Gestión de la Calidad (Lean Manufacturing/5S)", "Logística y Cadena de Suministro"],
            "Mes 4-6": ["Seguridad Industrial", "Mantenimiento", "Gestión de Proyectos", "Digitalización (IoT)"],
            "Mes 7-9": ["Sostenibilidad y Economía Circular", "Software Especializado (MS Project)", "Liderazgo", "Proyecto Integrador"]
        }
    },
    "Contabilidad": {
        "Plan": {
            "Bloque I": ["Contabilidad Básica I", "Legislación Comercial", "Matemática Financiera", "Informática Contable"],
            "Bloque II": ["Contabilidad Intermedia", "Legislación Tributaria (IVA e Impuesto sobre la Renta)", "Costos Industriales", "Planillas y Seguridad Social (CCSS/INS)"],
            "Bloque III": ["Auditoría y Control Interno", "Análisis de Estados Financieros", "Ética Profesional Contable", "Sistemas de Información Contable"]
        }
    }
}

# 3. PERSISTENCIA DE DATOS
if 'lista_alumnos' not in st.session_state:
    st.session_state['lista_alumnos'] = [
        {"Nombre": "Juan Pérez", "Cédula": "1-1111-1111", "Tel": "8630-0000", "Curso": "Asistente Legal", "Nota": 95},
        {"Nombre": "Dra. Mora", "Cédula": "2-2222-2222", "Tel": "7000-0000", "Curso": "Prep. Colegio de Abogados", "Nota": 88}
    ]

# 4. MENÚ LATERAL
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", ["Inicio", "Técnicos", "Inglés", "Prep. Colegio de Abogados", "Matrícula", "Información", "Campus Virtual"])
    st.markdown("---")
    st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50686302333)")

# --- SECCIONES DE INFORMACIÓN ---
if opcion == "Inicio":
    st.markdown("<h1 class='titulo-principal'>CETEP: Formación Técnica Superior</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)

elif opcion == "Técnicos":
    st.header("Programas Técnicos Superiores")
    seleccion = st.selectbox("Seleccione para ver temario:", list(TEMARIOS.keys()))
    info = TEMARIOS[seleccion]
    for bloque, materias in info['Plan'].items():
        st.markdown(f"<div class='header-bloque'>{bloque}</div>", unsafe_allow_html=True)
        for m in materias:
            st.markdown(f"<div class='bloque-temario'>🔹 {m}</div>", unsafe_allow_html=True)

elif opcion == "Inglés":
    st.header("Programa de Inglés Técnico y Conversacional")
    st.info("Desarrollo de fluidez verbal y escrita para entornos profesionales.")

elif opcion == "Prep. Colegio de Abogados":
    st.header("Curso de Preparación: Examen de Excelencia Académica")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='bloque-temario'><strong>⚖️ Civil y Mercantil</strong><br>Sustantivo y Procesal Civil.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-temario'><strong>⚖️ Penal</strong><br>Sustantivo y Procesal Penal.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-temario'><strong>⚖️ Familia</strong><br>Derecho de Familia y Procesal de Familia.</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='bloque-temario'><strong>🏛️ Público</strong><br>Contencioso, Admin. Pública y Contratación.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-temario'><strong>📜 Constitucional</strong><br>Jurisprudencia y Derecho de la Constitución.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-temario'><strong>📕 Ética y Ley Orgánica</strong><br>Deontología jurídica y normativa profesional.</div>", unsafe_allow_html=True)

elif opcion == "Matrícula":
    st.header("📝 Matrícula")
    with st.form("f_mat"):
        col1, col2 = st.columns(2)
        nom_m = col1.text_input("Nombre:")
        ced_m = col1.text_input("Cédula:")
        tel_m = col2.text_input("Teléfono:")
        cur_m = col2.selectbox("Curso:", list(TEMARIOS.keys()) + ["Inglés", "Prep. Colegio de Abogados"])
        if st.form_submit_button("Registrar Alumno"):
            st.session_state['lista_alumnos'].append({"Nombre": nom_m, "Cédula": ced_m, "Tel": tel_m, "Curso": cur_m, "Nota": 0})
            st.success("Matrícula Guardada.")

# --- CAMPUS VIRTUAL (CONTROL TOTAL) ---
elif opcion == "Campus Virtual":
    st.header("🔐 Acceso")
    perfil = st.selectbox("Perfil:", ["Director", "Profesor", "Estudiante"])
    
    if perfil == "Director":
        if st.text_input("Contraseña Maestro:", type="password") == "admin_cetep":
            st.success("Acceso Director: Luis Varela")
            t1, t2, t3 = st.tabs(["📊 Dashboard Financiero", "👥 Alumnos", "🔎 Auditoría de Notas"])
            with t1:
                st.metric("Ingresos Proyectados", "₡1,250,000")
                st.metric("Matrícula Total", len(st.session_state['lista_alumnos']))
            with t2:
                st.dataframe(pd.DataFrame(st.session_state['lista_alumnos'])[["Nombre", "Cédula", "Tel", "Curso"]])
            with t3:
                st.subheader("Cuadro de Calificaciones General")
                st.table(pd.DataFrame(st.session_state['lista_alumnos'])[["Nombre", "Curso", "Nota"]])

    elif perfil == "Profesor":
        if st.text_input("Clave Profe:", type="password") == "profe_cetep":
            st.success("Panel Docente Activo")
            st.selectbox("Grupo:", ["Legal", "Banca", "Abogados"])
            st.number_input("Nota:", 0, 100)
            st.button("Guardar Nota")

    elif perfil == "Estudiante":
        ced_l = st.text_input("Cédula:")
        if st.button("Ingresar"):
            alumno = next((a for a in st.session_state['lista_alumnos'] if a['Cédula'] == ced_l), None)
            if alumno:
                st.subheader(f"Bienvenido, {alumno['Nombre']}")
                tab_n, tab_t = st.tabs(["📊 Mis Notas", "📖 Mi Temario"])
                with tab_n:
                    st.metric("Promedio Actual", alumno['Nota'])
                with tab_t:
                    if alumno['Curso'] in TEMARIOS:
                        for b, ms in TEMARIOS[alumno['Curso']]['Plan'].items():
                            st.write(f"**{b}:**")
                            for m in ms: st.write(f"- {m}")
                    else: st.write("Contenido disponible en sede.")
