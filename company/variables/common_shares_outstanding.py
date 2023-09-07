from company.variables.variable_model import VariableModel
from company import constants

class CommonSharesOutstandingModel(VariableModel):
    def __init__(self,value, fy) -> None:
        super().__init__(constants.COMMON_SHARES_OUTSTANDING, value, fy)