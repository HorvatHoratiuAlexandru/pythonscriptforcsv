from company.variables.variable_model import VariableModel
from company import constants

class BookValuePerShareModel(VariableModel):
    def __init__(self,value, fy) -> None:
        super().__init__(constants.BOOK_VALUE_PER_SHARE, value, fy)