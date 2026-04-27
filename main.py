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

# 2. BASE DE DATOS ACADÉMICA (Manteniendo todo lo construido)
OFFER_ACADEMICA = {
    "Técnico en Operaciones Bancarias y Gestión de Efectivo": { # NOMBRE ACTUALIZADO
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
    }
}

# 3. PERSISTENCIA DE DATOS (Simulación de DB)
if 'alumnos_db' not in st.session_state:
    # Estado inicial: Luis como Director y un ejemplo de alumno con pagos
    st.session_state['alumnos_db'] = [
        {
            "Nombre": "Luis Varela", 
            "Cédula": "1-0000-0000", 
            "Curso": "Director", 
            "Matricula": "PAGADA",
            "Semana_Actual": "Al día",
            "Saldo_Pendiente": 0
        },
        {
            "Nombre": "Estudiante Ejemplo", 
            "Cédula": "1-1111-1111", 
            "Curso": "Técnico en Operaciones Bancarias y Gestión de Efectivo", 
            "Matricula": "PAGADA",
            "Semana_Actual": "PENDIENTE",
            "Saldo_Pendiente": 5000
        }
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
    st.info("💡 **NUEVO MODELO DE PAGO:** Matrícula ₡10,000 y solo ₡5,000 por semana.")

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
    st.write("Inicie su carrera con una inversión accesible.")
    with st.form("mat"):
        n = st.text_input("Nombre Completo:")
        c = st.text_input("Cédula:")
        cur = st.selectbox("Carrera:", list(OFFER_ACADEMICA.keys()))
        horario = st.selectbox("Horario deseado:", ["Mañana (9-11 am)", "Noche (6-8 pm)"])
        if st.form_submit_button("Formalizar Matrícula"):
            if n and c:
                st.session_state['alumnos_db'].append({
                    "Nombre": n, "Cédula": c, "Curso": cur, 
                    "Matricula": "PENDIENTE", "Semana_Actual": "PENDIENTE", "Saldo_Pendiente": 15000
                })
                st.success(f"¡Registro exitoso! Por favor proceda al pago de la matrícula (₡10,000) y su primer semana (₡5,000).")
            else:
                st.error("Por favor complete todos los datos.")

elif nav == "Campus Virtual":
    st.header("🔐 Acceso Académico y Financiero")
    p = st.selectbox("Tipo de Usuario:", ["Director", "Estudiante"])
    
    if p == "Director":
        if st.text_input("Clave de Acceso:", type="password") == "admin_cetep":
            st.success("Panel de Control: Luis Varela")
            st.write("### Control de Cobros y Estudiantes")
            df = pd.DataFrame(st.session_state['alumnos_db'])
            st.dataframe(df)
            
    elif p == "Estudiante":
        cl = st.text_input("Ingrese su Cédula:")
        if st.button("Consultar Mi Estado"):
            alu = next((x for x in st.session_state['alumnos_db'] if x['Cédula'] == cl), None)
            if alu:
                st.subheader(f"Bienvenido, {alu['Nombre']}")
                c1, c2 = st.columns(2)
                with c1:
                    st.write("**Curso:**", alu['Curso'])
                    st.write("**Matrícula:**", alu['Matricula'])
                with c2:
                    st.write("**Semana Actual:**", alu['Semana_Actual'])
                    st.metric("Saldo Pendiente", f"₡{alu['Saldo_Pendiente']}")
                
                if alu['Saldo_Pendiente'] > 10000:
                    st.error("⚠️ Su acceso a lecciones está en riesgo de suspensión. Favor ponerse al día.")
                else:
                    st.success("✅ Acceso habilitado a clases virtuales.")
            else:
                st.error("Cédula no registrada.")

st.markdown("<div class='footer-legal'>© 2026 CETEP | Educación Accesible | Sede San José, Costa Rica.</div>", unsafe_allow_html=True)
