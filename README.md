# API INSTITUTO
Desarrollo de API mediante Framework FastApi en Python para pruebas de Backend de LogicSystems.
¡Bienvenido al repositorio de la API de Instituto con FastAPI! Esta API es una aplicación web de Python que utiliza el framework FastAPI para crear servicios web rápidos y de alto rendimiento. Proporciona una forma sencilla y eficiente de construir APIs RESTful con soporte para validación automática, documentación interactiva y mucho más.

## Características

- Basada en el framework FastAPI, que ofrece una gran velocidad y rendimiento.
- Soporte para validación automática de datos de entrada y salida.
- Documentación interactiva generada automáticamente con Swagger UI.
- Implementación de CRUD (Crear, Leer, Actualizar, Eliminar) para diversos recursos.
- Configuración sencilla y flexible.

## Requisitos previos

Antes de instalar y ejecutar esta API, asegúrate de tener instaladas las siguientes herramientas:

- Python (versión 3.7 o superior)
- Pip (gestor de paquetes de Python)

`https://www.python.org/downloads/`

## Instalación

1. Clona este repositorio en tu máquina local:
<pre><code> git clone https://github.com/PeterPerez01/instituto_api.git </code></pre>


2. Accede al directorio del repositorio:
<pre><code> cd instituto_api </code></pre>


3. Crea un entorno virtual para el proyecto:
<pre><code>python -m venv venv</code></pre>


4. Activa el entorno virtual:

- En Windows:

  ```
  venv\Scripts\activate
  ```

- En Linux o macOS:

  ```
  source venv/bin/activate
  ```

5. Instala las dependencias del proyecto:
<pre><code> pip install -r requirements.txt </code></pre>


6. Ejecuta la API:
Entra en la carpeta main y abre una consola para ejecutar el comando
<pre><code> uvicorn api:app --reload </code></pre>


¡Listo! La API ahora está en funcionamiento en tu máquina local.

## Uso

Para acceder a la documentación interactiva de la API, abre tu navegador web y visita la siguiente URL: `http://localhost:8000/docs`. Aquí podrás explorar todos los endpoints disponibles, probarlos e incluso ver ejemplos de solicitud y respuesta.

Como opción alternativa puedes usar la URL: `http://localhost:8000/redoc`.

Si deseas modificar la configuración de la API o agregar nuevos endpoints, consulta el código fuente del proyecto y realiza los cambios necesarios. Luego, reinicia la API para que los cambios surtan efecto.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama para tu nueva característica o corrección de errores: `git checkout -b nueva-caracteristica`.
3. Realiza los cambios necesarios y commitea tus modificaciones: `git commit -am 'Agrega nueva característica'`.
4. Envía tus cambios a tu repositorio remoto: `git push origin nueva-caracteristica`.
5. Abre una pull request en este repositorio.

¡Agradecemos todas las contribuciones!

## Licencia

Este proyecto se encuentra bajo la [Licencia MIT](LICENSE).
