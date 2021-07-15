import asyncio
import socket
from flask import Flask

from databases import Database
from sqlalchemy import MetaData, create_engine

from objects import globals

async def main():

    globals.ip_adress = socket.gethostbyname(socket.gethostname())
    globals.app = Flask(__name__)
    globals.app.config['SECRET_KEY'] = "da7780e7736accb03d3742897e846e0e"

    #Database
    globals.db = Database("sqlite:///../db/UBI.sqlite")
    globals.metadata = MetaData()

    globals.db_engine = create_engine(str(globals.db.url))
    globals.metadata.create_all(globals.db_engine)

    from db_models.AdminAuth import AdminAuth

    #Set admin password
    admin_data = await AdminAuth.objects.all()
    globals.admin_password = admin_data[0].password

    import commands

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    globals.app.run(host="0.0.0.0", port="5002", debug=True)