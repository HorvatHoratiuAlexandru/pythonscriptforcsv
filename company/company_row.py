from company import constants

class CompanyRow:

    def __init__(self) -> None:
        self.id = ""
        self.year = ""
        self.name = ""
        self.match = ""
        self.country = ""
        self.ipo = ""
        self.industry = ""
        self.balance_sheet_date= ""
        self.acc_standard= ""
        self.assets= ""
        self.equity= ""
        self.price= ""
        self.common_shares_outstanding = ""
        self.net_income_before_extraordinary = ""
        self.net_cashflow_from_operating_activities = ""
        self.common_equity = ""
        self.book_value_per_share = ""
        self.total_return_ytd = ""
        self.net_income_per_share = ""
        self.delta_ni = ""
        self.loss = ""
        self.ni_per_price_laged = ""
        self.delta_ni_per_price_laged = ""

    def to_dict(self):
        return {
            constants.ID: self.id,
            constants.YEAR: self.year,
            constants.NAME: self.name,
            constants.MATCH: self.match,
            constants.COUNTRY: self.country,
            constants.IPO: self.ipo,
            constants.INDUSTRY: self.industry,
            constants.BALANCE_SHEET_DATE: self.balance_sheet_date,
            constants.ACC_STANDARD: self.acc_standard,
            constants.ASSETS: self.assets,
            constants.EQUITY: self.equity,
            constants.PRICE: self.price,
            constants.COMMON_SHARES_OUTSTANDING: self.common_shares_outstanding,
            constants.NET_INCOME_BEFORE_EXTRAORDINARY: self.net_income_before_extraordinary,
            constants.NET_CASHFLOW_FROM_OPERATING_ACTIVITIES: self.net_cashflow_from_operating_activities,
            constants.COMMON_EQUITY: self.common_equity,
            constants.BOOK_VALUE_PER_SHARE: self.book_value_per_share,
            constants.TOTAL_RETURN_YTD: self.total_return_ytd,
            constants.NET_INCOME_PER_SHARE: self.net_income_per_share,
            constants.DELTA_NI: self.delta_ni,
            constants.LOSS: self.loss,
            constants.NI_PER_LAGED_PRICE: self.ni_per_price_laged,
            constants.DELTA_NI_PER_LAGED_PRICE: self.delta_ni_per_price_laged,
        }