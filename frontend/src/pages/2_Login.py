import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

if "usuarios" not in st.session_state:
    st.session_state.usuarios = {"admin": "1234"}

st.title("Iniciar sesión")
st.subheader("Bienvenido a la jungla! ")

usuario = st.text_input("Usuario")
contraseña = st.text_input("Contraseña", type="password")

if st.button("Entrar", key="entrar"):
    if usuario in st.session_state.usuarios and st.session_state.usuarios[usuario] == contraseña:
        st.session_state["usuario_actual"] = usuario
        st.success(f"¡Bienvenido, {usuario}! 🐒")
        st.switch_page("Home")
    else:
        st.error("Usuario o contraseña incorrectos.")

st.markdown("¿No tienes cuenta?")
if st.button("Ir a registro", key="registro"):
    st.switch_page("1_Registro")
