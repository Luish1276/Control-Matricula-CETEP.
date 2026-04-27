import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CETEP - Plataforma Integral", layout="wide", page_icon="🎓")

# Estilo profesional tipo IPEA
st.markdown("""
    <style>
    .titulo-principal { color: #002d5a; text-align: center; font-weight: bold; }
    .stTabs [aria-selected="true"] { background-color: #004a99; color: white; }
    .bloque-derecho { background-color: #f1f4f9; padding: 15px; border-radius: 8px; border-left: 5px solid #002d5a; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS EN SESIÓN
if 'lista_alumnos' not in st.session_state:
    st.session_state['lista_alumnos'] = [
        {"Nombre": "Juan Pérez", "Cédula": "1-1111-1111", "Tel": "8630-0000", "Curso": "Asistente Legal"},
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

# --- 4. SECCIONES INICIO, TÉCNICOS E INGLÉS ---
if opcion == "Inicio":
    st.markdown("<h1 class='titulo-principal'>CETEP: Formación Técnica Superior</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.write("### Excelencia Académica en Heredia")

elif opcion == "Técnicos":
    st.header("Programas Técnicos")
    t1, t2, t3, t4 = st.tabs(["⚖️ Asistente Legal", "🏦 Gestión Bancaria", "📊 Contabilidad", "⚙️ Procesos Industriales"])
    with t1: st.write("Enfoque en Cobro Judicial, Prescripción y Notariado.")
    with t2: st.write("Normativa SUGEF y Operaciones Bancarias.")
    with t3: st.write("Ciclo Contable y Tributación ATV.")
    with t4: st.write("Calidad y Lean Manufacturing.")

elif opcion == "Inglés":
    st.header("Programa de Inglés")
    st.image("https://images.unsplash.com/photo-1543165796-5426273eaab3?auto=format&fit=crop&q=80&w=1200", use_container_width=True)
    st.subheader("Inglés Técnico y Conversacional")

# --- 5. SECCIÓN: PREPARACIÓN COLEGIO DE ABOGADOS (DETALLADO) ---
elif opcion == "Prep. Colegio de Abogados":
    st.header("Curso de Preparación: Examen de Excelencia Académica")
    st.write("Programa de alto rendimiento enfocado en los ejes temáticos del Colegio de Abogados de Costa Rica.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='bloque-derecho'><strong>⚖️ Bloque Civil y Mercantil</strong><br>Derecho Sustantivo y Procesal Civil. Actos de comercio y sociedades.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>⚖️ Bloque Penal</strong><br>Derecho Penal Sustantivo y Procesal Penal.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>⚖️ Bloque de Familia</strong><br>Derecho de Familia y Procesal de Familia.</div>", unsafe_allow_html=True)
    
    with col_b:
        st.markdown("<div class='bloque-derecho'><strong>🏛️ Bloque Público</strong><br>Contencioso Administrativo, Administración Pública y Contratación Administrativa.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>📜 Bloque Constitucional</strong><br>Derecho de la Constitución y Jurisprudencia Constitucional.</div>", unsafe_allow_html=True)
        st.markdown("<div class='bloque-derecho'><strong>📕 Ética y Ley Orgánica</strong><br>Deontología jurídica y normativa del Colegio de Abogados.</div>", unsafe_allow_html=True)

# --- 6. MATRÍCULA Y CAMPUS ---
elif opcion == "Matrícula":
    st.header("📝 Matrícula")
    with st.form("f_mat"):
        n = st.text_input("Nombre:")
        c = st.text_input("Cédula:")
        t = st.text_input("Teléfono:")
        cur = st.selectbox("Curso:", ["Asistente Legal", "Bancario", "Contabilidad", "Industrial", "Inglés", "Prep. Colegio de Abogados"])
        if st.form_submit_button("Matricular"):
            st.session_state['lista_alumnos'].append({"Nombre": n, "Cédula": c, "Tel": t, "Curso": cur})
            st.success("Registrado.")

elif opcion == "Información":
    st.header("Información CETEP")
    st.info("Centro especializado en Heredia. Convenios con el sector legal.")

elif opcion == "Campus Virtual":
    st.header("🔐 Campus")
    p = st.selectbox("Perfil:", ["Director", "Estudiante"])
    if p == "Director":
        if st.text_input("Clave:", type="password") == "admin_cetep":
            st.dataframe(pd.DataFrame(st.session_state['lista_alumnos']))
    else:
        st.text_input("Cédula:")
        st.button("Ver Notas")
