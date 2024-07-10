from dependency_injector import containers, providers

from src.app.container import ApplicationContainer
from src.app.post.adapter.output.persistence.post_repository_adapter import PostRepositoryAdapter
from src.app.post.application.services.post import PostService

class PostContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.app.post.adapter.input.api.v1.post"])

    application_container = providers.Container(ApplicationContainer)

    post_repository = providers.Factory(
        PostRepositoryAdapter,
        db=application_container.db
    )

    post_service = providers.Factory(
        PostService,
        repository=post_repository
    )
