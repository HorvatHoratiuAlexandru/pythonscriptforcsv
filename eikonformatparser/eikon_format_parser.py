import csv
import eikonformatparser.constantq as constantq

from typing import List

class EikonParser:

    def __init__(self) -> None:
        self.headers = None
        self.comps: List[EikonComp] = []

    def exec(self, file_name):
        path = f"data/{file_name}.csv"
        panel_filename = "PANEL_RESULT.csv"
        self.read_headers(path)

        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for line in csv_reader:
                for fy in range(27):
                    comp = EikonComp()
                    for index in range(len(self.headers)):
                        comp.addDataCell(self.headers[index], line[index], fy)

                    self.comps.append(comp)

            print(f"no. of rows: {len(self.comps)}")
        
        # write all comps to panel csv
        with open(panel_filename, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, constantq.HEADERS)

            writer.writeheader()

            for c in self.comps:
                writer.writerow(c.observations)

        print(f"file created")

    def read_headers(self, path):
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.headers = next(csv_reader)


class EikonComp:

    def __init__(self) -> None:
        self.headers = constantq.HEADERS
        self.observations = dict()

    def addDataCell(self, header_name, value, financial_year):
        if not value:
            value = "NA"

        #check if data is from the financial year

        if "FY" in header_name:
            fy = int(header_name.split("FY-")[1])
            if not fy == financial_year:
                return
        
        for header in self.headers:
            if header in header_name:
                self.observations[header] = value
                break
        
        if constantq.BALANCE_SHEET_DATE in header_name:
            if value == "NA":
                self.observations[constantq.YEAR] = "NA"
            else:
                self.observations[constantq.YEAR] = value.split("/")[2]

    