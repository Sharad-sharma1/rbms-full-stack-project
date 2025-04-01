from .helpers import logger

logger.setup_logging()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import app_routers
from .helpers import constant as sc
from .controller.app_config import app_config

# Initialize FastAPI application
app = FastAPI(
    title=sc.APPLICATION_NAME,
    swagger_ui_parameters={
        "defaultModelsExpandDepth": 0,  # Collapse `Schemas` section in Swagger
    },
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=app_config.ALLOW_ORIGIN if isinstance(app_config.ALLOW_ORIGIN, list) else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_routers.router)