# Monte Carlo Backtesting for Profitable Trading

A collection of Jupyter notebooks exploring **Monte Carlo simulation** methods applied to forex trading — from basic random number generation through distribution modeling to full backtesting with simulated slippage and spread.

## Project Structure

```
├── 01_random_generators/       # Custom random number generators (e.g. LCG)
├── 02_distributions/           # Explore statistical distributions for price modeling
│   ├── 01_log_normal           #   Log-normal distribution
│   ├── 02_cauchy               #   Cauchy distribution
│   ├── 03_laplace              #   Laplace distribution
│   ├── 04_student_t            #   Student's t-distribution
│   ├── 05_triangular           #   Triangular distribution
│   └── 06_pareto               #   Pareto distribution
├── 03_randomness_trading_data/ # Apply randomness to real trading data
│   ├── 01_slippage_modeling    #   Model slippage with Gaussian & Cauchy noise
│   └── 02_spread_synthetic     #   Model spread & generate synthetic tick data
├── 04_monte_carlo_backtesting/ # Full Monte Carlo backtest pipeline
│   └── backtesting             #   Strategy backtesting with MC slippage
├── utils/                      # Shared Python utilities
│   ├── data.py                 #   OHLCV data loading helpers
│   └── plotting.py             #   Candlestick & distribution plotting
├── requirements.txt
└── README.md
```

## Quick Start

```bash
# 1. Clone the repo
git clone <repo-url>
cd "Monte Carlo Backtesting for Profitable Trading"

# 2. Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter
jupyter notebook
```

## Notebooks Overview

| Section | Topic | Key Concepts |
|---------|-------|-------------|
| **01** | Random Generators | Linear Congruential Generator (LCG) |
| **02** | Distributions | Log-normal, Cauchy, Laplace, Student-t, Triangular, Pareto |
| **03** | Randomness in Trading | Slippage modeling, spread fitting, synthetic tick data |
| **04** | Monte Carlo Backtesting | Strategy development, MC slippage injection, trade sampling, risk assessment |

## Dependencies

- `numpy`, `pandas`, `matplotlib`, `seaborn` — Core data science stack
- `pandas_ta` — Technical analysis indicators
- `yfinance` — Yahoo Finance data downloader
- `plotly`, `mplfinance` — Interactive & financial charting
- `scipy` — Statistical fitting (curve fitting, distributions)
- `tqdm` — Progress bars for MC iterations
- `backtesting` — Backtesting.py framework for strategy evaluation
