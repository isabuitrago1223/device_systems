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

- -------------------------------------------------------------------------------------------------------------------------

# Device Systems API EV10

## Descripción

Device Systems API es una aplicación backend desarrollada con FastAPI para la gestión de usuarios, dispositivos y préstamos mediante una API REST.

En esta versión (EV10), la aplicación evoluciona incorporando relaciones entre entidades mediante SQLAlchemy ORM, migraciones con Alembic y gestión completa de préstamos de dispositivos.

La API permite administrar usuarios, dispositivos y préstamos, garantizando la integridad de los datos mediante relaciones entre tablas, validaciones con Pydantic y documentación automática con Swagger/OpenAPI.

---

## Funcionalidades

La aplicación permite:

* Crear usuarios.
* Consultar usuarios.
* Actualizar usuarios.
* Eliminar usuarios.
* Crear dispositivos.
* Consultar dispositivos.
* Actualizar dispositivos.
* Eliminar dispositivos.
* Registrar préstamos de dispositivos.
* Consultar préstamos.
* Devolver dispositivos prestados.
* Consultar detalles de préstamos.
* Aplicar relaciones entre tablas mediante SQLAlchemy.
* Aplicar validaciones con Pydantic v2.
* Gestionar migraciones con Alembic.
* Generar documentación automática con Swagger UI y ReDoc.

---

## Tecnologías Utilizadas

* Python 3.x
* FastAPI
* SQLAlchemy
* SQLite
* Alembic
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
│   │   ├── user_model.py
│   │   ├── device_model.py
│   │   └── loan_model.py
│   │
│   ├── schemas/
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
│       └── database_dependency.py
│
├── alembic/
│   └── versions/
│
├── device_systems.db
├── alembic.ini
├── requirements.txt
└── README.md
```

---

## Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/TU-USUARIO/device_systems.git
cd device_systems
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

### 3. Activar entorno virtual

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución del Proyecto

```bash
uvicorn app.main:app --reload
```

Salida esperada:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## Base de Datos

La aplicación utiliza SQLite como motor de base de datos.

Archivo generado:

```text
device_systems.db
```

Las tablas son creadas mediante SQLAlchemy y administradas mediante Alembic.

Tablas principales:

* users
* devices
* loans

---

## Migraciones Alembic

Crear migración:

```bash
alembic revision --autogenerate -m "create devices and loans tables"
```

Aplicar migraciones:

```bash
alembic upgrade head
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

## Endpoints Disponibles

### Users

| Método | Endpoint    |
| ------ | ----------- |
| GET    | /users      |
| GET    | /users/{id} |
| POST   | /users      |
| PUT    | /users/{id} |
| PATCH  | /users/{id} |
| DELETE | /users/{id} |

### Devices

| Método | Endpoint      |
| ------ | ------------- |
| GET    | /devices      |
| GET    | /devices/{id} |
| POST   | /devices      |
| PUT    | /devices/{id} |
| PATCH  | /devices/{id} |
| DELETE | /devices/{id} |

### Loans

| Método | Endpoint           |
| ------ | ------------------ |
| GET    | /loans             |
| GET    | /loans/{id}        |
| POST   | /loans             |
| PATCH  | /loans/{id}/return |

---

## Relaciones Implementadas

### User → Loan

Un usuario puede tener múltiples préstamos.

### Device → Loan

Un dispositivo puede tener múltiples préstamos.

### Loan → User

Cada préstamo pertenece a un usuario.

### Loan → Device

Cada préstamo pertenece a un dispositivo.

---

## Validaciones Implementadas

### Usuarios

* Nombre obligatorio.
* Correo válido.
* Correo único.
* Rol obligatorio.

### Dispositivos

* Nombre obligatorio.
* Número de serie único.
* Tipo de dispositivo obligatorio.

### Préstamos

* Usuario existente.
* Dispositivo existente.
* Dispositivo disponible para préstamo.

---

## Pruebas Funcionales

Se realizaron pruebas para verificar:

1. Crear usuario.
2. Consultar usuarios.
3. Crear dispositivo.
4. Consultar dispositivos.
5. Filtrar dispositivos.
6. Crear préstamo.
7. Evitar préstamo de dispositivo no disponible.
8. Consultar préstamos.
9. Consultar préstamo por ID.
10. Devolver dispositivo.
11. Verificar disponibilidad después de devolución.
12. Documentación Swagger.
13. Documentación ReDoc.

---

## Evidencias

## Evidencias

### Captura 1 - Inicialización de Alembic
<img width="560" height="406" alt="c1" src="https://github.com/user-attachments/assets/aa7a58bc-167f-4631-b0dc-add693324686" />


### Captura 2 - Configuración de env.py

<img width="339" height="139" alt="c2" src="https://github.com/user-attachments/assets/064468cd-9b3e-4d48-bc2d-25ac2b78e893" />


### Captura 3 - Generación de migración

<img width="500" height="435" alt="c3" src="https://github.com/user-attachments/assets/ecdef7c5-d073-4012-a452-ee013eb93feb" />


### Captura 4 - Aplicación de migración
<img width="629" height="79" alt="c4" src="https://github.com/user-attachments/assets/aadfb339-806a-4697-bf19-e23e9b77a918" />


### Captura 5 - Historial de migraciones
<img width="449" height="67" alt="c5" src="https://github.com/user-attachments/assets/d1f20a57-a1a5-47f7-871c-2c2cfb2cb0ca" />


### Captura 6 - Tablas creadas en SQLite
<img width="673" height="63" alt="c6" src="https://github.com/user-attachments/assets/2162e16b-0bb2-4ce1-ae4c-bd3c6639398f" />



### Captura 7 - Swagger - Users

<img width="550" height="153" alt="c7" src="https://github.com/user-attachments/assets/82406d14-34d5-4766-9fd7-f0115a1363b1" />


### Captura 8 - Swagger - Devices
<img width="547" height="158" alt="c9" src="https://github.com/user-attachments/assets/c02279e2-58b0-4888-9a10-b64a5d70642f" />
<img width="547" height="158" alt="c8" src="https://github.com/user-attachments/assets/3a1481bc-ed7d-4d1f-8314-a7b4e927af17" />


### Captura 9 - Swagger - Loans

![Uploading c9.png…]()

### Captura 10 - Creación de usuario
<img width="457" height="433" alt="C10" src="https://github.com/user-attachments/assets/480b9ca8-d4b5-48de-9b48-0dfd1972536f" />


### Captura 11 - Creación de dispositivo
<img width="455" height="437" alt="C11" src="https://github.com/user-attachments/assets/59715138-5566-4c86-a67e-becbf3b46bb4" />


### Captura 12 - Creación de préstamo
<img width="453" height="436" alt="C12" src="https://github.com/user-attachments/assets/7be9d5ec-91c8-4d83-b716-bfebe2820b6f" />


### Captura 13 - Intento de préstamo duplicado
<img width="453" height="426" alt="C13" src="https://github.com/user-attachments/assets/bc2fc8e0-1059-4d05-8c36-7ec3f274eef3" />


### Captura 14 - Consulta de préstamos
<img width="455" height="280" alt="C14" src="https://github.com/user-attachments/assets/4d688a43-60dd-4834-af61-4685daf1cf3f" />


### Captura 15 - Consulta de préstamos activos
<img width="468" height="292" alt="C15" src="https://github.com/user-attachments/assets/bff3608f-2095-4a8a-86bf-e8f176492cfc" />


### Captura 16 - Devolución de dispositivo
<img width="450" height="309" alt="C16" src="https://github.com/user-attachments/assets/6d11e2f0-39a1-4258-b5da-701635f1b97f" />


### Captura 17 - Verificación de disponibilidad del dispositivo
<img width="458" height="311" alt="C17" src="https://github.com/user-attachments/assets/8b96a251-e01a-4ee8-ac1e-040a2e852ac6" />



## Reflexión Final

Durante el desarrollo de esta actividad se fortalecieron los conocimientos sobre modelado relacional utilizando SQLAlchemy ORM, relaciones entre entidades, migraciones con Alembic y construcción de APIs REST más cercanas a escenarios reales.

La implementación de usuarios, dispositivos y préstamos permitió comprender cómo gestionar relaciones entre tablas, mantener integridad referencial y automatizar cambios en la base de datos mediante migraciones.

Además, se consolidó el uso de FastAPI, Pydantic y SQLAlchemy para construir aplicaciones backend más robustas, escalables y mantenibles.
