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


<!-- img2 -->
**Imagen 2 — GET /users**


<!-- img3 -->
**Imagen 3 — POST /users**


<!-- img4 -->
**Imagen 4 — PUT /users/{id}**


<!-- img5 -->
**Imagen 5 — PATCH /users/{id}**


<!-- img6 -->
**Imagen 6 — DELETE /users/{id}**


<!-- img7 -->
**Imagen 7 —  Estructura del Proyecto**


---

## Aprendizajes

- Desarrollo de APIs REST con FastAPI
- Arquitectura modular backend
- Uso de servicios, rutas y dependencias
- Manejo de errores HTTP
- Validación con Pydantic
- Documentación automática con Swagger