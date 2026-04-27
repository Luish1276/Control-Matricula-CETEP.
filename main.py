import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN E IDENTIDAD
st.set_page_config(page_title="CETEP - Campus Virtual", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    .main-title { color: #002d5a; text-align: center; font-weight: bold; font-size: 30px; }
    .card-academica { background-color: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 5px solid #004a99; margin-bottom: 10px; }
    .footer-legal { text-align: center; font-size: 12px; color: #666; margin-top: 50px; }
    .metrica-card { background-color: #e3f2fd; border: 1px solid #2196f3; padding: 10px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS ACADÉMICA (Actualizada: Del Aula al Coyol)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": {
        "D": "6 Meses (Virtual)",
        "Inversion": "Matrícula ₡10,000 / Semanal ₡5,000",
        "Plan": {
            "Mes 1-2": ["Sistemas Financieros", "Ética Bancaria", "Matemática"],
            "Mes 3-4": ["Manejo de Efectivo", "Prevención de Fraude", "Billetaje"],
            "Mes 5-6": ["SUGEF", "Simulación de Arqueos", "Empleabilidad"]
        }
    },
    "Técnico Asistente Legal": {
        "D": "9 Meses (Virtual)",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Trimestre I": ["Investigación Jurídica", "Informática Legal", "Redacción", "IA Digital"],
            "Trimestre II": ["Derecho Civil", "Legislación Migratoria", "Ética Jurídica"],
            "Trimestre III": ["Derecho Laboral", "Inmobiliario y Familia", "Penal Aplicado"]
        }
    },
    "Asistente Contable y Gestión Administrativa": {
        "D": "9 Meses (Virtual)",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Trimestre I": ["Principios Contables", "Legislación Comercial", "Gestión Documental"],
            "Trimestre II": ["Costos", "Excel Avanzado", "Legislación Tributaria"],
            "Trimestre III": ["Planillas y CCSS", "Análisis Financiero", "Ética"]
        }
    },
    "Gestión de Operaciones e Industria Médica": { # ENFOQUE "DEL AULA AL COYOL"
        "D": "9 Meses (Virtual)",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Trimestre I: Calidad y Cumplimiento": [
                "Introducción a la Industria de Dispositivos Médicos", 
                "GDP: Buenas Prácticas de Documentación (Llenado de bitácoras)", 
                "Metrología e Instrumentación (Uso de Vernier y Micrómetro)",
                "Normativa ISO 13485: Fundamentos de Calidad"
            ],
            "Trimestre II: Procesos y Cuartos Limpios": [
                "Protocolos de Cuarto Limpio (Microbiología y Vestimenta)", 
                "Lean Manufacturing (5S, Kaizen y eliminación de desperdicios)", 
                "Seguridad Industrial y Salud Ocupacional (SISO)",
                "Lectura de Planos e Instrucciones de Trabajo (OI)"
            ],
            "Trimestre III: Entrenamiento de Inserción (El Coyol)": [
                "Entrenamiento en Pruebas Métricas (Matemática y Lógica)", 
                "Preparación de Currículum para Multinacionales", 
                "Simulacro de Entrevistas bajo el Método STAR",
                "Taller de Destreza Motora y Precisión"
            ]
        }
    },
    "Inglés Global Conversacional": {
        "D": "12 Meses (Virtual)",
        "Inversion": "Consultar Plan",
        "Plan": {
            "Básico": ["Fonética", "Gramática", "Vocabulario"],
            "Intermedio": ["Lectura", "Redacción", "Conversación"],
            "Avanzado": ["Inglés Técnico", "Entrevistas", "Certificación"]
        }
    },
    "Prep. Colegio de Abogados": {
        "D": "Curso Intensivo",
        "Inversion": "Consultar Plan",
        "Plan": { "Ejes": ["Civil/Mercantil", "Penal/Familia", "Público", "Deontología"] }
    }
}

# 3. PERSISTENCIA DE DATOS
if 'alumnos_db' not in st.session_state:
    st.session_state['alumnos_db'] = [{"Nombre": "Luis Varela", "Cédula": "1-0000-0000", "Curso": "Director", "Saldo_Pendiente": 0}]

# 4. NAVEGACIÓN
with st.sidebar:
    st.title("🛡️ Sistema CETEP")
    nav = st.sidebar.radio("Menú Principal", ["Inicio", "Oferta Académica", "Matrícula", "Campus Virtual"])
    st.write("---")
    st.write("**Sede Central:** San José")

if nav == "Inicio":
    st.markdown("<h1 class='main-title'>CETEP: Formación de Alto Nivel</h1>", unsafe_allow_html=True)
    st.info("🚀 **PROYECTO DEL AULA AL COYOL:** Te preparamos para entrar a las mejores multinacionales de dispositivos médicos.")
    st.write("### Horarios Disponibles:")
    c1, c2, c3 = st.columns(3)
    with c1: st.success("☀️ 9:00 am - 11:00 am")
    with c2: st.success("⛅ 2:00 pm - 4:00 pm")
    with c3: st.success("🌙 6:00 pm - 8:00 pm")

elif nav == "Oferta Académica":
    st.header("Mallas Curriculares Actualizadas")
    cat = st.selectbox("Seleccione el programa:", list(OFFER_ACADEMICA.keys()))
    prog = OFFER_ACADEMICA[cat]
    st.write(f"**Duración:** {prog['D']}")
    for bloque, temas in prog['Plan'].items():
        st.subheader(bloque)
        for t in temas: st.markdown(f"<div class='card-academica'>🔹 {t}</div>", unsafe_allow_html=True)

elif nav == "Matrícula":
    st.header("📝 Formulario de Matrícula")
    with st.form("mat"):
        n, c = st.text_input("Nombre Completo:"), st.text_input("Cédula:")
        cur = st.selectbox("Carrera de Interés:", list(OFFER_ACADEMICA.keys()))
        hor = st.selectbox("Horario:", ["Mañana", "Tarde", "Noche"])
        if st.form_submit_button("Registrar Estudiante"):
            if n and c:
                st.session_state['alumnos_db'].append({"Nombre": n, "Cédula": c, "Curso": cur, "Saldo_Pendiente": 15000})
                st.success("¡Registro Exitoso!")

elif nav == "Campus Virtual":
    st.header("🔐 Acceso Académico")
    p = st.selectbox("Perfil:", ["Director", "Estudiante"])
    if p == "Director" and st.text_input("Clave:", type="password") == "admin_cetep":
        st.dataframe(pd.DataFrame(st.session_state['alumnos_db']))
    elif p == "Estudiante":
        cl = st.text_input("Cédula:")
        if st.button("Consultar Estado Académico"):
            alu = next((x for x in st.session_state['alumnos_db'] if x['Cédula'] == cl), None)
            if alu:
                st.write(f"Bienvenido: {alu['Nombre']}")
                if alu['Curso'] == "Gestión de Operaciones e Industria Médica":
                    st.markdown("<div class='metrica-card'>📊 **PRÓXIMA EVALUACIÓN:** Simulacro de Prueba Métrica (Matemática para Multinacionales)</div>", unsafe_allow_html=True)
                st.write(f"Estado de Cuenta: {'✅ Activo' if alu['Saldo_Pendiente'] <= 10000 else '⚠️ Contactar a Administración'}")

st.markdown("<div class='footer-legal'>© 2026 CETEP | Sede San José, Costa Rica.</div>", unsafe_allow_html=True)
