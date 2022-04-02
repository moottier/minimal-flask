# from app.models.db import db, migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from app.models.fact import Fact
from app.models.user import User