from fastapi import APIRouter, Query
from services.ticker_service import fetch_ticker_info

router = APIRouter()


@router.get("/stock")
def get_ticker_info(ticker: str = Query(..., description="주식 티커 심볼")):
    return fetch_ticker_info(ticker)
