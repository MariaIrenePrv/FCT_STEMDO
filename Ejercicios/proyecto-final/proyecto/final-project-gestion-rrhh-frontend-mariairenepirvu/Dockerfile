FROM node:16-alpine AS build
 
WORKDIR /app
 
#importante copiar todos los archivos .json y lock
 
COPY package.json package-lock.json ./
 
#instalacion de dependencias
 
RUN npm install
 
COPY . .
 
RUN npm run build
 
FROM nginx:alpine
#copia de achivos a nginx 
COPY --from=build app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
 
CMD ["nginx", "-g", "daemon off;"]