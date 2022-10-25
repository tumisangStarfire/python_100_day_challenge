from fastapi import FastAPI
import uvicorn
import sms_router

app = FastAPI()


def configure():
    app.include_router(sms_router.router, prefix="/api")


if __name__ == "__main__":
    configure()
    uvicorn.run(app, host="127.0.0.1", port=4000)
