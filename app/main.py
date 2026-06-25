from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Importación de rutas
from app.auth.auth_routes import router as auth_router
from app.routes import user_routes, device_routes, loan_routes  # Rutas de tus fases anteriores

# Importación del middleware personalizado
from app.middlewares.request_middleware import SecurityAndTraceMiddleware

# Importación de guardianes de rutas
from app.dependencies.auth_dependency import get_current_active_user

# --- Configuración de Rate Limiting (SlowAPI) ---
limiter = Limiter(key_func=get_remote_address)

# --- Fase 12: Inicializar FastAPI con metadatos requeridos ---
app = FastAPI(
    title="device_systems API",
    description="API REST segura para gestión de usuarios, dispositivos y préstamos",
    version="3.0.0"
)

# Acoplar el limitador de peticiones y su manejador de errores a la app
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# --- Fase 9: Configuración de CORS ---
origins = [
    "http://localhost:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Fase 10: Registrar Middleware Personalizado ---
app.add_middleware(SecurityAndTraceMiddleware)


# --- Aplicación de Rate Limiting en Endpoints (Fase 11) ---

@app.post("/auth/login", tags=["Auth"])
@limiter.limit("5/minute")
async def login_limited(request: Request):
    pass

@app.post("/auth/register", tags=["Auth"])
@limiter.limit("3/minute")
async def register_limited(request: Request):
    pass


# --- Inclusión de Routers al Sistema Principal ---

# Rutas de autenticación (Abiertas y autoprotegidas internamente)
app.include_router(auth_router)

# --- Fase 8: Protección de rutas existentes mediante dependencias globales ---
app.include_router(
    user_routes.router,
    dependencies=[Depends(get_current_active_user)]
)

app.include_router(
    device_routes.router
    # Nota: Recuerda proteger los endpoints individuales adentro de device_routes.py
)

app.include_router(
    loan_routes.router,
    dependencies=[Depends(get_current_active_user)]
)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bienvenido a device_systems API Segura v3.0.0"}