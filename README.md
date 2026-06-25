#  Device Systems API — EV07

---

## Descripción

**Device Systems API** es una aplicación backend desarrollada con FastAPI para la gestión de usuarios mediante una API REST.

Este proyecto fue realizado con el propósito de aplicar los conceptos fundamentales de FastAPI, incluyendo:

- Validación de datos con Pydantic v2
- Uso de métodos HTTP
- Parámetros de ruta (Path Parameters)
- Parámetros de consulta (Query Parameters)
- Modelos de respuesta
- Documentación automática con Swagger UI

---

## Funcionalidades

La aplicación permite:

- Consultar todos los usuarios registrados
- Buscar usuarios por identificador
- Filtrar usuarios por rol
- Filtrar usuarios por estado activo o inactivo
- Registrar nuevos usuarios
- Validar datos mediante Pydantic v2
- Evitar el registro de correos electrónicos duplicados
- Implementar cabeceras HTTP personalizadas

---

## Tecnologías utilizadas

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic v2
- Swagger UI
- Git
- GitHub

---

## Estructura del proyecto

```
device_systems/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── user_routes.py
│   │
│   └── schemas/
│       ├── __init__.py
│       └── user_schema.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/device_systems.git
cd device_systems
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

### 3. Activar entorno virtual

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución del servidor

```bash
uvicorn app.main:app --reload
```

Luego acceder a:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## Endpoints

| Método | Endpoint               | Descripción                    |
|--------|------------------------|--------------------------------|
| GET    | `/users`               | Obtener todos los usuarios     |
| GET    | `/users/{user_id}`     | Obtener usuario por ID         |
| GET    | `/users?role=admin`    | Filtrar usuarios por rol       |
| GET    | `/users?is_active=true`| Filtrar usuarios activos       |
| POST   | `/users`               | Registrar un nuevo usuario     |

---

## Modelo de Usuario

| Campo     | Tipo     | Validación                  |
|-----------|----------|-----------------------------|
| id        | integer  | Obligatorio                 |
| name      | string   | Mínimo 3 caracteres         |
| email     | EmailStr | Correo válido               |
| role      | string   | `admin`, `support` o `user` |
| is_active | boolean  | `true` o `false`            |

---

## Ejemplos de peticiones

### GET /users

```json
[
  {
    "id": 1,
    "name": "Isabella Buitrago",
    "email": "isa@gmail.com",
    "role": "admin",
    "is_active": true
  }
]
```

### GET /users/{user_id}

```json
{
  "id": 1,
  "name": "Isabella Buitrago",
  "email": "isa@gmail.com",
  "role": "admin",
  "is_active": true
}
```

### POST /users

```json
{
  "id": 5,
  "name": "Andrea",
  "email": "andrea@gmail.com",
  "role": "user",
  "is_active": true
}
```

---

## Validaciones implementadas

### Nombre
Debe tener mínimo 3 caracteres.

```json
{ "name": "Jo" }
```

### Correo electrónico
Debe tener formato válido.

```json
{ "email": "correo_invalido" }
```

### Rol
Valores permitidos: `admin`, `support`, `user`.

```json
{ "role": "manager" }
```

### Correo duplicado

```json
{ "detail": "El correo ya existe" }
```

---

## Cabeceras HTTP

```
X-App-Name: device_systems
X-API-Version: 1.0
```

---

## Evidencias

<!-- cap1 -->
**Captura 1 — Estructura del proyecto**

<!-- cap2 -->
**Captura 2 — Swagger UI**

<!-- cap3 -->
**Captura 3 — GET /users**

<!-- cap4 -->
**Captura 4 — GET /users/{user_id}**

<!-- cap5 -->
**Captura 5 — Filtro por rol**

<!-- cap6 -->
**Captura 6 — Filtro por estado**

<!-- cap7 -->
**Captura 7 — POST /users**

---

## Reflexión final

Durante el desarrollo de esta actividad aprendí a construir una API REST utilizando FastAPI y a organizar un proyecto backend de manera modular.

La implementación de modelos con Pydantic me permitió comprender la importancia de validar la información para garantizar la integridad de los datos.

Asimismo, apliqué conceptos como Path Parameters y Query Parameters para realizar consultas más específicas, además de Response Models para controlar la información retornada por la API.

La documentación automática con Swagger UI facilitó las pruebas de cada endpoint y permitió verificar el correcto funcionamiento de la aplicación.

Esta experiencia fortaleció mis conocimientos en el desarrollo de servicios web con Python y el uso de herramientas modernas para crear APIs seguras, organizadas y mantenibles.


----------------------------------------------------------------------------------------------------------------------------------

#  Device Systems API — EV08

---

## Descripción

**Device Systems API** es una API REST desarrollada con FastAPI para la gestión de usuarios del sistema `device_systems`.

Esta aplicación permite realizar operaciones CRUD completas sobre el recurso `users`, aplicando buenas prácticas de arquitectura backend.

---

## Funcionalidades

- Crear usuarios
- Listar usuarios
- Consultar usuario por ID
- Filtrar usuarios por rol y estado
- Actualizar usuarios completamente (PUT)
- Actualizar usuarios parcialmente (PATCH)
- Eliminar usuarios
- Validar datos con Pydantic v2
- Manejo de errores con HTTPException
- Uso de Dependency Injection (Depends)
- Documentación automática con Swagger UI y ReDoc

---

## Tecnologías utilizadas

- Python 3
- FastAPI
- Uvicorn
- Pydantic v2
- Swagger UI
- ReDoc
- Git & GitHub
- Postman / Thunder Client
- Visual Studio Code

---

## Estructura del proyecto

```
device_systems/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   └── user_routes.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   ├── dependencies/
│   │   └── user_dependencies.py
│   │
│   └── data/
│       └── users_db.py
│
├── requirements.txt
└── README.md
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/device_systems.git
cd device_systems
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

**Windows (PowerShell):**

```bash
venv\Scripts\Activate.ps1
```

**CMD:**

```bash
venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install fastapi uvicorn pydantic[email]
```

---

## Ejecución del servidor

```bash
uvicorn app.main:app --reload
```

- **URL local:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## Endpoints

| Método | Endpoint               | Descripción                     |
|--------|------------------------|---------------------------------|
| GET    | `/users`               | Listar usuarios                 |
| GET    | `/users/{user_id}`     | Obtener usuario por ID          |
| GET    | `/users?role=user`     | Filtrar por rol                 |
| GET    | `/users?is_active=true`| Filtrar por estado              |
| POST   | `/users`               | Crear usuario                   |
| PUT    | `/users/{user_id}`     | Actualizar usuario completo     |
| PATCH  | `/users/{user_id}`     | Actualizar parcialmente         |
| DELETE | `/users/{user_id}`     | Eliminar usuario                |
| GET    | `/users/config/info`   | Información de configuración    |

---

## Modelo de Usuario

| Campo     | Tipo     | Validación                 |
|-----------|----------|----------------------------|
| id        | int      | Obligatorio                |
| name      | str      | Mínimo 3 caracteres        |
| email     | EmailStr | Formato válido             |
| role      | str      | `admin`, `support`, `user` |
| is_active | bool     | `true` / `false`           |

---

## Ejemplos de peticiones

### GET /users

```json
[
  {
    "name": "Isabella Buitrago",
    "email": "isa@gmail.com",
    "role": "admin",
    "is_active": true
  }
]
```

### POST /users

**Request:**

```json
{
  "name": "Isabella Buitrago",
  "email": "isa@gmail.com",
  "role": "user",
  "is_active": true
}
```

**Response:**

```json
{
  "message": "Usuario creado correctamente",
  "user": {
    "id": 3,
    "name": "carlos",
    "email": "carlos@gmail.com",
    "role": "user",
    "is_active": true
  }
}
```

### PUT /users/{id}

```json
{
  "name": "Carlos Actualizadas",
  "email": "carlos_actualizados@gmail.com",
  "role": "support",
  "is_active": true
}
```

### PATCH /users/{id}

```json
{
  "role": "admin"
}
```

### DELETE /users/{id}

```json
{
  "message": "Usuario eliminado correctamente"
}
```

---

## Manejo de errores

```json
{
  "detail": {
    "error": true,
    "message": "Usuario no encontrado",
    "status_code": 404
  }
}
```

---

## Dependency Injection (Depends)

Se implementó inyección de dependencias para reutilizar lógica entre endpoints.

**Beneficios:**

- Código más limpio
- Menos duplicación
- Mejor mantenibilidad
- Arquitectura escalable

---

## Cabeceras HTTP

```
X-App-Name: device_systems
X-API-Version: 1.0
```

---

## Evidencias

<!-- img1 -->
**Imagen 1 — Swagger UI / Endpoints disponibles**
<img width="673" height="293" alt="img2" src="https://github.com/user-attachments/assets/5cc41021-3d4d-4e4e-ae26-b7cc63142a16" />


<!-- img2 -->
**Imagen 2 — GET /users**
<img width="404" height="309" alt="img3" src="https://github.com/user-attachments/assets/89fb579c-4aca-4237-afdf-c9f3bbdd12af" />


<!-- img3 -->
**Imagen 3 — POST /users**
<img width="539" height="110" alt="img4" src="https://github.com/user-attachments/assets/2925e36d-1f11-45ab-a20e-baab4bcd36e9" />


<!-- img4 -->
**Imagen 4 — PUT /users/{id}**
<img width="540" height="151" alt="img5" src="https://github.com/user-attachments/assets/a56ca025-d52c-4def-bb58-42d0bd7d11e2" />




<!-- img5 -->
**Imagen 5 — PATCH /users/{id}**
<img width="540" height="152" alt="img6" src="https://github.com/user-attachments/assets/4c387bcc-7ef6-4326-92b4-582826cdca0b" />


<!-- img6 -->
**Imagen 6 — DELETE /users/{id}**
<img width="543" height="163" alt="img7" src="https://github.com/user-attachments/assets/c51dbd6e-ebb6-4ebc-9592-0519c78399cb" />


<!-- img7 -->
**Imagen 7 —  Estructura del Proyecto**
<img width="172" height="268" alt="img1" src="https://github.com/user-attachments/assets/ca575283-ed1e-44a1-aec4-15bdb0892fb9" />



---

## Aprendizajes

- Desarrollo de APIs REST con FastAPI
- Arquitectura modular backend
- Uso de servicios, rutas y dependencias
- Manejo de errores HTTP
- Validación con Pydantic
- Documentación automática con Swagger

- --------------------------------------------------------------------------------------------------------------------

# Device Systems API EV09

## Descripción
 
Device Systems API es una aplicación backend desarrollada con FastAPI para la gestión de usuarios mediante una API REST.

En esta versión (EV09), la aplicación evoluciona desde una estructura basada en almacenamiento temporal en memoria hacia una solución con persistencia real de datos utilizando SQLAlchemy y SQLite.

La API permite realizar operaciones CRUD completas sobre usuarios almacenados en una base de datos relacional, aplicando validaciones mediante Pydantic, restricciones de integridad y documentación automática con Swagger/OpenAPI.

---

## Funcionalidades

La aplicación permite:

* Crear usuarios en base de datos.
* Consultar todos los usuarios.
* Consultar usuarios por ID.
* Filtrar usuarios por rol.
* Filtrar usuarios por estado activo/inactivo.
* Actualizar usuarios completamente mediante PUT.
* Actualizar usuarios parcialmente mediante PATCH.
* Eliminar usuarios.
* Validar datos utilizando Pydantic v2.
* Evitar correos electrónicos duplicados.
* Aplicar restricciones mediante SQLAlchemy.
* Generar documentación automática con Swagger UI y ReDoc.

---

## Tecnologías Utilizadas

* Python 3.x
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic v2
* Uvicorn
* Swagger UI
* ReDoc
* Git
* GitHub

---

## Estructura del Proyecto

```text
device_systems/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── database/
│   │   └── connection.py
│   │
│   ├── models/
│   │   └── user_model.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   ├── routes/
│   │   └── user_routes.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   └── dependencies/
│       └── database_dependency.py
│
├── device_systems.db
├── requirements.txt
└── README.md
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/device_systems.git
cd device_systems
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

### 3. Activar entorno virtual

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución del Proyecto

Ejecutar:

```bash
uvicorn app.main:app --reload
```

Salida esperada:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## Base de Datos

La aplicación utiliza SQLite para almacenar la información de los usuarios.

Archivo generado:

```text
device_systems.db
```

SQLAlchemy se encarga de crear automáticamente las tablas a partir de los modelos definidos.

---

## Documentación Automática

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## Endpoints Disponibles

| Método | Endpoint         | Descripción                     |
| ------ | ---------------- | ------------------------------- |
| GET    | /                | Mensaje de bienvenida           |
| GET    | /users           | Obtener todos los usuarios      |
| GET    | /users/{user_id} | Buscar usuario por ID           |
| POST   | /users           | Crear usuario                   |
| PUT    | /users/{user_id} | Actualizar usuario completo     |
| PATCH  | /users/{user_id} | Actualizar usuario parcialmente |
| DELETE | /users/{user_id} | Eliminar usuario                |

---

## Modelo SQLAlchemy

La tabla users contiene los siguientes campos:

| Campo      | Tipo     |
| ---------- | -------- |
| id         | Integer  |
| name       | String   |
| email      | String   |
| role       | String   |
| is_active  | Boolean  |
| created_at | DateTime |

### Restricciones Implementadas

* id como Primary Key.
* email único.
* email obligatorio.
* name obligatorio.
* role obligatorio.
* is_active con valor por defecto True.

---

## Schemas Pydantic

### UserCreate

Utilizado para crear usuarios.

### UserUpdate

Utilizado para actualizar usuarios completamente.

### UserPatch

Utilizado para actualizaciones parciales.

### UserResponse

Utilizado para las respuestas de la API.

---

## Validaciones Implementadas

### Nombre

Debe contener mínimo 3 caracteres.

Ejemplo inválido:

```json
{
  "name": "Jo"
}
```

---

### Correo Electrónico

Debe tener formato válido.

Ejemplo inválido:

```json
{
  "email": "correo_invalido"
}
```

---

### Rol

Valores permitidos:

* admin
* support
* user

Ejemplo inválido:

```json
{
  "role": "manager"
}
```

---

### Correo Duplicado

La API no permite registrar usuarios con correos ya existentes.

Respuesta:

```json
{
  "detail": "Correo ya registrado"
}
```

---

## Pruebas Funcionales

Se realizaron pruebas para verificar:

1. Creación de usuarios.
2. Consulta de usuarios.
3. Consulta por ID.
4. Consulta de usuario inexistente.
5. Filtrado por rol.
6. Filtrado por estado.
7. Actualización completa mediante PUT.
8. Actualización parcial mediante PATCH.
9. Eliminación mediante DELETE.
10. Validación de correo duplicado.
11. Validación de correo inválido.
12. Validación de rol inválido.

---

## Evidencias

### Captura 1 - Estructura del proyecto
<img width="118" height="461" alt="evi1" src="https://github.com/user-attachments/assets/4fb58b1e-baff-4daa-bb33-2b7e9a51feb9" />

### Captura 2 - Base de datos SQLite
<img width="125" height="34" alt="evi2" src="https://github.com/user-attachments/assets/13eaafc5-c99c-4726-b272-a123cff0b178" />


### Captura 3 - Swagger UI
<img width="776" height="355" alt="evi3" src="https://github.com/user-attachments/assets/4a75ff4f-d153-4b31-8411-d35a5b859333" />


### Captura 4 - Crear usuario (POST)
<img width="511" height="431" alt="evi4" src="https://github.com/user-attachments/assets/533c6528-4539-431b-b2f4-70a42c26260b" />


### Captura 5 - Correo duplicado
<img width="514" height="421" alt="evi5" src="https://github.com/user-attachments/assets/a2758003-4b3f-4ac9-8a29-b1e95ac56616" />


### Captura 6 - Obtener usuarios (GET)
<img width="499" height="335" alt="evi6" src="https://github.com/user-attachments/assets/7f942a07-137a-4112-b1a4-f6d99e65ff06" />


### Captura 7 - Obtener usuario por ID
<img width="507" height="291" alt="evi7" src="https://github.com/user-attachments/assets/c6d86dfa-4b48-4ac6-bd49-672aba8e9e1c" />


### Captura 8 - Usuario inexistente
<img width="504" height="269" alt="evi8" src="https://github.com/user-attachments/assets/f831896c-7bdf-4857-8a53-eff71dc0990d" />


### Captura 9 - Filtrar por rol
<img width="506" height="352" alt="evi9" src="https://github.com/user-attachments/assets/607ed54b-45f8-4bdc-bbe0-7611c027ae47" />


### Captura 10 - Filtrar por estado
<img width="508" height="350" alt="evi10" src="https://github.com/user-attachments/assets/2fdc8b61-bfcf-4c45-88cf-7fdfa0483b6c" />


### Captura 11 - Actualización completa (PUT)
<img width="443" height="412" alt="evi11" src="https://github.com/user-attachments/assets/f223823e-b1b8-4d43-ac15-19fea2a07d7c" />


### Captura 12 - Actualización parcial (PATCH)
<img width="443" height="398" alt="evi12" src="https://github.com/user-attachments/assets/f9e60e3d-37e3-4209-bab6-cdf2495977ea" />


### Captura 13 - Eliminar usuario (DELETE)
<img width="440" height="238" alt="evi13" src="https://github.com/user-attachments/assets/5692341e-4c93-4e6d-89a0-c9a266b51d51" />


### Captura 14 - Verificación de usuario eliminado
<img width="445" height="241" alt="evi14" src="https://github.com/user-attachments/assets/ae51233a-1f19-4759-bb79-becc7ff8926f" />


### Captura 15 - ReDoc
<img width="959" height="469" alt="evi15" src="https://github.com/user-attachments/assets/8b4aecd7-5aad-4393-9821-8ed5737687bd" />


### Captura 16 - Correo inválido
<img width="542" height="340" alt="evi16" src="https://github.com/user-attachments/assets/b56707c9-c9c8-4551-abe0-3a9468ec5fd1" />


### Captura 17 - Rol inválido
<img width="539" height="340" alt="evi17" src="https://github.com/user-attachments/assets/ca170940-7da1-4832-bf95-6160fd823679" />

---

## Diferencia entre Modelo SQLAlchemy y Schema Pydantic

Los modelos SQLAlchemy representan la estructura de las tablas dentro de la base de datos y permiten realizar operaciones de persistencia sobre los datos.

Por otro lado, los schemas Pydantic se utilizan para validar la información que entra y sale de la API, garantizando que los datos cumplan con las reglas definidas antes de ser procesados.

Esta separación permite mantener una arquitectura más organizada, segura y escalable.

---

## Reflexión Final

Durante el desarrollo de esta actividad se comprendió la importancia de la persistencia de datos en las aplicaciones backend.

La integración de SQLAlchemy con FastAPI permitió reemplazar el almacenamiento temporal en memoria por una base de datos relacional, logrando que la información permanezca disponible incluso después de reiniciar la aplicación.

Además, se fortalecieron conocimientos relacionados con ORM, validaciones mediante Pydantic, manejo de errores, operaciones CRUD y documentación automática mediante Swagger/OpenAPI.

Esta experiencia permitió comprender cómo se construyen APIs REST más robustas, escalables y cercanas a entornos reales de desarrollo profesional.
