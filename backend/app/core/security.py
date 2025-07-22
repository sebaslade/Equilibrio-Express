import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv

load_dotenv()
# Clave secreta para firmar el JWT (debe estar en tu .env)
SECRET_KEY = os.getenv("SECRET_KEY")
# Algoritmo para firmar el JWT (debe estar en tu .env)
ALGORITHM = os.getenv("ALGORITHM", "HS256")
# Tiempo de expiración del token en minutos (debe estar en tu .env)
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

if not SECRET_KEY:
    raise ValueError("La variable de entorno SECRET_KEY no está definida en el archivo .env")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return None
        return email
    except JWTError:
        return None