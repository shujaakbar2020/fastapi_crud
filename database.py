from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://RDuTlIxlEDEPsDSFMSqaOBQCZuTUPCwM:AC3ru4DMpxRyXCFgg1BDNNwF3qUT62TSjNu2X1SNWsRtTAmm9U6IvgPM29qDLXD0@localhost:5432/fastapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()