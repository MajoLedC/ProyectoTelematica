import streamlit as st

st.set_page_config(page_title="Registro - Majo App", layout="centered", page_icon="🐵")

# CSS personalizado
st.markdown("""
<style>
    /* Fondo y tema general */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Contenedor principal */
    .main {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    /* Títulos */
    h1 {
        color: #667eea;
        text-align: center;
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    h3 {
        color: #764ba2;
        text-align: center;
        font-weight: 400 !important;
        margin-bottom: 2rem !important;
    }
    
    /* Inputs */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 12px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Botones */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        margin-top: 10px;
    }
    
    .stButton > button:first-child {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Mensajes de error y éxito */
    .stAlert {
        border-radius: 10px;
        border: none;
        margin-top: 1rem;
    }
    
    /* Logo/Emoji central */
    .emoji-header {
        text-align: center;
        font-size: 4rem;
        margin: 1rem 0;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* Divisor */
    .divider {
        text-align: center;
        margin: 2rem 0;
        color: #999;
    }
</style>
""", unsafe_allow_html=True)

# Inicialización de estado
if "usuarios" not in st.session_state:
    st.session_state.usuarios = {}

# Header con emoji
st.markdown('<div class="emoji-header">🐵</div>', unsafe_allow_html=True)

# Título y subtítulo
st.title("¡Únete a la Jungla!")
st.subheader("Crea tu cuenta y comienza a compartir")

# Espacio
st.markdown("<br>", unsafe_allow_html=True)

# Formulario de registro
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    nuevo_usuario = st.text_input("👤 Nombre de usuario", placeholder="Elige tu nombre de mono")
    nueva_contraseña = st.text_input("🔒 Contraseña", type="password", placeholder="Mínimo 6 caracteres")
    confirmar = st.text_input("🔒 Confirmar contraseña", type="password", placeholder="Repite tu contraseña")
    
    # Botón principal
    if st.button("🚀 Crear cuenta", key="crear", type="primary"):
        if nuevo_usuario in st.session_state.usuarios:
            st.error("❌ Ese nombre de usuario ya existe. ¡Prueba otro!")
        elif nueva_contraseña != confirmar:
            st.error("❌ Las contraseñas no coinciden. Inténtalo de nuevo.")
        elif nuevo_usuario == "" or nueva_contraseña == "":
            st.warning("⚠️ Por favor completa todos los campos.")
        elif len(nueva_contraseña) < 6:
            st.warning("⚠️ La contraseña debe tener al menos 6 caracteres.")
        else:
            st.session_state.usuarios[nuevo_usuario] = nueva_contraseña
            st.success(f"✅ ¡Cuenta creada con éxito, {nuevo_usuario}! 🎉")
            st.balloons()
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("➡️ Ir al login"):
                st.switch_page("pages/2_Login.py")  # ← Se mantiene igual (misma carpeta)
    
    # Divisor
    st.markdown('<div class="divider">━━━━━━━ o ━━━━━━━</div>', unsafe_allow_html=True)
    
    # Botón secundario
    st.markdown("¿Ya tienes una cuenta?")
    if st.button("🔑 Iniciar sesión", key="volver"):
        st.switch_page("pages/2_Login.py")  # ← Se mantiene igual (misma carpeta)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #999; padding: 1rem;'>
    <small>🐒 Majo App 2025 - Red Social de la Jungla 🌴</small>
</div>
""", unsafe_allow_html=True)