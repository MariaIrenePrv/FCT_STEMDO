# Construcción
FROM node:16-alpine AS build

# Directorio de trabajo
WORKDIR /app

# Copia los archvios de definición de dependencias .json y lock
COPY package.json package-lock.json ./

# Instalación de dependencias
RUN npm install

# Copia el resto de archivos del proyecto
COPY . .

# Construcción aplicación 
RUN npm run build


FROM nginx:alpine

# Copia de achivos a nginx 
COPY --from=build app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
# Expone el puerto 80 
EXPOSE 80

# Comando para ejecutar el contenedor
CMD ["nginx", "-g", "daemon off;"]