




# Dockerfile para el backend Flask usando pipenv
FROM python:3.11-slim

# Instala pipenv
RUN pip install pipenv

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de dependencias
COPY Pipfile* ./

# Instala las dependencias del proyecto
RUN pipenv install --deploy --ignore-pipfile

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto por defecto de Flask
EXPOSE 5000

# Comando para ejecutar la aplicación con pipenv
CMD ["pipenv", "run", "python", "app.py"]
