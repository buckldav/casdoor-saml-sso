from uuid import UUID
from fastapi_sessions.backends.implementations import InMemoryBackend
from .models import SessionData

backend = InMemoryBackend[UUID, SessionData]()
