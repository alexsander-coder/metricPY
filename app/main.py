from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.upload import router as upload_router

fast = FastAPI()

# config do cors
origins = ["http://localhost:5173"]
fast.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rotas do módulo de upload
fast.include_router(upload_router)
