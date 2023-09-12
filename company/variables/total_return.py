from company.variables.variable_model import VariableModel
from company import constants

class TotalReturnModel(VariableModel):
    def __init__(self,value, fy) -> None:
        super().__init__(constants.TOTAL_RETURN_YTD, value, fy)