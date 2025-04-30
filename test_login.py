import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open("usuarios.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    credentials=config["credentials"],
    cookie_name=config["cookie"]["name"],
    key=config["cookie"]["key"],
    expiry_days=config["cookie"]["expiry_days"]
)

auth_status = authenticator.login(
    location="main",
    fields={
        'Form name': 'Login',
        'Username': 'Usuario',
        'Password': 'Contraseña',
        'Login': 'Iniciar sesión'
    }
)

st.write("Estado de login:", auth_status)

if auth_status:
    authenticator.logout("Cerrar sesión", "sidebar")
    st.success(f"Bienvenido {authenticator.username}")
elif auth_status is False:
    st.error("Usuario o contraseña incorrectos.")
elif auth_status is None:
    st.info("Por favor inicia sesión.")
