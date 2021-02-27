from fastapi import FastAPI

from routes.trucks import truck_routers
from routes.vowels import vowels_routers
from routes.worker import workers_routers


app = FastAPI(
    title="EnvioClickTests",
    description="Endpoints for backend vacancie",
    version="0.0.1",
)

app.include_router(vowels_routers)
app.include_router(truck_routers)
app.include_router(workers_routers)
