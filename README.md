Market Analytics

A quantitative market research dashboard for Indian equities, built with Python and Streamlit.


What this is

This started as a way to bring together the market and stock-level metrics I kept rebuilding in separate notebooks every time I wanted to check something. It's now a working dashboard covering two areas — the broader market, and individual stocks.

I'm deliberately keeping the scope tight for this first version rather than trying to fit every technique I know into one app. A larger system covering the full NSE universe with cross-sectional and portfolio-level analytics is next.

Features
Market Analytics
Market snapshot
Market map
Sector performance
Sector correlation
Top performing stocks
Stock correlation
Stock Analytics
Performance across multiple periods
CAGR and rolling returns
Win rates
Volatility, Sharpe, Sortino, Calmar
Maximum drawdown and recovery time
CVaR / Expected Shortfall
Nifty 50 beta and correlation
Up/down capture
Price structure and moving averages
Autocorrelation
Liquidity and trading-volume metrics
Nifty 50 outperformer screen
Stack
Python — core logic
Pandas / NumPy — data handling and calculations
Streamlit — dashboard interface
Plotly — charts
Parquet — market data storage

The quantitative calculations are kept separate from the dashboard/UI layer on purpose, so the analytics engine can be reused or extended without touching the interface code.

Project structure
market-analytics/
├── data/               # Parquet-based market data
├── analytics/          # Calculation logic (returns, risk metrics, correlations, etc.)
├── dashboard/          # Streamlit app and page layouts
├── requirements.txt
└── README.md

(Adjust this to match your actual folder layout before pushing.)

Running it locally
bash
git clone [paste your GitHub repository URL]
cd market-analytics
pip install -r requirements.txt
streamlit run app.py
Roadmap

This is version one. Next up:

Expanding coverage to the full NSE stock universe
Cross-sectional analytics
Portfolio-level tools and optimization
Notes

Built as part of my ongoing move into quantitative research. Feedback from anyone working in markets or building similar tools is welcome — feel free to open an issue or reach out.
