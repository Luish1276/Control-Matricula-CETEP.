# --- 5. INFORMACIÓN (ACTUALIZADA CON CONVENIOS Y FAQ) ---
elif opcion == "Información":
    st.header("Sobre el CETEP")
    
    col_inf1, col_inf2 = st.columns(2)
    with col_inf1:
        st.subheader("Nuestra Identidad")
        st.write("Somos un centro de formación técnica especializado en la empleabilidad rápida.")
        st.markdown("✅ **Sede:** Heredia, Costa Rica")
        st.markdown("✅ **Horarios:** Sabatinos y Nocturnos")
    
    with col_inf2:
        st.subheader("🤝 Alianzas Estratégicas")
        st.write("Nuestros estudiantes cuentan con opciones de práctica en:")
        st.info("Despachos Legales - Entidades Financieras - Plantas Industriales")

    st.write("---")
    st.subheader("❓ Preguntas Frecuentes")
    with st.expander("¿Cuáles son los requisitos de ingreso?"):
        st.write("Cédula de identidad y título de noveno año o bachillerato (según el técnico).")
    with st.expander("¿Cuáles son los métodos de pago?"):
        st.write("Aceptamos transferencia bancaria, Sinpe Móvil y pagos con tarjeta en el Campus Virtual.")

# --- BOTÓN DE CONTACTO EN LA BARRA LATERAL ---
st.sidebar.markdown("---")
st.sidebar.subheader("📱 Soporte Inmediato")
# Sustituye el número por el tuyo real
st.sidebar.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contactar-green?style=for-the-badge&logo=whatsapp)](https://wa.me/50680000000)")
