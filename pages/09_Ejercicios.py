import streamlit as st
import random

st.sidebar.header("Ejercicios")

st.title("Ejercicios")

st.header("Ejercicio 1: Saludo Simple")

with st.form("form_saludo"):
    Nombre = st.text_input("Ingrese su nombre")
    submit_saludo = st.form_submit_button("Enviar")
    if submit_saludo and Nombre:
        st.write("¡Hola, ", Nombre, "!")

st.divider()

st.header("Ejercicio 2: Calculadora de Producto")

with st.form("form_calculadora"):
    num1 = st.number_input("Ingrese el primer número")
    num2 = st.number_input("Ingrese el segundo número")
    submit_calc = st.form_submit_button("Calcular")
    
    if submit_calc:
        resultado = num1 * num2
        if num1 > 100 or num2 > 100:
            st.warning("Números grandes")
        else:
            st.write("El resultado de su operación es: ", resultado)

st.divider()

st.header("Ejercicio 3: Convertidor de temperatura")

with st.form("form_temperatura"):
    medida = st.radio("¿Qué temperatura desea convertir?", ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
    temperatura = st.number_input("Ingrese la temperatura: ")
    submit_temp = st.form_submit_button("Convertir")

    if submit_temp:
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

st.header("Ejercicio 6: Login Simulado")

if "logueado" not in st.session_state:
    st.session_state.logueado = False

if st.session_state.logueado:
    st.success("Bienvenido al sistema")
    if st.button("Cerrar Sesión"):
        st.session_state.logueado = False
        st.rerun()
else:
    with st.form("form_login"):
        usuario = st.text_input("Usuario")
        contrasena = st.text_input("Contraseña", type="password")
        submit_login = st.form_submit_button("Ingresar")
        
        if submit_login:
            if usuario == "admin" and contrasena == "1234":
                st.session_state.logueado = True
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")

st.divider()

st.header("Ejercicio 7: Lista de Compras")

if 'tareas' not in st.session_state:
    st.session_state.tareas = []

with st.form("form_compras"):
    nueva_tarea = st.text_input("Nueva tarea", key="input_tarea")
    submit_tarea = st.form_submit_button("Agregar tarea")
    
    if submit_tarea and nueva_tarea:
        st.session_state.tareas.append(nueva_tarea)
        st.success(f"Tarea '*{nueva_tarea}*' agregada!")

st.write("### Tus Tareas:")
if st.session_state.tareas:
    for i, tarea in enumerate(st.session_state.tareas):
        st.write(f"{i + 1}. {tarea}")
    
    if st.button("Limpiar lista"):
        st.session_state.tareas = []
        st.rerun()
else:
    st.info("La lista está vacía.")

st.divider()

st.header("Ejercicio 8: Gráfico Interactivo")

with st.form("form_grafico"):
    N = st.slider("Selecciona un número entre 10 y 100", 0, 150, 50)
    submit_grafico = st.form_submit_button("Generar / Regenerar")

if submit_grafico:
    if N < 10:
        st.warning("El número debe ser mayor a 10")
    else:
        lista = [random.randint(1, 100) for _ in range(N)]
        st.line_chart(lista)
elif 'submit_grafico' not in locals():
    # Mostrar un gráfico inicial o mensaje
    st.info("Ajusta el slider y presiona el botón para generar el gráfico.")

st.divider()

