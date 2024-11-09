# Proyecto: Urban Routes
## *Automatización de las pruebas*
![image](https://github.com/user-attachments/assets/2f64ea02-82a9-45e3-bbae-5d41a2232e2c)

### :page_facing_up: *Documentación utilizada:* 
- Requisitos para aplicativo Web de UrbanRoutes:  [Link de requisitos](https://cnt-9aea8897-4d05-4697-990a-d321c45463a6.containerhub.tripleten-services.com/)

### 🛠️ *Lenguajes y herramientas utilizadas:*
<div id="header" align="left">
  
- DevTools: Generar buscadores.
- Python: Codigo para las pruebas.
- Pycharm: Ejecución de las pruebas.
- GitBash: Clonación del repositorio.
- GitHub: Respaldo del codigo.
- Selenium
- Pytest
- Pip

<img decoding="async" src="https://img.shields.io/badge/DevTools-D80B01?style=for-the-badge&logo=Drawio&logoColor=white" alt="Drawio"/>
<img decoding="async" src="https://img.shields.io/badge/Python-0052CC?style=for-the-badge&logo=python&logoColor=white" alt="python"/>
<img decoding="async" src="https://img.shields.io/badge/PyCharm-darkgreen.svg?&style=for-the-badge&logo=PyCharm&logoColor=white" alt="PyCharm"/>
<img decoding="async" src="https://img.shields.io/badge/Git_Bash-D89B01?&style=for-the-badge&logo=GitBash&logoColor=white" alt="GitBash"/>
<img decoding="async" src="https://img.shields.io/badge/GitHub-000000.svg?&style=for-the-badge&logo=GitHub&logoColor=white" alt="GitHub"/>
<img decoding="async" src="https://img.shields.io/badge/Selenium-008000?style=for-the-badge&logo=Selenium&logoColor=white" alt="Selenium"/>
<img decoding="async" src="https://img.shields.io/badge/Pytest-darkblue?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest"/>
<img decoding="async" src="https://img.shields.io/badge/Pip-darkred?style=for-the-badge&logo=Pip&logoColor=white" alt="Pip"/>

### :computer:  *Descripción del Aplicativo Urban Routes* 
- Urban Routes es una aplicación que crea rutas y calcula la duración y precio del viaje para diferentes tipos de transporte. La interfaz es bastante sencilla, contiene dos campos para las direcciones: "Desde" y "Hasta". Además, cuenta con tres modos ("Óptimo", "Flash" y "Personal"), así como íconos para los tipos de transporte (automóvil del usuario, a pie, taxi, bicicleta, scooter o compartir un automóvil). Se realizará la automatización de las pruebas de la selección de la tarifa Comfort y el llenado de su formulario para el pedido y la verificación de la confirmación.

### :page_facing_up: *Lista de Comprobación de Pruebas:*  

1. Configuración de direcciones.
2. Selección de tarifa Comfort.
3. Rellenar número de teléfono.
4. Agregar una tarjeta de crédito.
5. Escribir un mensaje para el conductor.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Aparece el modal para buscar un taxi.
9. Esperar la información del conductor.

### :file_folder: *Archivos:* 
1. Data.py (Datos)
2. Main.py (métodos de la clase)
3. Test_cases_UrbanRoutes (funciones de casos de prueba)
4. README (Descripcion del contenido)

### :paw_prints: *Pasos a seguir metodología POM:* 
- Se crean los localizadores de cada uno de los elementos que se utilizarán en las pruebas.
- Se crea __init__ qué es el constructor de la clase UrbanRoutesPage, para crear nuevas instancias de la clase y 
las funciones para sus atributos.
- Se agrega WebDriverWait que permite establecer tiempos de espera para la carga y verificación de datos en la 
secuencia de las pruebas automatizadas.

### 🧪 *Resultados de las pruebas:* 
  - #### Prueba 1. 
    Se crean lo métodos para los campos de entrada e ingresar las direcciones utilizando;
.send_keys() y .get_propierty() respectivamente para obtener el valor de entrada de los campos de direcciones,
y realizar las comprobaciones.
  - #### Prueba 2.
    Se crean los métodos para la selección de la tarifa  comfort, verificando la opción flash con 
el método .is_enable() para "Pedir un taxi" con .click() y finalmente .text para la verificación de la 
selección de la tarifa Comfort.
  - #### Prueba 3. 
    Se crean los métodos para ingresar el número de teléfono con .click(), send_keys() y .text respectivamente 
para ingresar, introducir y verificar el número de teléfono, se ingresa codigo de confirmación con la funcion:
retrieve_phone_code que devuelve el codigo de confirmación.
  - #### Prueba 4. 
    Se crean los métodos para los campos de entrada e ingresar número y código de la tarjeta con .click(), 
.send_keys(). Posteriormente se verifica la seleccion de la tarjeta ingresada con .is_enabled() y .text para realizar
la verificación de los datos y la seleción del método de pago.
  - #### Prueba 5. 
    Se crean los métodos para ingresar el mensaje del conductor en el campo de entrada con .send_keys() y 
.get_propierty() para la comprobación del mensaje.
  - #### Prueba 6. 
    Se crean los métodos .click() y is_anable() para la selección de manta y pañuelos comprobando la selección.
  - #### Prueba 7.
    Se crean los métodos .click() y is_anable() para la selección de 2 heñados comprobando la selección.
  - #### Prueba 8.
    Se cxrean los métodos .is_anable(), .click() para la selección del modal y .text compobabando la selección.
  - #### Prueba 9. 
    Se verifica la ventana emergente con los datos del viaje, con el método .text compobabando.

