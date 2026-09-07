
# Market Analytics

A quantitative market research dashboard for Indian equities, built with Python and Streamlit.

## What this is

Market Analytics started as a way to bring together the market and stock-level metrics I kept rebuilding in separate notebooks whenever I wanted to investigate a stock or the broader market.

It is now a working dashboard covering two areas:

- Broader market analytics
- Individual stock analytics

I am deliberately keeping the scope tight for this first version rather than trying to fit every technique I know into one application.

A larger system covering the full NSE universe, cross-sectional analytics, and portfolio-level research is planned as the next build.

## Live Dashboard

[Market Analytics](https://market-analytics-dashboard.streamlit.app/)

## Features

### Market Analytics

- Market snapshot
- Market map
- Sector performance
- Sector correlation
- Top performing stocks
- Stock correlation

### Stock Analytics

- Performance across multiple periods
- CAGR and rolling returns
- Win rates
- Volatility, Sharpe, Sortino, and Calmar ratios
- Maximum drawdown and recovery time
- CVaR / Expected Shortfall
- Nifty 50 beta and correlation
- Up/down capture
- Price structure and moving averages
- Autocorrelation
- Liquidity metrics
- Nifty 50 outperformer screen

## Tech Stack

- **Python** — core logic
- **Pandas / NumPy** — data handling and calculations
- **Streamlit** — dashboard interface
- **Plotly** — interactive charts
- **Parquet** — market data storage

The quantitative calculations are kept separate from the dashboard/UI layer on purpose. This makes the analytics engine easier to reuse, test, and extend without having to rebuild the interface.

## Project Structure

```text
Market-Analytics/
├── app.py
├── dashboard/
│   ├── market/
│   └── stocks/
├── src/
│   ├── analytics/
│   │   ├── market.py
│   │   └── stocks/
│   └── data/
├── data/
│   ├── analytics/
│   ├── market/
│   └── raw/
├── scripts/
├── requirements.txt
└── README.md
