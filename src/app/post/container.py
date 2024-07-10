from dependency_injector import containers, providers, wiring
from src.app.container import AppContainer  # Import the main AppContainer
from domain.repository.post import PostRepository
from domain.services.post import AbstractPostService
from adapter.output.persistence.post_repository_adapter import PostRepositoryAdapter
from sqlalchemy.orm import Session

class PostContainer(containers.DeclarativeContainer):
    # Extend the main application container
    app_container = providers.Container(AppContainer)

    @providers.Singleton
    @app_container.inject
    def session(self, session: Session = providers.Provider[AppContainer.session]):
        return session

    @providers.Singleton
    def post_repository(self, session: Session) -> PostRepository:
        """Provides an instance of PostRepository."""
        return PostRepositoryAdapter(session)

    @providers.Singleton
    def post_service(self, repository: PostRepository) -> AbstractPostService:
        """Provides an instance of AbstractPostService."""
        return AbstractPostService(repository)

    # Add more providers specific to the post module

    # Wiring configuration to automate dependency injection
    wiring_config = wiring.Wiring()

    def __init__(self):
        super().__init__()
        self.wiring_config = self.wiring_config(self)
