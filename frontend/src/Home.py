import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Muro - Majo App",
    layout="wide",
    page_icon="🐵"
)

# VERIFICAR SESIÓN PRIMERO - ANTES DE CUALQUIER COSA
if "usuario_actual" not in st.session_state:
    st.switch_page("pages/2_Login.py")  # ← CAMBIO AQUÍ

# CSS personalizado mejorado
st.markdown("""
<style>
    /* Fondo general */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Sidebar mejorada */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] .stRadio > label {
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stSidebar"] label {
        color: white !important;
    }
    
    /* Contenedor principal */
    .main {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
    }
    
    /* Títulos */
    h1 {
        color: #667eea;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0.5rem !important;
    }
    
    h2, h3 {
        color: #764ba2;
    }
    
    /* Cards de publicaciones */
    .post-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .post-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
    }
    
    .post-header {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        font-weight: 600;
        color: #667eea;
        font-size: 1.1rem;
    }
    
    .post-date {
        color: #999;
        font-size: 0.85rem;
        margin-left: auto;
    }
    
    .post-content {
        color: #333;
        line-height: 1.6;
        font-size: 1rem;
    }
    
    /* Tarjeta de tendencias */
    .trend-card {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid #667eea30;
    }
    
    .trend-item {
        padding: 0.8rem;
        margin: 0.5rem 0;
        background: white;
        border-radius: 10px;
        border-left: 3px solid #667eea;
    }
    
    /* Botones */
    .stButton > button {
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* Inputs y text areas */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Card de perfil */
    .profile-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Stats */
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar publicaciones en session_state
if "publicaciones" not in st.session_state:
    st.session_state.publicaciones = [
        {
            "usuario": "MonoLoco",
            "contenido": "¡Encontré una nueva cueva con bananas! 🍌 ¿Alguien quiere venir?",
            "fecha": "2025-11-11 14:30",
            "likes": 15
        },
        {
            "usuario": "BananaFan",
            "contenido": "¿Alguien más vio al gorila bailar? 🦍💃 ¡Fue épico!",
            "fecha": "2025-11-10 18:45",
            "likes": 23
        },
        {
            "usuario": "JungleExplorer",
            "contenido": "Descubrí un árbol gigante con frutas exóticas. La jungla nunca deja de sorprender 🌴✨",
            "fecha": "2025-11-09 10:20",
            "likes": 8
        }
    ]

# Header
col_title1, col_title2 = st.columns([3, 1])
with col_title1:
    st.title("🐵 Red Social - Majo App")
    st.markdown(f"**Bienvenido, {st.session_state.usuario_actual}!** 👋")
with col_title2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚪 Cerrar sesión"):
        del st.session_state["usuario_actual"]
        st.switch_page("pages/2_Login.py")  # ← CAMBIO AQUÍ

st.markdown("---")

# Sidebar
st.sidebar.title("🌴 Menú")
st.sidebar.markdown("---")
opcion = st.sidebar.radio(
    "Navegar a:",
    ["🏠 Inicio", "✏️ Publicar", "👤 Mi Perfil"],
    label_visibility="collapsed"
)
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style='color: white; text-align: center; padding: 1rem;'>
    <p style='font-size: 0.9rem; margin: 0;'>🐒 <strong>Majo App</strong></p>
    <p style='font-size: 0.8rem; opacity: 0.8; margin: 0;'>Red Social de la Jungla</p>
</div>
""", unsafe_allow_html=True)

# SECCIÓN: INICIO
if opcion == "🏠 Inicio":
    col1, col2 = st.columns([2.5, 1])
    
    with col1:
        st.markdown("### 📰 Feed de Publicaciones")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Mostrar publicaciones
        for i, post in enumerate(reversed(st.session_state.publicaciones)):
            st.markdown(f"""
            <div class="post-card">
                <div class="post-header">
                    🐵 {post['usuario']}
                    <span class="post-date">📅 {post['fecha']}</span>
                </div>
                <div class="post-content">
                    {post['contenido']}
                </div>
                <div style="margin-top: 1rem; color: #999;">
                    ❤️ {post['likes']} Me gusta
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🔥 Tendencias")
        st.markdown("""
        <div class="trend-card">
            <div class="trend-item">
                <strong>🏆 Mono más popular</strong><br>
                <span style="color: #667eea;">MonoLoco</span>
            </div>
            <div class="trend-item">
                <strong>🍌 Tema del día</strong><br>
                <span style="color: #764ba2;">#BananasBrillantes</span>
            </div>
            <div class="trend-item">
                <strong>📊 Usuarios activos</strong><br>
                <span style="color: #667eea;">127 monos online</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🖼️ Chisme del día")
        st.image("https://i.imgur.com/WxNkK3m.png", use_container_width=True)

# SECCIÓN: PUBLICAR
elif opcion == "✏️ Publicar":
    st.markdown("### ✏️ Crear nueva publicación")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%); 
                    padding: 1.5rem; border-radius: 15px; margin-bottom: 2rem;">
            <p style="text-align: center; margin: 0; color: #667eea; font-size: 1.1rem;">
                🌴 <strong>Comparte tus aventuras en la jungla</strong> 🌴
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        contenido = st.text_area(
            "¿Qué chisme quieres compartir? 🍌",
            placeholder="Escribe aquí tu publicación... ¡Cuéntanos todo!",
            height=150,
            key="nueva_publicacion"
        )
        
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("🚀 Publicar", use_container_width=True, type="primary"):
                if contenido:
                    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
                    nueva_publicacion = {
                        "usuario": st.session_state.usuario_actual,
                        "contenido": contenido,
                        "fecha": fecha,
                        "likes": 0
                    }
                    st.session_state.publicaciones.append(nueva_publicacion)
                    st.success(f"✅ ¡Publicación añadida con éxito! 🎉")
                    st.balloons()
                    # Limpiar el campo después de publicar
                    st.session_state["nueva_publicacion"] = ""
                else:
                    st.error("❌ Por favor escribe algo antes de publicar.")
        
        with col_btn2:
            if st.button("🔄 Limpiar", use_container_width=True):
                st.rerun()

# SECCIÓN: MI PERFIL
elif opcion == "👤 Mi Perfil":
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="profile-card">
            <img src="https://i.imgur.com/l0yqI3G.png" style="width: 150px; border-radius: 50%; border: 5px solid #667eea; margin-bottom: 1rem;">
            <h2 style="color: #667eea; margin: 0.5rem 0;">""" + st.session_state.usuario_actual + """</h2>
            <p style="color: #999; margin-bottom: 2rem;">🐒 Mono de la Jungla</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Estadísticas
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_stat1, col_stat2, col_stat3 = st.columns(3)
        
        with col_stat1:
            mis_posts = len([p for p in st.session_state.publicaciones if p["usuario"] == st.session_state.usuario_actual])
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number">{mis_posts}</div>
                <div class="stat-label">Publicaciones</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_stat2:
            total_likes = sum([p["likes"] for p in st.session_state.publicaciones if p["usuario"] == st.session_state.usuario_actual])
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number">{total_likes}</div>
                <div class="stat-label">Me gusta</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_stat3:
            st.markdown("""
            <div class="stat-box">
                <div class="stat-number">⭐⭐⭐</div>
                <div class="stat-label">Nivel Banana</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Info adicional
        st.markdown("""
        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; text-align: left;">
            <p><strong>📅 Miembro desde:</strong> 2025</p>
            <p><strong>🎯 Logros:</strong> Explorador Novato 🏅</p>
            <p><strong>🍌 Frutas recolectadas:</strong> 42</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #999; padding: 1rem;'>
    <p style='margin: 0;'>Creado con 🐒 por Majo App - 2025</p>
    <p style='margin: 0; font-size: 0.85rem;'>🌴 Red Social de la Jungla 🌴</p>
</div>
""", unsafe_allow_html=True)