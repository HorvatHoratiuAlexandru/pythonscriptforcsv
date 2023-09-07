from company.variables.variable_model import VariableModel
from company import constants

class CommonEquityModel(VariableModel):
    def __init__(self,value, fy) -> None:
        super().__init__(constants.COMMON_EQUITY, value, fy)