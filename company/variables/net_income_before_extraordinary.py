from company.variables.variable_model import VariableModel
from company import constants

class NetIncomeBeforeExtraordinaryModel(VariableModel):
    def __init__(self,value, fy) -> None:
        super().__init__(constants.NET_INCOME_BEFORE_EXTRAORDINARY, value, fy)