from company.parser import ComParser
from company import constants

west_p = ComParser("EAST-2023")
east_p = ComParser("WEST-2023")

west_comps = west_p.get_companies()
east_comps = east_p.get_companies()

ifrs_count = 0
for comp in east_comps:
    ifrs_adoption_year = comp.get_ifrs_adoption_year()
    if ifrs_adoption_year and ifrs_adoption_year < 2007 and ifrs_adoption_year > 2003:
        ifrs_count += 1
    
print(ifrs_count)