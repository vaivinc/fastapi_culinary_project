import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes import user_route, auth_route, receipe_route
app = FastAPI(docs_url="/docs")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


app.include_router(user_route, prefix="/account", tags=["users"])
app.include_router(auth_route, prefix="/auth", tags=["auth"])
app.include_router(receipe_route, prefix="/receipe", tags=["receipe"])

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
