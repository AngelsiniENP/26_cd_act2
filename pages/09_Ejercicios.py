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

tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"]) 

with tab1:
    st.write("Un gato")
    st.image("https://i.guim.co.uk/img/media/327aa3f0c3b8e40ab03b4ae80319064e401c6fbc/377_133_3542_2834/master/3542.jpg?width=620&dpr=1&s=none&crop=none")
    if st.button("👍", key="voto_gato"):
        st.toast("Te gusta esta mascota", icon="👍")

with tab2:
    st.write("Un perro")
    st.image("https://images.ctfassets.net/denf86kkcx7r/2KGI03JSLCerDS7RD20OZP/b85317da255ed7119430759308414a49/perros_de_pastor_y_boyeros_-_1.jpg")
    if st.button("👍", key="voto_perro"):
        st.toast("Te gusta esta mascota", icon="👍")

with tab3:
    st.write("Un Ave")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkAvK9Eh7Z11ZY8Nxx0bH3JSPfKPp2dzDiUMxjzBGTb_TSpCByzmZ5gv8XKQgB7And7BUVWw0TBprqa2uiHaTB-nPjsSm_M5-10nT1vUSMuw&s=10")
    if st.button("👍", key="voto_ave"):
        st.toast("Te gusta esta mascota", icon="👍")

st.divider()

st.header("Ejercicio 5: Caja de Comentarios")

with st.form("Caja de comentarios"):
    
    asunto = st.text_input("Asunto")
    mensaje = st.text_area("Mensaje")

    enviar = st.form_submit_button("Enviar")

    if enviar:
        if len(mensaje) == 0 or len(asunto) == 0:
            st.write("Debe ingresar un asunto y un mensaje")
        else:
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

if 'Productos' not in st.session_state:
    st.session_state.Productos = []

with st.form("form_compras"):
    nuevo_producto = st.text_input("Nuevo Producto", key="input_producto")
    submit_producto = st.form_submit_button("Agregar Producto")
    
    if submit_producto and nuevo_producto:
        st.session_state.Productos.append(nuevo_producto)
        st.success(f"Producto '*{nuevo_producto}*' agregado!")

st.write("### Tus Productos:")
if st.session_state.Productos:
    for i, producto in enumerate(st.session_state.Productos):
        st.write(f"{i + 1}. {producto}")
    
    if st.button("Limpiar lista"):
        st.session_state.Productos = []
        st.rerun()
else:
    st.info("La lista está vacía.")

st.divider()

st.header("Ejercicio 8: Gráfico Interactivo")

with st.form("form_grafico"):
    # Rango ajustado de 10 a 100
    N = st.slider("Selecciona un número entre 10 y 100", 10, 100)
    submit_grafico = st.form_submit_button("Generar / Regenerar")

if submit_grafico:
    if N < 10:
        st.warning("El número debe ser mayor a 10")
    else:
        lista = [random.randint(1, 100) for _ in range(N)]
        st.line_chart(lista)
        st.success(f"Gráfico generado con {N} puntos aleatorios.")
else:
    st.info("Ajusta el slider y presiona el botón para generar el gráfico.")
st.divider()

