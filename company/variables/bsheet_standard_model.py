from company.variables.variable_model import VariableModel
from company import constants

class BalanceSheetStandardModel(VariableModel):
    def __init__(self,value, fy) -> None:
        super().__init__(constants.ACC_STANDARD, value, fy)
