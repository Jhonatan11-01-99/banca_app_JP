import streamlit as st

def mostrar():
    st.title("Bienvenido al simulador bancario")
    st.markdown("""
                
            Esta aplicacion permite simular creditos hipotecarios y vehiculares.
            Proximamente se conectara con Supabase para guardar las simulaciones
            """
                )