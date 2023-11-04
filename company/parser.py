import csv
from company import constants
from company.company_model import Company
from company.variables.factory import VariableFactory

from typing import List

class ComParser:
    

    def __init__(self, file_name):
        self.path = f"data/{file_name}.csv"
        self.headers = None
        self.companies = []
        self.current_company = None
        self.var_factory = VariableFactory()
    
    def get_companies(self):
        self.read_headers()

        with open(self.path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                

                self.current_company = Company()
                for index in range(len(self.headers)):
                    if line[index]:
                        self.cell_dispatcher(self.headers[index], line[index])

                self.current_company.calculate_variables_needed()
                self.current_company.trimm_missing_data_rows()
                if not len(self.current_company.get_variables()) == 0:
                    
                    self.companies.append(self.current_company)
        return self.companies

    def write_to_files(self, matched_companies_list: List[Company]):
        west_filename = "WEST-Final.csv"
        east_filename = "EAST-Final.csv"
        headers = constants.HEADERS

        write_counter = 0

        for c in matched_companies_list:
            c.trimm_self_and_mached_non_common_years()
        for c in matched_companies_list:
            c.match.trimm_self_and_mached_non_common_years()

        for c in matched_companies_list:
            write_counter = write_counter + c.trimm_self_NA()

        print(f"east NAs: {write_counter}")

        write_counter = 0

        for c in matched_companies_list:
            write_counter = write_counter + c.match.trimm_self_NA()
        
        print(f"west NAs: {write_counter}")
        

        with open(east_filename, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, headers)

            writer.writeheader()

            for c in matched_companies_list:
                for row in c.to_rows():
                    writer.writerow(row.to_dict())

        print(f"east file created")

        with open(west_filename, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, headers)

            writer.writeheader()

            for c in matched_companies_list:
                for row in c.match.to_rows():
                    writer.writerow(row.to_dict())

        print("west file created")




    def read_headers(self):
        with open(self.path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.headers = next(csv_reader)

    def cell_dispatcher(self, header_value, cell_value):
        if self.identifier_observer(header_value, cell_value):
            pass
        elif self.name_observer(header_value, cell_value):
            pass
        elif self.country_observer(header_value, cell_value):
            pass
        elif self.ipo_observer(header_value, cell_value):
            pass
        elif self.balance_sheet_period_observer(header_value, cell_value):
            pass
        elif self.industry_observer(header_value, cell_value):
            pass
        else:
            self.variable_observer(header_value, cell_value)
    
    def identifier_observer(self, header, value):
        if constants.ID in header:
            self.current_company.set_id(value)
            return True
        return False

    def name_observer(self, header, value):
        if constants.NAME in header:
            self.current_company.set_name(value)
            return True
        return False
    
    def country_observer(self, header, value):
        if constants.COUNTRY in header:
            self.current_company.set_country(value)
            return True
        return False
    
    def ipo_observer(self, header, value):
        if constants.IPO in header:
            self.current_company.set_ipo(value)
            return True
        return False
    
    def industry_observer(self, header, value):
        if constants.INDUSTRY in header:
            self.current_company.set_industry(value)
            return True
        return False
    
    def balance_sheet_period_observer(self, header, value):
        if constants.BALANCE_SHEET_DATE in header:
            self.current_company.add_fy(header.split("FY-")[1], value)
            return True
        return False
    
    def variable_observer(self, header, value):
        self.current_company.add_variable(self.var_factory.create_var(header, value))

        return True
