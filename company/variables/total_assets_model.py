from company.variables.variable_model import VariableModel
from company import constants

class TotalAssetsModel(VariableModel):
    def __init__(self,value, fy) -> None:
        super().__init__(constants.ASSETS, value, fy)

    

