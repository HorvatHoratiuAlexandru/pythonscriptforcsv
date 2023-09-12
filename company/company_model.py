from company.company_row import CompanyRow
from company import constants
from company import utils

class Company:
    def __init__(self) -> None:
        self.id = ""
        self.name = ""
        self.country = ""
        self.ipo = ""
        self.industry = ""
        self.match: Company = None
        self.financial_years = dict()
        self.variables = dict()
        

    def __str__(self) -> str:
        return f"Name: {self.name}, Country: {self.country}, IPO: {self.ipo}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def to_rows(self):
        rows = []
        variables = self.get_variables()

        for key in variables:
            row = CompanyRow()
            row.id = self.id
            row.match = self.match.id
            row.name = self.name
            row.country = self.country
            row.industry = self.industry
            row.ipo = self.ipo
            row.year = key
            row.balance_sheet_date = key
            row.assets = variables.get(key).get(constants.ASSETS)
            row.equity = variables.get(key).get(constants.EQUITY)
            row.acc_standard = variables.get(key).get(constants.ACC_STANDARD)
            row.price = variables.get(key).get(constants.PRICE)
            row.common_shares_outstanding = variables.get(key).get(constants.COMMON_SHARES_OUTSTANDING)
            row.net_income_before_extraordinary = variables.get(key).get(constants.NET_INCOME_BEFORE_EXTRAORDINARY)
            row.net_cashflow_from_operating_activities = variables.get(key).get(constants.NET_CASHFLOW_FROM_OPERATING_ACTIVITIES)
            row.common_equity = variables.get(key).get(constants.EQUITY)
            row.book_value_per_share = variables.get(key).get(constants.BOOK_VALUE_PER_SHARE)
            row.total_return_ytd = variables.get(key).get(constants.TOTAL_RETURN_YTD)

            rows.append(row)
        
        return rows

            

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
        if not variable_model:
            return
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


    def trimm_self_and_mached_non_common_years(self):
        self_years = list(self.get_variables().keys())
        match_years = list(self.match.get_variables().keys())
        matched_years = utils.longest_common_array(self_years, match_years)
        

        to_delete = []

        for key in self.get_variables():
            if key not in matched_years:
                to_delete.append(key)

        for key in to_delete:
            self.variables.pop(key)


    def non_continuos_ifrs(self):
        first_ifrs_occurence = self.get_ifrs_adoption_year()
        if not first_ifrs_occurence:
            return True
        acc_standards = self.get_accounting_standards()
        years = []

        for key in acc_standards:
            years.append(int(key))
        
        years.sort()

        non_ifrs_years = []

        for year in years:
            if year >= first_ifrs_occurence:
                if not acc_standards.get(str(year)) == "IFRS":
                    return True
            if year < first_ifrs_occurence:
                non_ifrs_years.append(year)

        if len(non_ifrs_years) < 1:
            return True
        
        return False


    def get_ifrs_adoption_year_mve(self):
        year = self.get_ifrs_adoption_year()
        c_variables = self.get_variables()

        shares_outstanding = utils.from_delimited_str_to_float(c_variables.get(str(year)).get(constants.COMMON_SHARES_OUTSTANDING))
        price = utils.from_delimited_str_to_float(c_variables.get(str(year)).get(constants.PRICE))

        return price * shares_outstanding

    def get_ifrs_adoption_year(self):
        acc_standards = self.get_accounting_standards()
        years = []

        for key in acc_standards:
            years.append(int(key))
        
        years.sort()

        for year in years:
            if acc_standards.get(str(year)) == "IFRS":
                return year
        
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

    
