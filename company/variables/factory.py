from company import constants
from company.variables.variable_model import VariableModel
from company.variables.total_assets_model import TotalAssetsModel
from company.variables.total_equity_model import TotalEquityModel
from company.variables.bsheet_standard_model import BalanceSheetStandardModel
from company.variables.price_close_model import PriceCloseModel
from company.variables.common_shares_outstanding import CommonSharesOutstandingModel
from company.variables.net_income_before_extraordinary import NetIncomeBeforeExtraordinaryModel
from company.variables.net_cashflow_from_operating_activities import NetCashflowFromOperatingActivitiesModel
from company.variables.common_equity import CommonEquityModel
from company.variables.book_value_per_share import BookValuePerShareModel
from company.variables.total_return import TotalReturnModel

class VariableFactory:

    def __init__(self) -> None:
        pass

    def create_var(self, header, value):
        fy = header.split("FY-")[1]
        if constants.ASSETS in header:
            return TotalAssetsModel(value, fy)
        elif constants.EQUITY in header :
            return TotalEquityModel(value, fy)
        elif constants.ACC_STANDARD in header:
            return BalanceSheetStandardModel(value, fy)
        elif constants.PRICE in header:
            return PriceCloseModel(value, fy)
        elif constants.COMMON_SHARES_OUTSTANDING in header:
            return CommonSharesOutstandingModel(value, fy)
        elif constants.NET_INCOME_BEFORE_EXTRAORDINARY in header:
            return NetIncomeBeforeExtraordinaryModel(value, fy)
        elif constants.NET_CASHFLOW_FROM_OPERATING_ACTIVITIES in header:
            return NetCashflowFromOperatingActivitiesModel(value, fy)
        elif constants.COMMON_EQUITY in header:
            return CommonEquityModel(value, fy)
        elif constants.BOOK_VALUE_PER_SHARE in header:
            return BookValuePerShareModel(value, fy)
        elif constants.TOTAL_RETURN_YTD in header:
            return TotalReturnModel(value, fy)
        else:
            return VariableModel("UNKNOWN_VAR", value, fy)
        