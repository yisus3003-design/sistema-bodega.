import streamlit as st
from supabase import create_client

# Configuración de la página (adaptada a móviles) 📱
st.set_page_config(page_title="Bodega 🏪", layout="wide")

# Conexión a Supabase ⚡
SUPABASE_URL = "https://xzpdtupzjczsyxrohlet.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh6cGR0dXB6amN6c3l4cm9obGV0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODYzODMyNTEsImV4cCI6MjEwMTk1OTI1MX0.fQ6PHyl1R5sC32b5trQ4xmOzlA2MXO2w3NW6iM6IMLs"

@st.cache_resource
def obtener_conexion():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase = obtener_conexion()

st.title("Sistema de Bodega 🏪")

# Formulario e Inventario 📊
col_form, col_lista = st.columns([1, 2])

with col_form:
    st.header("Nuevo Producto ➕")
    with st.form("form_agregar", clear_on_submit=True):
        nombre = st.text_input("Nombre del producto")
        categoria = st.text_input("Categoría")
        precio = st.number_input("Precio USD", min_value=0.0, step=0.1, format="%.2f")
        guardar = st.form_submit_button("Guardar Producto")

        if guardar and nombre:
            supabase.table("Productos").insert({
                "nombre": nombre,
                "categoria": categoria,
                "precio_usd": precio
            }).execute()
            st.success(f"¡{nombre} guardado correctamente!")

with col_lista:
    st.header("Inventario Actual 📦")
    respuesta = supabase.table("Productos").select("*").execute()
    st.dataframe(respuesta.data, use_container_width=True)