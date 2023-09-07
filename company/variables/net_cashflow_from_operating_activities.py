from company.variables.variable_model import VariableModel
from company import constants

class NetCashflowFromOperatingActivitiesModel(VariableModel):
    def __init__(self,value, fy) -> None:
        super().__init__(constants.NET_CASHFLOW_FROM_OPERATING_ACTIVITIES, value, fy)