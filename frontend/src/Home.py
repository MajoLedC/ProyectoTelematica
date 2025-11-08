import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Red Social Majito",
    layout="wide",
    page_icon="🐵"
)

# --- ENCABEZADO ---
st.title("Red Social - Majo App")
st.subheader("Comparte y descubre los chismes más salvajes de la jungla ")

st.markdown("---")

# --- BARRA LATERAL ---
st.sidebar.title("Menú")
opcion = st.sidebar.radio(
    "Navegar a:",
    ["Inicio", "Publicar", "Mi Perfil"]
)

# --- SECCIÓN PRINCIPAL ---
if opcion == "Inicio":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("Últimas Noticias")
        
        # Ejemplo de publicaciones simuladas
        posts = [
            {"usuario": "MonoLoco", "contenido": "¡Encontré una nueva cueva con bananas!", "fecha": "2025-10-27"},
            {"usuario": "BananaFan", "contenido": "¿Alguien más vio al gorila bailar?", "fecha": "2025-10-26"},
        ]
        
        for post in posts:
            st.markdown(f"**{post['usuario']}** 🍌 — *{post['fecha']}*")
            st.info(post["contenido"])
            st.markdown("---")

    with col2:
        st.markdown("Tendencias")
        st.write("🔥 Mono más popular: **MonoLoco**")
        st.write("🍌 Tema del día: *'Bananas brillantes'*")
        st.image("https://i.imgur.com/WxNkK3m.png", caption="Chisme del día", use_container_width=True)

elif opcion == "Publicar":
    st.markdown("### ✏️ Crear nueva publicación")

    usuario = st.text_input("Nombre del mono 🐒", "")
    contenido = st.text_area("¿Qué chisme quieres compartir? 🍌", "")

    if st.button("Publicar"):
        if usuario and contenido:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
            st.success(f"Publicación de **{usuario}** añadida con éxito 🐵 ({fecha})")
        else:
            st.error("Por favor, completa todos los campos.")

elif opcion == "Mi Perfil":
    st.markdown("### 👤 Perfil de usuario")
    st.image("https://i.imgur.com/l0yqI3G.png", width=150)
    st.write("**Nombre:** Mono Anónimo 🐒")
    st.write("**Nivel de Banana:** 🟡🟡🟡⚪⚪")
    st.write("**Publicaciones:** 12")
    st.write("**Miembro desde:** 2025")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("Creado con 🐒 por Majo App - 2025")
