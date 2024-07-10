from fastapi import FastAPI
from src.app.post.adapter.input.api.v1.post import router as post_router
from src.app.container import ApplicationContainer

app = FastAPI()

# Initialize and wire the container
container = ApplicationContainer()
container.init_resources()
container.wire(modules=["src.app.post.adapter.input.api.v1.post"])

app.container = container

app.include_router(post_router, prefix="/api/v1", tags=["posts"])

@app.on_event("startup")
async def on_startup():
    from src.database import Base  # Import your Base from your database module
    engine = container.db_engine()
    Base.metadata.create_all(bind=engine)
