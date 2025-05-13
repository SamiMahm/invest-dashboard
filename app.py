import streamlit as st
from main import get_fmp_data

st.title("📊 FMP Investment Dashboard")

ticker = st.text_input("Enter a stock ticker (e.g. META, AAPL, MSFT):", value="META").upper()

def display_data(name, sector, currency, eps, gpm, 
                 rev_y1, rev_y2, yoy_rev, net_income,
                 total_assets, total_liab, total_equity,
                 debt_ratio, op_cash, capex, fcf):
    
    st.subheader(f"{name} ({sector})")
    st.write(f"**Currency:** {currency}")

    st.subheader("📈 Financial Overview")
    st.write(f"**Total Assets:** {currency} {total_assets}")
    st.write(f"**Total Liabilities:** {currency} {total_liab}")
    st.write(f"**Total Equity:** {currency} {total_equity}")
    st.write(f"**Debt Ratio:** {debt_ratio:.2f}%" if debt_ratio else "N/A")

    st.subheader("📊 Profitability")
    st.write(f"**Revenue Year 1:** {currency} {rev_y1}")
    st.write(f"**Revenue Year 2:** {currency} {rev_y2}")
    st.write(f"**YOY Revenue Change:** {yoy_rev:.2%}" if yoy_rev else "N/A")
    st.write(f"**Net Income:** {currency} {net_income}")
    st.write(f"**EPS:** {eps}")
    st.write(f"**Gross Profit TTM:** {currency} {gpm}")
    st.write(f"**Free Cash Flow:** {currency} {fcf}")

# Run the app
if __name__ == "__main__":
    result = get_fmp_data(ticker)
    if result:
        display_data(*result)
    else:
        st.error("❌ Failed to fetch data. Check the ticker or your API usage.")
