import streamlit as st

st.set_page_config(page_title="Registro ", layout="centered")

if "usuarios" not in st.session_state:
    st.session_state.usuarios = {}

st.title("Registro de nuevo usuario")
st.subheader("Crea tu cuenta para unirte a la jungla!")

nuevo_usuario = st.text_input("Nuevo usuario")
nueva_contraseña = st.text_input("Contraseña", type="password")
confirmar = st.text_input("Confirmar contraseña", type="password")

if st.button("Crear cuenta", key="crear"):
    if nuevo_usuario in st.session_state.usuarios:
        st.error("Ese nombre de usuario ya existe")
    elif nueva_contraseña != confirmar:
        st.error("Las contraseñas no coinciden")
    elif nuevo_usuario == "" or nueva_contraseña == "":
        st.warning("Por favor completa todos los campos.")
    else:
        st.session_state.usuarios[nuevo_usuario] = nueva_contraseña
        st.success(f"¡Cuenta creada con éxito, {nuevo_usuario}! 🐵")
        st.switch_page("2_Login")

if st.button("Volver al login", key="volver"):
    st.switch_page("2_Login")