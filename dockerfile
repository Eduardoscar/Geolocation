# Utilizar la imagen oficial de Python 3
FROM python:3

# Seleccionar el directorio donde trabajaremos
# Copiar el codigo fuente al directorio de trabajo
COPY ./src/ /usr/src/main
WORKDIR /usr/main
COPY ./src/ /usr/src/controllerGeolocationAutomatic
WORKDIR /usr/controllerGeolocationAutomatic
COPY ./src/ /usr/src/geolocationAutomatic
WORKDIR /usr/geolocationAutomatic
COPY ./src/ /usr/src/settings
WORKDIR /usr/settings

# Instalar flask y sus dependencias.
RUN python -m pip install --upgrade pip
RUN pip install fastapi==0.81.0
RUN pip install uvicorn==0.18.2
RUN pip install starlette==0.20.4
RUN pip install requests==2.27.1
RUN pip install python-dotenv==0.20.0
RUN pip install pytest-reporter-html1
# Abrir el puerto 80 del contendor
EXPOSE 5000

# Injectar variable de configuracion para flask
ENV FASTAPI_APP=settings.py

# Iniciar el servicio
CMD [ "uvicorn", "main:app", "--host=0.0.0.0" ]