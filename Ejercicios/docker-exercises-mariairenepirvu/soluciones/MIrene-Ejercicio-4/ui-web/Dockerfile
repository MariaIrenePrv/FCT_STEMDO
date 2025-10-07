# Imagen Node.js
FROM node:current-alpine3.21

# Directorio de trabajo 
WORKDIR /app

# Copiar los archivos   
COPY package*.json ./

# Copiar el resto de los archivos
COPY . .

# Instalaciones necesarias
RUN yarn install

# Exponer el puerto 
EXPOSE 5173

# Comando para iniciar la aplicación
CMD ["yarn", "dev", "--host"]   