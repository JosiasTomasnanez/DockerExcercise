# DOCKER_SETUP.md

# Proyecto: Hola Mundo con Flask

Este proyecto es un servidor web simple usando **Flask** y Redis, totalmente containerizado con Docker.

---

## 1️⃣ Cómo construir la imagen

1. Abre la terminal en la carpeta raíz del proyecto (donde está tu Dockerfile).
2. Ejecuta el siguiente comando para construir la imagen Docker:

```bash
docker build -t contador-visitas-flask .
```

- `-t contador-visitas-flask` es el nombre que le damos a la imagen.
- `.` indica que Docker debe usar el Dockerfile en el directorio actual.

> Este comando instalará todas las dependencias de Python y del sistema dentro del contenedor.

---

## 2️⃣ Cómo ejecutar el contenedor

1. Una vez construida la imagen, ejecuta el contenedor con:

```bash
docker run -d -p 5000:5000 --name flask_app contador-visitas-flask
```

- `-d` ejecuta el contenedor en segundo plano.
- `-p 5000:5000` mapea el puerto 5000 del contenedor al 5000 de tu máquina.
- `--name flask_app` le da un nombre al contenedor.
- `hola-mundo-flask` es el nombre de la imagen que creamos previamente.

2. Para ver los logs y verificar que Flask arrancó correctamente:

```bash
docker logs -f flask_app
```

---

## 3️⃣ Cómo verificar que funciona correctamente

1. Abre tu navegador y ve a:

```
http://localhost:5000
```

2. Deberías ver un mensaje tipo:

```
Hola Mundo desde Flask!
```

3. Verificar que Redis está corriendo dentro del contenedor:

```bash
docker exec -it flask_app redis-cli ping
```

- Debería responder `PONG`.

---

## 4️⃣ Parar y eliminar el contenedor

- Para parar el contenedor:

```bash
docker stop flask_app
```

- Para eliminar el contenedor:

```bash
docker rm flask_app
```

- Para eliminar la imagen:

```bash
docker rmi hola-mundo-flask
```

