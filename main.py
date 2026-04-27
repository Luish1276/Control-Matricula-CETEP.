import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILO "IPEA STYLE"
st.set_page_config(page_title="CETEP | Formación Técnica Profesional", layout="wide", page_icon="🎓")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700;800&display=swap');
    
    * { font-family: 'Poppins', sans-serif; }

    /* Hero Section Principal */
    .hero-full {
        background: linear-gradient(rgba(0,45,90,0.8), rgba(0,45,90,0.8)), 
                    url('https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=1920');
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        color: white;
        text-align: center;
        border-radius: 0px 0px 50px 50px;
        margin: -60px -20px 40px -20px;
    }
    
    .hero-title { font-size: 55px; font-weight: 800; margin-bottom: 10px; letter-spacing: -1px; }
    .hero-sub { font-size: 22px; font-weight: 300; margin-bottom: 30px; opacity: 0.9; }

    /* Tarjetas de Programas Estilo Moderno */
    .program-card {
        background: #ffffff;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #f0f0f0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
        text-align: center;
        height: 100%;
    }
    .program-card:hover { transform: translateY(-10px); border-color: #004a99; }
    
    .category-tag {
        background: #e3f2fd;
        color: #004a99;
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 15px;
    }

    .btn-matricula {
        background: #ffcc00;
        color: #002d5a;
        padding: 12px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        display: inline-block;
        margin-top: 20px;
    }
    
    .footer { text-align: center; padding: 40px; color: #666; font-size: 14px; border-top: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS MANTENIDA (Sin cambios en contenido)
PROGRAMAS = {
    "Técnico en Operaciones Bancarias": "6 Meses | Enfoque SUGEF",
    "Técnico Asistente Legal": "9 Meses | Procesal y Civil",
    "Gestión de Operaciones e Industria Médica": "9 Meses | Enfoque Coyol Free Zone",
    "Asistente Contable Administrativo": "9 Meses | Gestión Empresarial",
    "Inglés Global Conversacional": "12 Meses | Fluidez Profesional"
}

# 3. INTERFAZ
with st.sidebar:
    st.markdown("### 🛡️ CETEP ADMIN")
    nav = st.radio("Navegación Principal", ["⭐ Inicio", "📚 Programas", "📝 Matrícula", "🔐 Campus Virtual"])
    st.write("---")
    st.caption("Conectando talento con la industria costarricense.")

if nav == "⭐ Inicio":
    # HERO SECTION (Estilo IPEA)
    st.markdown("""
        <div class="hero-full">
            <h1 class="hero-title">IMPULSÁ TU FUTURO PROFESIONAL</h1>
            <p class="hero-sub">Técnicos especializados con alta demanda laboral en Costa Rica.</p>
            <a href="#" class="btn-matricula">VER TÉCNICOS DISPONIBLES</a>
        </div>
        """, unsafe_allow_html=True)
    
    # SECCIÓN DE VALORES
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="program-card">
                <div class="category-tag">100% Virtual</div>
                <h3>Clases en Vivo</h3>
                <p>Estudiá desde cualquier parte del país con horarios flexibles.</p>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="program-card">
                <div class="category-tag">Accesibilidad</div>
                <h3>Pagos Semanales</h3>
                <p>Modelo financiero diseñado para tu comodidad (Desde ₡5,000).</p>
            </div>
            """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="program-card">
                <div class="category-tag">Empleabilidad</div>
                <h3>Enfoque Industrial</h3>
                <p>Convenios y mallas curriculares alineadas a multinacionales.</p>
            </div>
            """, unsafe_allow_html=True)

elif nav == "📚 Programas":
    st.markdown("<h2 style='text-align:center;'>Nuestra Oferta Académica</h2>", unsafe_allow_html=True)
    for nombre, detalle in PROGRAMAS.items():
        with st.expander(f"📖 {nombre}"):
            st.write(f"**Duración:** {detalle}")
            st.button(f"Más información sobre {nombre}", key=nombre)

elif nav == "📝 Matrícula":
    st.markdown("## Proceso de Admisión 2026")
    with st.form("form_ipea"):
        st.text_input("Nombre Completo")
        st.text_input("Cédula de Identidad")
        st.selectbox("Programa de Interés", list(PROGRAMAS.keys()))
        st.selectbox("Horario", ["Mañana (9am-11am)", "Tarde (2pm-4pm)", "Noche (6pm-8pm)"])
        submitted = st.form_submit_button("¡SOLICITAR CUPO!")
        if submitted:
            st.success("Hemos recibido tu solicitud. Un asesor te contactará por WhatsApp.")

elif nav == "🔐 Campus Virtual":
    st.markdown("## Acceso a la Plataforma")
    st.text_input("Usuario")
    st.text_input("Contraseña", type="password")
    st.button("Entrar al Aula")

st.markdown("<div class='footer'>© 2026 CETEP | Centro de Estudios Técnicos Profesionales | Heredia, Costa Rica.</div>", unsafe_allow_html=True)
