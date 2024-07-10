from dependency_injector import containers, providers, wiring
from sqlalchemy.orm import Session
from ..database import SessionLocal  # Adjust as per your database setup

class AppContainer(containers.DeclarativeContainer):
    # Define providers for application-level dependencies

    @providers.Singleton
    def session(self) -> Session:
        """Provides a SQLAlchemy session."""
        return SessionLocal()

    # Add more application-level dependencies as needed

    # Wiring configuration to automate dependency injection
    wiring_config = wiring.Wiring()

    def __init__(self):
        super().__init__()
        self.wiring_config = self.wiring_config(self)
