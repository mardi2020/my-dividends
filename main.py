from fastapi import FastAPI
from routers.ticker import router as ticker_router

app = FastAPI()

# 라우터 등록
app.include_router(ticker_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
