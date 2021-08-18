from orm import (
        Model,  DateTime,
        String, Integer
        )
        
from objects.globals import db, metadata
from datetime import datetime as dt

class UserAuth(Model):
    __tablename__ = "user_auth"
    __database__  = db
    __metadata__  = metadata

    id = Integer(primary_key=True)

    login         = String(max_length=255)
    password      = String(max_length=255)
    last_name     = String(max_length=255, default=None)
    first_name    = String(max_length=255, default=None)
    last_password = String(max_length=255)
    last_active   = DateTime(default=dt.now())
    ip_address    = String(max_length=15, default=None)