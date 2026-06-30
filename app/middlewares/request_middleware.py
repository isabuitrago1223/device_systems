import time
import uuid
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Configuración de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("device_systems.middleware")


class SecurityAndTraceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        # Generar un identificador único para cada petición
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))

        # Registrar el tiempo de inicio
        start_time = time.time()

        # Procesar la petición
        response = await call_next(request)

        # Calcular el tiempo de procesamiento
        process_time = time.time() - start_time

        # Agregar cabeceras personalizadas
        response.headers["X-App-Name"] = "device_systems"
        response.headers["X-Process-Time"] = f"{process_time:.4f}"
        response.headers["X-Request-ID"] = request_id

        # Registrar información en la consola
        logger.info(
            f"Method: {request.method} | "
            f"Path: {request.url.path} | "
            f"Status: {response.status_code} | "
            f"Time: {process_time:.4f}s | "
            f"Request-ID: {request_id}"
        )

        return response