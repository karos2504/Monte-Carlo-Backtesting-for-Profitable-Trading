"""Shared data-loading utilities for the Monte Carlo Backtesting project."""

import pandas as pd
import yfinance as yf


def load_ohlcv(
    ticker: str,
    period: str = "max",
    interval: str = "1d",
    start: str | None = None,
    end: str | None = None,
    auto_adjust: bool = True,
) -> pd.DataFrame:
    """Download OHLCV data from Yahoo Finance.

    Parameters
    ----------
    ticker : str
        Yahoo Finance ticker symbol (e.g. "EURUSD=X").
    period : str, optional
        Data period to download, by default "max".
    interval : str, optional
        Data interval, by default "1d".
    start / end : str or None, optional
        Start and end dates. When provided, *period* is ignored.
    auto_adjust : bool, optional
        Adjust OHLC automatically, by default True.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns ['Open', 'High', 'Low', 'Close', 'Volume'].
    """
    kwargs: dict = dict(interval=interval, auto_adjust=auto_adjust)
    if start and end:
        kwargs.update(start=start, end=end)
    else:
        kwargs["period"] = period

    df = yf.download(ticker, **kwargs)
    df.columns = ["Open", "High", "Low", "Close", "Volume"]
    return df
