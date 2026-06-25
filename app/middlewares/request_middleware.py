import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import logging

# Configuración básica de logs en consola
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("device_systems.middleware")

class SecurityAndTraceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. Generar o capturar el ID de la petición (Correlation ID)
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        
        # 2. Registrar el inicio y medir el tiempo
        start_time = time.time()
        
        # Procesar la petición original
        response = await call_next(request)
        
        # Calcular el tiempo total transcurrido
        process_time = time.time() - start_time
        
        # 3. Inyectar las cabeceras obligatorias exigidas por la guía
        response.headers["X-App-Name"] = "device_systems"
        response.headers["X-Process-Time"] = f"{process_time:.4f}"
        response.headers["X-Request-ID"] = request_id
        
        # 4. Registrar en los logs de la consola el método, ruta y estatus HTTP
        logger.info(
            f"Method: {request.method} | Path: {request.url.path} | "
            f"Status: {response.status_code} | Time: {process_time:.4f}s | Request-ID: {request_id}"
        )
        
        return response