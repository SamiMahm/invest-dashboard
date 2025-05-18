# for requests and getting metrics
import requests

API_KEY = "kSxzOpCTmUAZvSKH9zjXmechwOMM1trL"

def fetch_fmp_data(ticker):
    base_url = "https://financialmodelingprep.com/api/v3"

    def get_json(endpoint, extra_params=""):
        if extra_params:
            url = f"{base_url}/{endpoint}{extra_params}&apikey={API_KEY}"
        else:
            url = f"{base_url}/{endpoint}?apikey={API_KEY}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    profile = get_json(f"profile/{ticker}")
    income = get_json(f"income-statement/{ticker}", "?limit=2")
    balance = get_json(f"balance-sheet-statement/{ticker}", "?limit=1")
    cashflow = get_json(f"cash-flow-statement/{ticker}", "?limit=1")

    return profile, income, balance, cashflow

def get_fmp_data(ticker):
    profile, income, balance, cashflow = fetch_fmp_data(ticker)

    if not profile or not income or not balance or not cashflow:
        return None

    name = profile[0].get('companyName', 'N/A')
    sector = profile[0].get('sector', 'N/A')
    currency = profile[0].get('currency', 'USD')
    eps = profile[0].get('eps', 'N/A')
    gpm = profile[0].get('grossProfitTTM', 'N/A')
    market_cap = profile[0].get('marketCap')
    shares_outstanding = profile[0].get('sharesOutstanding')

    rev_y1 = income[1].get('revenue')
    rev_y2 = income[0].get('revenue')
    yoy_rev = ((rev_y2 - rev_y1) / rev_y1) if rev_y1 else None
    net_income = income[0].get('netIncome')

    total_assets = balance[0].get('totalAssets')
    total_liab = balance[0].get('totalLiabilities')
    total_equity = balance[0].get('totalStockholdersEquity')
    debt_ratio = (total_liab / total_assets * 100) if total_assets else None
    short_term_debt = balance[0].get('shortTermDebt')
    long_term_debt = balance[0].get('longTermDebt')
    current_debt = balance[0].get('currentDebt')
    avgPrice36m = sum(last_756_days_of_close_prices) / 756
    avgMarketCap36m = avgPrice36m * shares_outstanding



    op_cash = cashflow[0].get('operatingCashFlow')
    capex = cashflow[0].get('capitalExpenditure')
    fcf = (op_cash - capex) if op_cash and capex else None

    return (
        name, sector, currency, eps, gpm,
        rev_y1, rev_y2, yoy_rev, net_income,
        total_assets, total_liab, total_equity,
        debt_ratio, op_cash, capex, fcf
    )

haram_sectors = [
    "Beverages—Wineries & Distilleries", 
    "Beverages—Alcoholic",
    "Package Foods",
    "Banks",
    "Capital Markets",
    "Insurance",
    "Credit Services",
    "Gambling",
    "Resorts & Casinos",
    "Entertainment",
    "Publishing",
    "Tobacco",
    "Aerospace & Defense",
    "Media",
    "Mortgage Finance",
    "Insurance-Diversified",
    "Insurance—Property & Casualty"
]


def is_halal_sector(area):
    if area in haram_sectors:
        return 'Haram'
    else:
        return 'Halal'

#lets determine if the stock is halal
# make a function that calculates everything and then makes a decison 
# then output if it halal or not

#CHAT GPT PROMPT  leverage ratio, what is the formula, and what 
#specifically in FMP what are the terms used 
# Leverage Ratio

# Receivables Ratio

# Cash and Interest-Bearing Securities Ratio

# Dividend Purification Ratio (DP Ratio)

# Average Market Capitalization (36-Month)

# Non-Permissible Revenue Percentage

# Sector Compliance Check