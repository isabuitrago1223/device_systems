from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite:///./device_systems.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# --- ESTA ES LA FUNCIÓN QUE TE HACÍA FALTA ---
def get_db():
    """Genera una sesión de base de datos para cada petición y la cierra al terminar."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()