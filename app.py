import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Control de Ingresos Ecopetrol", layout="wide")

# Título del Tablero
st.title("🛡️ Tablero de Registro y Control de Ingresos - Ecopetrol")
st.write("Sube el archivo Excel con el registro del personal y adjunta los certificados en PDF.")

# Dividir la pantalla en dos columnas
col1, col2 = st.columns(2)

# Columna 1: Para el Excel
with col1:
    st.subheader("📊 Base de Datos de Personal")
    archivo_excel = st.file_uploader("Sube aquí el archivo Excel (XLSX)", type=["xlsx"])
    
    if archivo_excel is not None:
        try:
            # Leemos y mostramos el Excel
          df = pd.read_excel(archivo_excel)
            st.dataframe(df, use_container_width=True)
            st.success("¡Base de datos cargada correctamente!")
        except Exception as e:
            st.error(f"Hubo un error al leer el Excel. Asegúrate de subir el archivo correcto.")

# Columna 2: Para los PDFs
with col2:
    st.subheader("📄 Certificados Parafiscales (PDF)")
    archivos_pdf = st.file_uploader("Sube los certificados de parafiscales aquí", type=["pdf"], accept_multiple_files=True)
    
    if archivos_pdf:
        st.write("**Archivos adjuntos:**")
        for pdf in archivos_pdf:
            st.write(f"✅ {pdf.name}")
        st.success(f"¡{len(archivos_pdf)} documento(s) cargado(s) exitosamente!")
