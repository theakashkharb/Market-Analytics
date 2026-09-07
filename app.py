from __future__ import annotations

import streamlit as st

from dashboard.market.market_ui import render_market_page
from dashboard.stocks.stocks_ui import render_stocks_page


st.set_page_config(
    page_title="Market Analytics",
    layout="wide",
)

st.title("Market Analytics")

st.markdown(
    """
    <style>
    div[role="radiogroup"] label {
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        padding: 0.35rem 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

page = st.radio(
    "Navigate",
    [
        "Market",
        "Stocks",
    ],
    horizontal=True,
)

if page == "Market":
    render_market_page()

elif page == "Stocks":
    render_stocks_page()