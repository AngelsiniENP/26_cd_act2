import streamlit as st

st.title("Ejercicios")

st.header("Ejercicio 1: Saludo Simple")

Nombre = st.text_input("Ingrese su nombre")

if Nombre:
    st.write("¡Hola, ", Nombre, "!")

st.divider()

st.header("Ejercicio 2: Calculadora de Producto")

num1 = st.number_input("Ingrese el primer número")
num2 = st.number_input("Ingrese el segundo número")
resultado = num1 * num2

if num1 > 100 or num2 > 100:
    st.warning("Números grandes")
else:
    st.write("El resultado de su operación es: ", resultado)

st.divider()

st.header("Ejercicio 3: Convertidor de temperatura")

medida = st.radio("¿Qué temperatura desea convertir?", ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])

temperatura = st.number_input("Ingrese la temperatura: ")

if temperatura != 0:
    if medida == "Celsius a Fahrenheit":
        st.write("La temperatura en fahrenheit es:", (temperatura * 9/5) + 32)
    else:
        st.write("La temperatura en celsius: es", (temperatura - 32) * 5/9)

st.divider()

st.header("Ejercicio 4: Galería de Mascotas")

tab1, tab2, tab3 = st.tabs(["Cerdo", "Mono", "T-Rex"]) 

with tab1:
    st.write("Un cerdo")
    st.image("https://img.freepik.com/foto-gratis/cerdo-domestico-granja-al-aire-libre_52683-115856.jpg?semt=ais_user_personalization&w=740&q=80")
    if st.button("👍", key="voto_cerdo"):
        st.toast("Te gusta esta mascota", icon="👍")

with tab2:
    st.write("Un mono")
    st.image("https://media.cnn.com/api/v1/images/stellar/prod/cnne-212344-monkey-selfie.jpeg?c=16x9&q=h_833,w_1480,c_fill")
    if st.button("👍", key="voto_mono"):
        st.toast("Te gusta esta mascota", icon="👍")

with tab3:
    st.write("Un T-Rex")
    st.image("https://telusworldofscienceedmonton.ca/media/images/NEW_T.REX_Main_Webp.2e16d0ba.fill-1920x1080.format-webp.webp")
    if st.button("👍", key="voto_trex"):
        st.toast("Te gusta esta mascota", icon="👍")

st.divider()

st.header("Ejercicio 5: Caja de Comentarios")

with st.form("Caja de comentarios"):
    
    asunto = st.text_input("Asunto")
    mensaje = st.text_input("Mensaje")

    enviar = st.form_submit_button("Enviar")

    if enviar:
        st.write("Formulario enviado")
        st.write(f"Asunto: {asunto}")
        st.write(mensaje)

st.divider()
