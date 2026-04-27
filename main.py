import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA E IDENTIDAD VISUAL
st.set_page_config(page_title="CETEP - Campus Virtual Nacional", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    .main-title { color: #002d5a; text-align: center; font-weight: bold; font-size: 32px; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    .card-academica { background-color: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 5px solid #004a99; margin-bottom: 10px; }
    .footer-legal { text-align: center; font-size: 12px; color: #666; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS ESTRUCTURADA (CETEP VIRTUAL CR)
OFFER_ACADEMICA = {
    "Asistente Legal": {
        "D": "1 Año (Virtual)",
        "Plan": {
            "I Cuatrimestre": ["Investigación Jurídica y Procedimientos", "Informática para la Oficina Legal", "Redacción Jurídica Profesional", "IA Aplicada al Derecho"],
            "II Cuatrimestre": ["Servicio al Cliente y Ética", "Introducción al Derecho", "Derecho Civil (Obligaciones)", "Legislación Migratoria"],
            "III Cuatrimestre": ["Legislación Laboral", "Derecho Inmobiliario", "Derecho de Familia", "Práctica Procesal Penal"]
        }
    },
    "Cajero Bancario": {
        "D": "4 Meses (Intensivo Virtual)",
        "Plan": {
            "Etapa 1": ["Fundamentos Bancarios", "Matemática Financiera Aplicada", "Protocolos de Servicio y Ética"],
            "Etapa 2": ["Manejo de Efectivo", "Seguridad Bancaria y Prevención de Fraude", "Normativa SUGEF y Antilavado"],
            "Etapa 3": ["Banca Digital (E-Banking)", "Habilidades para la Empleabilidad", "Simulación de Escenarios Reales"]
        }
    },
    "Ingeniería Industrial": {
        "D": "9 Meses (Virtual)",
        "Plan": {
            "Módulo Calidad": ["Optimización de Procesos", "Lean Manufacturing y 5S", "Logística y Suministros"],
            "Módulo Técnico": ["Seguridad Industrial", "Gestión de Proyectos (MS Project)", "Industria 4.0 e IoT"],
            "Módulo Estratégico": ["Sostenibilidad Ambiental", "Liderazgo de Equipos", "Proyecto Integrador Final"]
        }
    },
    "Contabilidad Técnica": {
        "D": "1 Año (Virtual)",
        "Plan": {
            "Bloque A": ["Contabilidad Básica e Intermedia", "Legislación Comercial", "Matemática Financiera"],
            "Bloque B": ["Tributación Costa Rica (IVA/Renta)", "Costos y Presupuestos", "Planillas y Seguridad Social"],
            "Bloque C": ["Auditoría y Control Interno", "Análisis Financiero", "Ética y Software Contable"]
        }
    },
    "Inglés Profesional (Bilingüe)": {
        "D": "12 Meses (Virtual)",
        "Plan": {
            "Nivel A1-A2": ["Fonética y Pronunciación", "Estructuras Gramaticales Esenciales", "Vocabulario de Oficina"],
            "Nivel B1": ["Business Correspondence (Correos/Reportes)", "Inglés para Negociaciones", "Lectura Técnica"],
            "Nivel B2": ["Inglés Legal y Contractual", "Debates y Liderazgo", "Preparación para Certificación TOEIC"]
        }
    },
    "Prep. Colegio de Abogados": {
        "D": "Ciclo Intensivo (Virtual)",
        "Plan": {
            "Eje Privado": ["Procesal Civil", "Derecho Mercantil", "Procesal de Familia"],
            "Eje Público": ["Contencioso Administrativo", "Administración Pública", "Contratación Administrativa"],
            "Eje Penal/Const.": ["Procesal Penal", "Jurisprudencia Constitucional", "Ética y Ley Orgánica"]
        }
    }
}

# 3. PERSISTENCIA DE DATOS
if 'alumnos_db' not in st.session_state:
    st.session_state['alumnos_db'] = [
        {"Nombre": "Luis Varela", "Cédula": "1-0000-0000", "Curso": "Prep. Colegio de Abogados", "Nota": 100}
    ]

# 4. NAVEGACIÓN
with st.sidebar:
    st.title("🛡️ Panel CETEP")
    nav = st.radio("Secciones", ["Inicio", "Oferta Académica", "Matrícula", "Campus Virtual"])
    st.markdown("---")
    st.write("**Sede Central:** San José, Costa Rica")
    st.write("**Alcance:** Cobertura Nacional (Virtual)")

if nav == "Inicio":
    st.markdown("<h1 class='main-title'>CETEP: Formación de Excelencia para toda Costa Rica</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1523240715634-d9c2ae919f6e?auto=format&fit=crop&q=80&w=1200")
    st.write("### Capacitación técnica de alto nivel desde San José para todo el país.")

elif nav == "Oferta Académica":
    st.header("Programas Técnicos Virtuales")
    cat = st.selectbox("Seleccione una carrera:", list(OFFER_ACADEMICA.keys()))
    prog = OFFER_ACADEMICA[cat]
    st.write(f"**Duración:** {prog['D']}")
    for bloque, temas in prog['Plan'].items():
        st.subheader(bloque)
        for t in temas: st.markdown(f"<div class='card-academica'>🔹 {t}</div>", unsafe_allow_html=True)

elif nav == "Matrícula":
    st.header("📝 Matrícula Abierta - Costa Rica")
    with st.form("mat_form"):
        c1, c2 = st.columns(2)
        n = c1.text_input("Nombre Completo:")
        ced = c1.text_input("Cédula:")
        cur = c2.selectbox("Elegir Programa:", list(OFFER_ACADEMICA.keys()))
        if st.form_submit_button("Formalizar Registro"):
            if n and ced:
                st.session_state['alumnos_db'].append({"Nombre": n, "Cédula": ced, "Curso": cur, "Nota": 0})
                st.success("Alumno matriculado correctamente en la modalidad virtual.")
            else:
                st.error("Por favor complete nombre y cédula.")

elif nav == "Campus Virtual":
    st.header("🔐 Acceso Autorizado")
    perfil = st.selectbox("Perfil:", ["Director", "Profesor", "Estudiante"])
    
    if perfil == "Director":
        if st.text_input("Clave Maestro:", type="password") == "admin_cetep":
            st.success("Acceso Director: Luis Varela")
            t1, t2 = st.tabs(["📊 Dashboard de Gestión", "🔎 Auditoría de Notas"])
            with t1:
                st.metric("Matrícula Total CR", len(st.session_state['alumnos_db']))
                st.dataframe(pd.DataFrame(st.session_state['alumnos_db']))
            with t2:
                st.subheader("Control de Calificaciones para Reclamos")
                st.table(pd.DataFrame(st.session_state['alumnos_db'])[["Nombre", "Curso", "Nota"]])
    
    elif perfil == "Estudiante":
        cl = st.text_input("Cédula:")
        if st.button("Consultar Mi Perfil"):
            alu = next((x for x in st.session_state['alumnos_db'] if x['Cédula'] == cl), None)
            if alu:
                st.subheader(f"Hola, {alu['Nombre']}")
                st.metric("Mi Nota Actual", alu['Nota'])
                st.info(f"Carrera Virtual: {alu['Curso']}")
            else:
                st.error("Cédula no encontrada en el padrón nacional de CETEP.")

st.markdown("<div class='footer-legal'>© 2026 CETEP Costa Rica | Sede Central San José | Educación Virtual de Alcance Nacional.</div>", unsafe_allow_html=True)
