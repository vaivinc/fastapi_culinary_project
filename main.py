import uvicorn
from fastapi import FastAPI

app = FastAPI(docs_url="/docs")


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)