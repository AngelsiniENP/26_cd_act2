# Ejercicios de Streamlit

Realiza estos ejercicios en tu archivo `pages/09_Ejercicios.py`.

### Ejercicio 1: Saludo Simple
Crea un campo de entrada de texto para que el usuario escriba su nombre.
*   Si el nombre no está vacío, muestra un mensxaje de bienvenida: "¡Hola, [Nombre]!".  

### Ejercicio 2: Calculadora de Producto
Pide al usuario dos números (usando `st.number_input`).
*   Muestra el resultado de su multiplicación.
*   Si alguno de los números es mayor a 100, muestra un `st.warning` indicando "Números grandes".

### Ejercicio 3: Convertidor de Temperatura (Radio Buttons)
*   Usa un `st.radio` para elegir la dirección de la conversión: "Celsius a Fahrenheit" o "Fahrenheit a Celsius".
*   Usa un `st.number_input` para ingresar la temperatura.
*   Muestra el resultado calculado.
    *   *Fórmula C a F*: `(C * 9/5) + 32`
    *   *Fórmula F a C*: `(F - 32) * 5/9`

### Ejercicio 4: Galerí­a de Mascotas (Tabs)
*   Crea 3 pestañas: "Gatos", "Perros", "Aves".
*   En cada pestaña muestra una imagen diferente (puedes usar URLs públicas) y un botón de "Me gusta" que, al ser presionado, muestre un `st.toast` diciendo "Te gusta esta mascota".

### Ejercicio 5: Caja de Comentarios (Formulario)
Crea un formulario con:
*   Un campo de texto para el asunto.
*   Un área de texto para el mensaje.
*   Un botón de envío.
*   Al enviar, muestra los datos ingresados en un `st.json` o `st.write` solo si el mensaje no está vacío.

### Ejercicio 6: Login Simulado (Session State)
*   Crea dos campos: usuario y contraseña (usa `type='password'`).
*   Un botón "Ingresar".
*   Si el usuario es "admin" y la contraseña "1234", guarda en `st.session_state` que el usuario está logueado y muestra un mensaje de éxito.
*   Si ya está logueado, muestra un botón "Cerrar Sesión" que limpie el estado.

### Ejercicio 7: Lista de Compras (Session State)
*   Un `st.text_input` para ingresar un producto.
*   Dos botones: "Agregar" y "Limpiar Lista".
*   Muestra la lista de productos agregados hasta el momento. La lista debe persistir aunque interactúes con otros widgets.

### Ejercicio 8: Gráfico Interactivo
*   Usa un `st.slider` para seleccionar un número `N` entre 10 y 100.
*   Genera una lista de `N` números aleatorios.
*   Muestra un `st.line_chart` con esos datos.
*   Añade un botón para "Regenerar" los datos (pista: el botón hará rerun, lo que regenerará los aleatorios automáticamente).
