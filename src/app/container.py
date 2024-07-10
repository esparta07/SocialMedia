from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL  = "sqlite:///./src/db.sql"

class ApplicationContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.app.post.adapter.input.api.v1.post"])

    db_engine = providers.Singleton(create_engine, DATABASE_URL)
    db_session = providers.Singleton(sessionmaker, bind=db_engine)

    # Provide a session
    db = providers.Resource(
        lambda db_session: db_session(),
        db_session=db_session
    )
