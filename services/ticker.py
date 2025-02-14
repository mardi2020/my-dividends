import yfinance as yf
from fastapi import HTTPException


def fetch_ticker_info(symbol: str):
    try:
        stock = yf.Ticker(symbol)
        stock_info, dividends = dict(stock.info), stock.history(period='max')['Dividends']

        if not stock_info:
            raise HTTPException(status_code=404, detail="티커 정보를 찾을 수 없습니다.")

        return {
            "symbol": symbol,
            "name": stock_info["longName"],
            "current_price": calculate_curr_price(stock_info),
            "52_week_high": stock_info["fiftyTwoWeekHigh"],
            "52_week_low": stock_info["fiftyTwoWeekLow"],
            "dividends": pick_dividends(dividends.to_dict()) if not dividends.empty else 'N/A',
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


def calculate_curr_price(stock_info: dict) -> str:
    bid, ask = stock_info['bid'], stock_info['ask']
    previous_close, open_price = stock_info['previousClose'], stock_info['open']
    return (bid + ask) / 2 if bid and ask else previous_close or open_price or 'N/A'


def pick_dividends(dividends: dict) -> dict:
    return {str(k.date()): v for k, v in dividends.items() if v > 0}
