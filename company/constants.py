ID='Identifier'
NAME='Company Name'
COUNTRY='Country of Headquarters'
IPO='IPO Date'
INDUSTRY='TRBC Economic Sector Name'
BALANCE_SHEET_DATE='Balance Sheet Period End Date'
ASSETS='Total Assets'
EQUITY="Total Equity"
ACC_STANDARD='Balance Sheet Accounting Standard'
PRICE='Price Close'
COMMON_SHARES_OUTSTANDING="Common Shares - Outstanding"
NET_INCOME_BEFORE_EXTRAORDINARY="Net Income Before Extraordinary Items"
NET_CASHFLOW_FROM_OPERATING_ACTIVITIES="Net Cash Flow from Operating Activities"
COMMON_EQUITY="Common Equity"
BOOK_VALUE_PER_SHARE="Book Value Per Share"
TOTAL_RETURN_YTD="YTD Total Return"
MATCH = "MATCH"
YEAR = "Year"

VARIABLES = [
    ASSETS,
    EQUITY,
    ACC_STANDARD,
    PRICE,
    COMMON_SHARES_OUTSTANDING,
    NET_INCOME_BEFORE_EXTRAORDINARY,
    NET_CASHFLOW_FROM_OPERATING_ACTIVITIES,
    BOOK_VALUE_PER_SHARE,
    TOTAL_RETURN_YTD,
]



# Calculated Variables

# PURE
NET_INCOME_PER_SHARE = "NI"

# IMPURE
DELTA_NI = "NI CHANGE" # abs(NI t - NI t - 1)
NI_PER_LAGED_TA = "NI PER LAGED TA" # NI/TA t-1
LOSS = "LOSS"
DELTA_NI_PER_LAGED_PRICE = "NI CHANGE PER LAGGED PRICE"
NI_PER_LAGED_PRICE = "NI PER LAGGED PRICE"
CF = "CASH FLOW PER LAGGED TOTAL ASSETS"
CF_T_PLUS_ONE = "CASHFLOW T P ONE"


# HEADERS TO WRITE

HEADERS = [
    ID,
    YEAR,
    NAME,
    MATCH,
    COUNTRY,
    IPO,
    INDUSTRY,
    BALANCE_SHEET_DATE,
    ACC_STANDARD,
    ASSETS,
    EQUITY,
    PRICE,
    COMMON_SHARES_OUTSTANDING,
    NET_INCOME_BEFORE_EXTRAORDINARY,
    NET_CASHFLOW_FROM_OPERATING_ACTIVITIES,
    COMMON_EQUITY,
    BOOK_VALUE_PER_SHARE,
    TOTAL_RETURN_YTD,
    NET_INCOME_PER_SHARE,
    DELTA_NI,
    LOSS,
    NI_PER_LAGED_PRICE,
    DELTA_NI_PER_LAGED_PRICE
    ]