import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN E IDENTIDAD
st.set_page_config(page_title="CETEP - Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    .main-title { color: #002d5a; text-align: center; font-weight: bold; font-size: 30px; }
    .card-academica { background-color: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 5px solid #004a99; margin-bottom: 10px; }
    .status-pagado { color: #2e7d32; font-weight: bold; }
    .status-pendiente { color: #d32f2f; font-weight: bold; }
    .footer-legal { text-align: center; font-size: 12px; color: #666; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS ACADÉMICA COMPLETA (RESTAURADA Y CORREGIDA)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses (Virtual)",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Plan": {
            "Mes 1-2": ["Introducción al Sistema Financiero", "Ética y Servicio al Cliente", "Matemática Financiera"],
            "Mes 3-4": ["Manejo de Efectivo y Títulos Valores", "Prevención de Fraude", "Detección de Billetaje"],
            "Mes 5-6": ["Normativa SUGEF y Cumplimiento", "Simulación de Arqueos", "Taller de Empleabilidad"]
        }
    },
    "Técnico Asistente Legal": {
        "D": "1 Año (Virtual)",
        "Inversion": "Consultar Plan",
        "Plan": {
            "I Cuatrimestre": ["Investigación Jurídica", "Informática Legal", "Redacción Documental", "IA Digital"],
            "II Cuatrimestre": ["Introducción al Derecho", "Derecho Civil", "Legislación Migratoria"],
            "III Cuatrimestre": ["Derecho Laboral", "Inmobiliario", "Familia", "Penal Aplicado"]
        }
    },
    "Técnico en Ingeniería Industrial": {
        "D": "9 Meses (Virtual)",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Módulo A": ["Gestión de Calidad", "Lean Manufacturing", "Logística"],
            "Módulo B": ["Seguridad Industrial", "Gestión de Proyectos", "Industria 4.0"],
            "Módulo C": ["Sostenibilidad", "Liderazgo", "Proyecto Integrador"]
        }
    },
    "Técnico en Contabilidad": { # RESTAURADO
        "D": "1 Año (Virtual)",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Bloque I": ["Contabilidad Básica e Intermedia", "Legislación Comercial", "Informática Contable"],
            "Bloque II": ["Legislación Tributaria (IVA/Renta)", "Costos e Inventarios", "Planillas y CCSS"],
            "Bloque III": ["Auditoría", "Análisis Financiero", "Ética Profesional"]
        }
    },
    "Inglés para Profesionales": { # RESTAURADO (El que faltaba)
        "D": "12 Meses (Virtual)",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Niveles Iniciales": ["Fonética y Pronunciación", "Gramática Esencial", "Inglés de Oficina"],
            "Niveles Medios": ["Business English", "Redacción Técnica", "Comunicación para Negocios"],
            "Niveles Superiores": ["Inglés Legal", "Negociación Internacional", "Certificación B2"]
        }
    },
    "Prep. Colegio de Abogados": {
        "D": "Curso Intensivo",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Ejes": ["Civil y Mercantil", "Penal y Familia", "Público y Constitucional", "Deontología Jurídica"]
        }
    }
}

# 3. PERSISTENCIA DE DATOS
if 'alumnos_db' not in st.session_state:
    st.session_state['alumnos_db'] = [
        {"Nombre": "Luis Varela", "Cédula": "1-0000-0000", "Curso": "Director", "Matricula": "PAGADA", "Semana_Actual": "Al día", "Saldo_Pendiente": 0}
    ]

# 4. NAVEGACIÓN
with st.sidebar:
    st.title("🛡️ Sistema CETEP")
    nav = st.radio("Menú Principal", ["Inicio", "Oferta Académica", "Matrícula", "Campus Virtual"])
    st.write("---")
    st.write("**Sede Central:** San José, Costa Rica")
    st.write("**Modalidad:** Virtual Nacional")

if nav == "Inicio":
    st.markdown("<h1 class='main-title'>CETEP: Formación Técnica Especializada</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&q=80&w=1200")
    st.info("💡 **MODELO ACCESIBLE:** Matrícula ₡10,000 y solo ₡5,000 por semana en banca.")
    
    st.write("### Horarios Disponibles (Modalidad Virtual):")
    c1, c2, c3 = st.columns(3)
    with c1: st.success("☀️ **Mañana:** 9am - 11am")
    with c2: st.success("⛅ **Tarde:** 2pm - 4pm")
    with c3: st.success("🌙 **Noche:** 6pm - 8pm")

elif nav == "Oferta Académica":
    st.header("Programas Técnicos Disponibles")
    cat = st.selectbox("Seleccione el programa:", list(OFFER_ACADEMICA.keys()))
    prog = OFFER_ACADEMICA[cat]
    st.write(f"**Duración:** {prog['D']}")
    st.write(f"**Inversión:** {prog['Inversion']}")
    for bloque, temas in prog['Plan'].items():
        st.subheader(bloque)
        for t in temas: st.markdown(f"<div class='card-academica'>🔹 {t}</div>", unsafe_allow_html=True)

elif nav == "Matrícula":
    st.header("📝 Registro de Estudiantes")
    with st.form("mat"):
        n = st.text_input("Nombre Completo:")
        c = st.text_input("Cédula:")
        cur = st.selectbox("Carrera:", list(OFFER_ACADEMICA.keys()))
        hor = st.selectbox("Horario:", ["Mañana (9-11 am)", "Tarde (2-4 pm)", "Noche (6-8 pm)"])
        if st.form_submit_button("Formalizar Matrícula"):
            if n and c:
                st.session_state['alumnos_db'].append({
                    "Nombre": n, "Cédula": c, "Curso": cur, "Horario": hor,
                    "Matricula": "PENDIENTE", "Semana_Actual": "PENDIENTE", "Saldo_Pendiente": 15000
                })
                st.success(f"¡Registro exitoso! Matrícula ₡10,000 + 1ra Semana ₡5,000.")

elif nav == "Campus Virtual":
    st.header("🔐 Acceso Académico")
    p = st.selectbox("Tipo de Usuario:", ["Director", "Estudiante"])
    if p == "Director":
        if st.text_input("Clave:", type="password") == "admin_cetep":
            st.success("Panel de Control: Luis Varela")
            st.dataframe(pd.DataFrame(st.session_state['alumnos_db']))
    elif p == "Estudiante":
        cl = st.text_input("Ingrese su Cédula:")
        if st.button("Consultar Estado"):
            alu = next((x for x in st.session_state['alumnos_db'] if x['Cédula'] == cl), None)
            if alu:
                st.subheader(f"Bienvenido, {alu['Nombre']}")
                st.metric("Saldo Pendiente", f"₡{alu['Saldo_Pendiente']}")
                if alu['Saldo_Pendiente'] > 10000:
                    st.error("⚠️ Acceso restringido. Favor ponerse al día.")
                else:
                    st.success("✅ Acceso habilitado.")

st.markdown("<div class='footer-legal'>© 2026 CETEP | Educación Accesible | Sede San José, Costa Rica.</div>", unsafe_allow_html=True)
