# Alternova_Prueba

CONFIGURAR EL ENVIROMENT EN LA CONSOLA DE WINDOWS

1 Crear una carpeta en donde va estar el "Enviroment" del programa y descargar todos los archivos ahí

2 Abrir la consola de comandos de Windows (Escribir cmd en el buscador y abrir "símbolo de sistema")

3 En la consola Escribir:

	 1. cd (comando para navegar entre carpetas)
  
	 2. Pegar la ruta de la carpeta creada en el paso 1

4 En la consola escribir para crear el "Enviroment": 

	python -m venv .venv

5 Para activar el "Enviroment" escribir en la consola:

	.venv\Scripts\activate.bat

6 Dentro de la descarga hay un archivo llamado requirements.txt en donde están los packages necesarios para el programa. Para activarlos escribir en la consola:

	pip install -r requirements.txt


---------------------------------------------------------------------------------------------------

CONFIGURAR TWILIO

1 Entrar a twilio y crear una cuenta

2 en "account dashboard" en la pestaña de develop desplegar "messaging" - "try it out" y seleccionar "Send a Whatsapp message

3 Seguir los pasos de la pagina para conectarte con "el Sandbox"

4 Luego en la ventana "Request" señalar la pestaña "Python" 

5 Copiar los valores correspondientes a account_sid y auth_token

6 Abrir el archivo credenciales

7 Editar el archivo según los valores copiados incluyendo el número de teléfono que se conectó con el sandbox

8 Guardar el archivo credenciales y cerrar

9 Ejecutar el programa ingresando en la consola de comandos 

	python PRUEBA.py

Nota: Revisar que la ruta que muestra la consola sea la correspondiente a la del "Enviroment" configurado anteriormente y que el archivo PRUEBA.py y credenciales, se encuentre en esa ruta
