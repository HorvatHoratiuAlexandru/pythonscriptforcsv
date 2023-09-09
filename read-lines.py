from company.parser import ComParser
from company.match_model import CompanyMatcher

west_p = ComParser("WEST-2023")
east_p = ComParser("EAST-2023")

west_comps = west_p.get_companies()
east_comps = east_p.get_companies()

print(f"west no. : {len(west_comps)}")

print(f"east no. : {len(east_comps)}")

comp_matcher = CompanyMatcher(east_comps, west_comps)

east_matched = comp_matcher.exec()

east_p.write_to_files(east_matched)