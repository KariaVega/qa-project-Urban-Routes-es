1. Se instala Selenium
2. Se instala Pip
3. Se instala pytest

Lista de Comprobación de Pruebas.

1. Configuración de direcciones.
2. Selección de tarifa Comfort.
3. Rellenar número de teléfono.
4. Agregar una tarjeta de crédito.
5. Escribir un mensaje para el conductor.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Aparece el modal para buscar un taxi.
9. Esperar la información del conductor.

ARCHIVOS:
1. Data.py (Datos)
2. Main.py (métodos de la clase)
3. Test_cases_UrbanRoutes (funciones de casos de prueba)
4. README (Descripcion del contenido)

PASOS A SEGUIR CON MÉTODO POM:
- Se crean los localizadores de cada uno de los elemntos que se utilizaran en las pruebas.
- Se crea __init__ qué es el constructor de la clase UrbanRoutesPage, para crear nuevas instancias de la clase y 
las funciones para sus atributos.
- Se agrega WebDriverWait que permite establecer tiempos de espera para la craga y verificación de datos en la 
secuencia de las pruebas automatizadas.
Prueba 1. 
Se crean lo métodos para los campos de entrada e ingresar las direcciones utilizando;
.send_keys() y .get_propierty() respectivamente para obtener el valor de entrada de los campos de direcciones,
y realizar las comprobaciones.
Prueba 2. 
Se crean los métodos para la selección de la tarifa  comfort, verificando la opción flash con 
el método .is_enable() para "Pedir un taxi" con .click() y finalmente .text para la verificación de la 
selección de la tarifa Comfort.
Prueba 3. 
Se crean los métodos para ingresar el número de teléfono con .click(), send_keys() y .text respectivamente 
para ingresar, introducir y verificar el número de teléfono, se ingresa codigo de confirmación con la funcion:
retrieve_phone_code que devuelve el codigo de confirmación.
Prueba 4. 
Se crean los métodos para los campos de entrada e ingresar número y código de la tarjeta con .click(), 
.send_keys(). Posteriormente se verifica la seleccion de la tarjeta ingresada con .is_enabled() y .text para realizar
la verificación de los datos y la seleción del método de pago.
Prueba 5. 
Se crean los métodos para ingresar el mensaje del conductor en el campo de entrada con .send_keys() y 
.get_propierty() para la comprobación del mensaje.
Prueba 6. 
Se crean los métodos .click() y is_anable() para la selección de manta y pañuelos comprobando la selección.
Prueba 7.
Se crean los métodos .click() y is_anable() para la selección de 2 heñados comprobando la selección.
Prueba 8.
Se cxrean los métodos .is_anable(), .click() para la selección del modal y .text compobabando la selección.
Prueba 9. 
Se verifica la ventana emergente con los datos del viaje, con el método .text compobabando.

