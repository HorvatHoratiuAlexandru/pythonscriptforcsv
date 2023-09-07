from company import constants

class Company:
    def __init__(self) -> None:
        self.id = ""
        self.name = ""
        self.country = ""
        self.ipo = ""
        self.industry = ""
        self.financial_years = dict()
        self.variables = dict()
        

    def __str__(self) -> str:
        return f"Name: {self.name}, Country: {self.country}, IPO: {self.ipo}"
    
    def __repr__(self) -> str:
        return self.__str__()

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name
    
    def set_country(self, country):
        self.country = country
    
    def set_ipo(self, ipo):
        self.ipo = ipo

    def set_industry(self, industry):
        self.industry = industry

    def add_fy(self, fy, date):
        self.financial_years[fy] = date.split("/")[2]
    
    def add_variable(self, variable_model):
        if not self.financial_years.get(variable_model.fy):
            return
        if not self.variables.get(self.financial_years[variable_model.fy]):
            self.variables[self.financial_years[variable_model.fy]] = dict()

        self.variables[self.financial_years[variable_model.fy]][variable_model.type]=variable_model.value

    def trimm_missing_data_rows(self):
        keys_to_remove = []
        fy_keys_to_remove = []
        for key in self.variables:
            for coll in constants.VARIABLES:
                if coll not in self.variables[key]:
                    keys_to_remove.append(key)
                    break
        
        for key in keys_to_remove:
            self.variables.pop(key)
        
        for key in self.financial_years:
            if self.financial_years[key] in keys_to_remove:
                fy_keys_to_remove.append(key)

        for key in fy_keys_to_remove:
            self.financial_years.pop(key)

    def get_first_year(self):
        first_year = 2024

        for key in self.variables:
            if int(key) < first_year:
                first_year = int(key)

        return first_year     

        



   

    
    
    
    

    
# LEFT HERE
    def get_ifrs_adoption_year(self):
        acc_standards = self.get_accounting_standards()
        is_ifrs = False
        year = self.get_first_year()
        print(year)
        while(year < 2024):
            STANDARD = self.variables.get(str(year)).get(constants.ACC_STANDARD) if self.variables.get(str(year)) else None
            if STANDARD and STANDARD == "IFRS":
                is_ifrs = True
                return year
            year += 1
        return None
        



    def get_accounting_standards(self):
        acc_standards = dict()
        for key in self.financial_years:
            value = self.variables[self.financial_years[key]].get(constants.ACC_STANDARD)
            if value:
                acc_standards[self.financial_years[key]] = value
        
        return acc_standards

    def list_variables(self):
        for k, v in self.variables.items():
            print(f"{k}: {v}")

    def get_variables(self):
        return self.variables
    
    def list_fy(self):
        for k, v in self.financial_years.items():
            print(f"{k}: {v}")

    
