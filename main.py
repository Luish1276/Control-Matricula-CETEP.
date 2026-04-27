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
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS DEL SISTEMA (Persistencia en sesión)
if 'lista_alumnos' not in st.session_state:
    st.session_state['lista_alumnos'] = [
        {"Nombre": "Juan Pérez", "Cédula": "1-1111-1111", "Tel": "8630-0000", "Curso": "Asistente Legal", "Nota": 95},
        {"Nombre": "Ana Mora", "Cédula": "2-2222-2222", "Tel": "7000-0000", "Curso": "Prep. Colegio de Abogados", "Nota": 88}
    ]

# 3. MENÚ LATERAL
with st.sidebar:
    st.title("🛡️ CETEP")
    opcion = st.radio("Menú Principal", [
        "Inicio", "Técnicos", "Inglés", "Prep. Colegio de Abogados", "Matrícula", "Información", "Campus Virtual"
    ])
    st.markdown("---")
    st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50686302333)")

# --- SECCIONES INFORMATIVAS ---
if opcion == "Inicio":
    st.markdown("<h1 class='titulo-principal'>CETEP: Formación Técnica Superior</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)

elif opcion == "Técnicos":
    st.header("Programas Técnicos")
    t1, t2, t3, t4 = st.tabs(["⚖️ Asistente Legal", "🏦 Gestión Bancaria", "📊 Contabilidad", "⚙️ Procesos Industriales"])
    with t1: st.write("Especialista en Cobro Judicial, Prescripción y Derecho Notarial.")
    with t2: st.write("Normativa SUGEF y Operaciones Bancarias.")

elif opcion == "Inglés":
    st.header("Programa de Inglés Técnico")
    st.info("Enfoque conversacional para el éxito laboral.")

elif opcion == "Prep. Colegio de Abogados":
    st.header("Curso de Preparación: Examen de Excelencia Académica")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='bloque-derecho'><strong>⚖️ Civil y Mercantil</strong><br>Procesal Civil y Actos de Comercio.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>⚖️ Penal</strong><br>Procesal Penal y Sustantivo.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>⚖️ Familia</strong><br>Procesal de Familia.</div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='bloque-derecho'><strong>🏛️ Público</strong><br>Contencioso, Admin. Pública y Contratación.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>📜 Constitucional</strong><br>Jurisprudencia Constitucional.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>📕 Ética y Ley Orgánica</strong><br>Deontología jurídica.</div>", unsafe_allow_html=True)

elif opcion == "Matrícula":
    st.header("📝 Matrícula Oficial")
    with st.form("f_mat"):
        c1, c2 = st.columns(2)
        with c1:
            nom = st.text_input("Nombre:")
            ced = st.text_input("Cédula:")
        with c2:
            tel = st.text_input("Teléfono:")
            cur = st.selectbox("Curso:", ["Asistente Legal", "Bancario", "Contabilidad", "Industrial", "Inglés", "Prep. Colegio de Abogados"])
        if st.form_submit_button("Matricular"):
            st.session_state['lista_alumnos'].append({"Nombre": nom, "Cédula": ced, "Tel": tel, "Curso": cur, "Nota": 0})
            st.success("Registrado.")

# --- CAMPUS VIRTUAL (CONTROL TOTAL DIRECTOR) ---
elif opcion == "Campus Virtual":
    st.markdown("<h2 style='text-align: center;'>🔐 Acceso al Campus Virtual</h2>", unsafe_allow_html=True)
    perfil = st.selectbox("Ingresar como:", ["Director", "Profesor", "Estudiante"])
    
    if perfil == "Director":
        if st.text_input("Contraseña Maestro:", type="password") == "admin_cetep":
            st.success("👨‍⚖️ Panel de Control - Luis Varela")
            tab1, tab2, tab3 = st.tabs(["📊 Dashboard Financiero", "👥 Control de Alumnos", "🔎 Auditoría de Notas"])
            
            with tab1:
                st.metric("Ingresos Proyectados", "₡1,250,000")
                st.metric("Alumnos Inscritos", len(st.session_state['lista_alumnos']))
            
            with tab2:
                st.subheader("Base de Datos de Contacto")
                st.dataframe(pd.DataFrame(st.session_state['lista_alumnos'])[["Nombre", "Cédula", "Tel", "Curso"]], use_container_width=True)
                
            with tab3:
                st.subheader("Registro General de Calificaciones (Reclamos)")
                st.write("Historial completo para revisión de notas:")
                st.table(pd.DataFrame(st.session_state['lista_alumnos'])[["Nombre", "Curso", "Nota"]])

    elif perfil == "Profesor":
        if st.text_input("Contraseña Docente:", type="password") == "profe_cetep":
            st.success("Panel Docente")
            st.write("Registro de Actas.")

    elif perfil == "Estudiante":
        c_est = st.text_input("Cédula:")
        if st.button("Consultar"):
            st.table(pd.DataFrame([{"Módulo": "Módulo I", "Nota": 95}]))
