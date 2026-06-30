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

- ------------------------------------------------------------------------------------------------------------------------

# Device Systems API EV11 – Seguridad y Autenticación

## Descripción

**Device Systems API** es una aplicación backend desarrollada con FastAPI para la gestión de usuarios, dispositivos y préstamos mediante una API REST.

En esta versión (**EV11**), la aplicación incorpora mecanismos avanzados de seguridad para proteger los recursos y garantizar un acceso controlado a la información. Se implementa autenticación mediante JWT (JSON Web Tokens), autorización basada en roles (RBAC), protección de rutas con OAuth2, control de peticiones mediante Rate Limiting y configuración segura de CORS.

---

## Funcionalidades

La aplicación permite:

###  Autenticación Avanzada

* Registro seguro de usuarios.
* Inicio de sesión mediante credenciales.
* Contraseñas protegidas mediante hashing con Passlib y Bcrypt.

###  Tokens JWT

* Generación de tokens de acceso seguros.
* Validación automática de tokens en rutas protegidas.
* Gestión de sesiones mediante Bearer Token.

###  Control de Acceso por Roles (RBAC)

* Roles disponibles:

  * Admin
  * Support
  * User
* Restricción de operaciones según permisos asignados.

### 🛡 Protección de Rutas

* Endpoints privados protegidos mediante OAuth2.
* Respuestas automáticas:

  * 401 Unauthorized para usuarios no autenticados.
  * 403 Forbidden para usuarios sin permisos.

### Middleware Personalizado

* Registro de peticiones.
* Medición de tiempo de respuesta.
* Generación de identificadores únicos de solicitud.
* Inclusión de cabeceras personalizadas:

  * X-App-Name
  * X-Process-Time
  * X-Request-ID

###  Rate Limiting

* Limitación de peticiones por dirección IP.
* Prevención de ataques de fuerza bruta y abuso de recursos.

###  Configuración de CORS

* Acceso restringido únicamente a clientes autorizados.
* Protección frente a solicitudes cruzadas no confiables.

###  Persistencia de Datos

* Base de datos SQLite.
* ORM SQLAlchemy.
* Migraciones administradas con Alembic.

---

## Tecnologías Utilizadas

| Tecnología       | Descripción                    |
| ---------------- | ------------------------------ |
| Python 3.x       | Lenguaje principal             |
| FastAPI          | Framework para APIs REST       |
| SQLAlchemy       | ORM para acceso a datos        |
| Alembic          | Migraciones de base de datos   |
| SQLite           | Motor de base de datos         |
| Pydantic v2      | Validación de datos            |
| Passlib + Bcrypt | Hash seguro de contraseñas     |
| Python-JOSE      | Generación y validación de JWT |
| SlowAPI          | Rate Limiting                  |
| Uvicorn          | Servidor ASGI                  |
| Swagger UI       | Documentación interactiva      |
| ReDoc            | Documentación alternativa      |

---

## Estructura del Proyecto

```text
device_systems/
│
├── app/
│   ├── main.py
│   │
│   ├── auth/
│   │   ├── auth_routes.py
│   │   ├── auth_service.py
│   │   └── security.py
│   │
│   ├── database/
│   │   └── connection.py
│   │
│   ├── models/
│   │   ├── user_model.py
│   │   ├── device_model.py
│   │   └── loan_model.py
│   │
│   ├── schemas/
│   │   ├── auth_schema.py
│   │   ├── user_schema.py
│   │   ├── device_schema.py
│   │   └── loan_schema.py
│   │
│   ├── routes/
│   │   ├── user_routes.py
│   │   ├── device_routes.py
│   │   └── loan_routes.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   ├── device_service.py
│   │   └── loan_service.py
│   │
│   └── dependencies/
│       ├── database_dependency.py
│       └── auth_dependency.py
│
├── alembic/
├── device_systems.db
├── alembic.ini
├── requirements.txt
└── README.md
```

---

## Instalación y Ejecución

### 1. Activar entorno virtual

```bash
source .venv/Scripts/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Aplicar migraciones

```bash
alembic upgrade head
```

### 4. Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

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

## Endpoints de Autenticación

| Método | Endpoint       | Descripción                          | Protegido |
| ------ | -------------- | ------------------------------------ | --------- |
| POST   | /auth/register | Registro de usuarios                 | No        |
| POST   | /auth/login    | Inicio de sesión y generación de JWT | No        |
| GET    | /auth/me       | Información del usuario autenticado  | Sí        |

---

## Configuración de Seguridad

### CORS

La API permite solicitudes únicamente desde:

```text
http://localhost:3000
http://localhost:5173
```

No se utiliza el comodín (`*`) debido a que, en entornos de producción, permitiría que cualquier dominio pudiera interactuar con la API, aumentando significativamente los riesgos de seguridad cuando se utilizan credenciales o tokens de autenticación.

### Rate Limiting

Se configuró un límite de peticiones por dirección IP para prevenir abuso de los endpoints.

Ejemplos:

* Login: 5 solicitudes por minuto.
* Registro: 3 solicitudes por minuto.
* Usuarios: 30 solicitudes por minuto.

Cuando se supera el límite permitido, la API responde con:

```http
429 Too Many Requests
```

---

## Evidencias de Pruebas

### 1. Estructura del proyecto
<img width="171" height="233" alt="cp1 2" src="https://github.com/user-attachments/assets/54f71fff-81c9-4f1e-939f-465c433866dd" />
<img width="191" height="466" alt="cp1" src="https://github.com/user-attachments/assets/08a9a928-67cd-408d-bdac-76a380f08c4b" />



### 2. Migración Alembic aplicada
<img width="184" height="34" alt="cp2" src="https://github.com/user-attachments/assets/5402cfed-3e10-4bc4-bc9a-aaf9c8708aaf" />



```bash
alembic upgrade head
```

### 3. Registro de usuario

<img width="461" height="371" alt="cp3" src="https://github.com/user-attachments/assets/2635ac17-0456-4ec2-9eff-32ee66538642" />


### 4. Login y token generado

<img width="455" height="416" alt="cp4" src="https://github.com/user-attachments/assets/872dce2c-3912-44d7-9bc5-22b555e2e7d7" />


### 5. Endpoint /auth/me

<img width="251" height="171" alt="cp5" src="https://github.com/user-attachments/assets/820ef073-52a0-4ab1-8e93-b5a0b7853ad7" />


### 6. Acceso sin token

<img width="416" height="287" alt="cp6" src="https://github.com/user-attachments/assets/f863b086-dea9-4c1b-9965-07731cba98ed" />


### 7. Acceso con rol no permitido
<img width="407" height="340" alt="cp7" src="https://github.com/user-attachments/assets/354d828c-615b-4bc9-8191-251651749292" />


### 8. Swagger con OAuth2

<img width="352" height="324" alt="cp8" src="https://github.com/user-attachments/assets/fcd8f094-6d3f-4320-9e4f-596e4ec5dbc2" />


### 9. Cabeceras del middleware
<img width="440" height="352" alt="cp9" src="https://github.com/user-attachments/assets/4d660f05-fe54-430b-baf8-db7c6340e31b" />


* X-App-Name
* X-Process-Time
* X-Request-ID

### 10. Rate Limiting
<img width="478" height="342" alt="cp10" src="https://github.com/user-attachments/assets/01c246a4-4ada-42bc-ade1-a180eb7a30c1" />

 

```http
429 Too Many Requests
```

---

## Reflexión Final

La seguridad en una API REST es fundamental porque los endpoints se encuentran expuestos a través de la red y representan el punto de acceso a los recursos y datos del sistema.

La implementación de mecanismos como JWT, OAuth2, hashing de contraseñas, control de acceso por roles, middleware de monitoreo y Rate Limiting permite reducir significativamente los riesgos asociados a accesos no autorizados, ataques de fuerza bruta y abuso de recursos.

Gracias a estas prácticas, la aplicación garantiza la confidencialidad, integridad y disponibilidad de la información, acercándose a los estándares utilizados en entornos profesionales de desarrollo backend.

