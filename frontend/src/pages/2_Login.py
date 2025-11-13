import streamlit as st

st.set_page_config(page_title="Login - Majo App", layout="centered", page_icon="🐵")

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
        animation: swing 2s infinite;
    }
    
    @keyframes swing {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(10deg); }
        75% { transform: rotate(-10deg); }
    }
    
    /* Divisor */
    .divider {
        text-align: center;
        margin: 2rem 0;
        color: #999;
    }
    
    /* Card de bienvenida */
    .welcome-card {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        border: 1px solid #667eea30;
    }
</style>
""", unsafe_allow_html=True)

# Inicialización de estado
if "usuarios" not in st.session_state:
    st.session_state.usuarios = {"admin": "1234"}

# Si ya está logueado, redirigir al home
if "usuario_actual" in st.session_state:
    st.success(f"✅ Ya tienes sesión activa, {st.session_state.usuario_actual}!")
    if st.button("➡️ Ir al muro"):
        st.switch_page("Home.py")  # ← CAMBIO AQUÍ (va a la raíz)
    st.stop()

# Header con emoji
st.markdown('<div class="emoji-header">🐒</div>', unsafe_allow_html=True)

# Título y subtítulo
st.title("¡Bienvenido de vuelta!")
st.subheader("Ingresa a la jungla y descubre lo nuevo")

# Card de bienvenida
st.markdown("""
<div class="welcome-card">
    <p style='text-align: center; margin: 0; color: #667eea; font-size: 1.1rem;'>
        🌴 <strong>¡La jungla te estaba esperando!</strong> 🌴
    </p>
</div>
""", unsafe_allow_html=True)

# Formulario de login
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    usuario = st.text_input("👤 Usuario", placeholder="Ingresa tu nombre de usuario")
    contraseña = st.text_input("🔒 Contraseña", type="password", placeholder="Ingresa tu contraseña")
    
    # Botón principal
    if st.button("🚪 Entrar", key="entrar", type="primary"):
        if usuario in st.session_state.usuarios and st.session_state.usuarios[usuario] == contraseña:
            st.session_state["usuario_actual"] = usuario
            st.success(f"✅ ¡Bienvenido de vuelta, {usuario}! 🎉")
            st.balloons()
            st.rerun()
        else:
            st.error("❌ Usuario o contraseña incorrectos. Verifica tus datos.")
    
    # Divisor
    st.markdown('<div class="divider">━━━━━━━ o ━━━━━━━</div>', unsafe_allow_html=True)
    
    # Sección de registro
    st.markdown("""
    <div style='text-align: center; color: #666; margin-bottom: 1rem;'>
        ¿Aún no tienes cuenta? 🤔
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📝 Crear cuenta nueva", key="registro"):
        st.switch_page("pages/1_Registro.py")  # ← Se mantiene igual (misma carpeta)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #999; padding: 1rem;'>
    <small>🐒 Majo App 2025 - Red Social de la Jungla 🌴</small>
</div>
""", unsafe_allow_html=True)

# Tips de login (opcional)
with st.expander("💡 Consejos de seguridad"):
    st.markdown("""
    - 🔐 Nunca compartas tu contraseña
    - 🚫 No uses la misma contraseña en otros sitios
    - ✅ Asegúrate de cerrar sesión en dispositivos compartidos
    """)