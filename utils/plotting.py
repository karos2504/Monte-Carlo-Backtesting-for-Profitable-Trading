"""Shared plotting helpers for the Monte Carlo Backtesting project."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_candlestick(
    df: pd.DataFrame,
    start_index: int = 0,
    num_rows: int = 100,
    title: str = "Candlestick Chart",
) -> None:
    """Plot an interactive Plotly candlestick chart.

    Parameters
    ----------
    df : pd.DataFrame
        OHLCV DataFrame with a DatetimeIndex.
    start_index : int
        First row to include in the chart.
    num_rows : int
        Number of rows to display.
    title : str
        Chart title.
    """
    subset = df.iloc[start_index : start_index + num_rows].copy()
    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(
        go.Candlestick(
            x=subset.index,
            open=subset["Open"],
            high=subset["High"],
            low=subset["Low"],
            close=subset["Close"],
            name="Price",
        )
    )
    fig.update_layout(title=title, xaxis_rangeslider_visible=False)
    fig.show()


def plot_distribution(
    data: np.ndarray | pd.Series,
    bins: int = 50,
    log_scale: bool = True,
    title: str = "Distribution",
    xlabel: str = "Value",
    ylabel: str = "Frequency",
    figsize: tuple[int, int] = (12, 6),
) -> None:
    """Plot a histogram of a distribution using matplotlib/seaborn.

    Parameters
    ----------
    data : array-like
        Data to plot.
    bins : int
        Number of histogram bins.
    log_scale : bool
        Whether to use log scale on the y-axis.
    title, xlabel, ylabel : str
        Axis labels and title.
    figsize : tuple
        Figure size.
    """
    import seaborn as sns

    plt.figure(figsize=figsize)
    sns.histplot(data, bins=bins)
    if log_scale:
        plt.yscale("log")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
