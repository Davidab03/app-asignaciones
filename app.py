import streamlit as st
import pandas as pd

# 1. Configuración de la página
st.set_page_config(page_title="Panel Concentrix", page_icon="📊", layout="wide")

# 2. Título y bienvenida
st.title("📊 Panel Interactivo de Asignaciones")
st.write("Sube tu archivo de Excel descargado para generar los reportes y promedios al instante.")

# 3. El botón para subir el archivo
archivo_subido = st.file_uploader("Arrastra aquí tu base de datos (.xlsx)", type=["xlsx"])

# 4. ¿Qué pasa cuando el usuario sube el archivo?
if archivo_subido is not None:
    # Mostramos un mensaje de carga
    with st.spinner('Leyendo 39,000 filas... 🚀'):
        # Leer el Excel (openpyxl hace el trabajo sucio)
        df = pd.read_excel(archivo_subido)
    
    st.success("¡Archivo cargado con éxito!")
    
    # --- A PARTIR DE AQUÍ DIBUJAS TU INTERFAZ ---
    
    # Crear columnas para que se vea como un tablero profesional
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total de Filas", value=len(df))
        
    with col2:
        # Ejemplo: Contar cuántas columnas tiene
        st.metric(label="Total de Columnas", value=len(df.columns))
        
    with col3:
        st.metric(label="Estado", value="Procesado")

    st.markdown("---")
    
    # 5. Replicar tu "Tabla Dinámica" de la imagen anterior
    st.subheader("Resumen por Grupo (Tabla Dinámica)")
    
    # Asegúrate de usar los nombres exactos de las columnas de tu Excel
    try:
        # Agrupamos por GROUP_NAME y contamos (puedes cambiar las columnas según tu Excel real)
        tabla_dinamica = df.groupby('GROUP_NAME').size().reset_index(name='Total Asignaciones')
        st.dataframe(tabla_dinamica, use_container_width=True)
    except Exception as e:
        st.warning(f"Asegúrate de que tu Excel tenga una columna llamada 'GROUP_NAME'. Error: {e}")
        
    # 6. Mostrar la base de datos cruda con filtros interactivos
    st.subheader("Base de Datos Exploratoria")
    st.dataframe(df)

else:
    st.info("Esperando el archivo. Por favor, sube tu Excel para comenzar.")
