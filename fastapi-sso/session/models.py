from pydantic import BaseModel, EmailStr


class SessionData(BaseModel):
    name: str
    email: EmailStr
    phone: str
    countryCode: str
