# app/services/jwt_service.py
from builtins import dict, str
import jwt
from datetime import datetime, timedelta
from settings.config import settings
import logging

def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    # Convert role to uppercase before encoding the JWT
    if 'role' in to_encode:
        to_encode['role'] = str(to_encode['role']).split('.')[-1].upper()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=settings.access_token_expire_minutes))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt

def decode_token(token: str):
    try:
        decoded = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        print(f"Decoded token: {decoded}")
        return decoded
    except jwt.PyJWTError:
        print(f"Token decoding failed: {e}")
        return None
