from company.company_model import Company
from company import utils

import math
import time

from typing import List


class CompanyMatcher:

    def __init__(self, list_one, list_two) -> None:
        self.list_one:List[Company] = list_one
        self.list_two:List[Company] = list_two
        self.matched_l1:List[Company] = []
        self.matched_l2:List[Company] = []


    def exec(self):
        matches_list:List[Company] = []
        matched_list:List[Company] = []
        matches_no = 0
        for comp in self.list_one:
            print(f"Working on company:")
            print(comp)
            matches_list = self.get_matched_industry_comps(comp, self.list_two)
            # matches_list = self.get_matched_mve_comps(comp, matches_list)
            matched_c = self.get_matched_longest_common_timeframe_and_mve(comp, matches_list)
            if matched_c:
                print(f"Company: {comp}")
                print(f"Matched: {matched_c}")
                matched_c.match = comp
                comp.match = matched_c
                self.list_two = [c for c in self.list_two if c.id != matched_c.id]
                matched_list.append(comp)
            print("----")
        
        for c in matched_list:
            print(f"Match: {c.name} with {c.match}")
            matches_no += 1

        print(f"Matched: {matches_no} companies!")

        return matched_list


    def get_matched_industry_comps(self, comp: Company, c_list: List[Company]):
        matched = []

        for c in c_list:
            if c.industry == comp.industry:
                matched.append(c)

        print(f"matched {len(matched)} companies by industry")
        
        return matched


    def get_matched_mve_comps(self, comp: Company, c_list: List[Company]):
        matched = []
        comp_mve: float = comp.get_ifrs_adoption_year_mve()
        
        for c in c_list:
            c_mve:float = c.get_ifrs_adoption_year_mve()

            diff: float = abs(c_mve - comp_mve)

            if 0.5 * comp_mve <= diff:
                matched.append(c)
        
        print(f"matched {len(matched)} companies by mve in ifrs adoption year")

        return matched
    
    def if_mve_match(self, to_match_mve, matching_mve):
        pass
    
    def get_matched_longest_common_timeframe(self, comp: Company, c_list: List[Company]):
        comp_years = list(comp.get_variables().keys())
        comp_mve = 0
        matched_id = ""
        max_length = 1
        max_mve = 0

        for c in c_list:
            c_years = list(c.get_variables().keys())
            longest_sub_array = utils.longest_common_array(comp_years, c_years)

            if longest_sub_array:
                longest_sub_array.sort()
                first_common_year = longest_sub_array[0]
                comp_mve = comp.get_year_mve(first_common_year)

            if len(longest_sub_array) == max_length:
                if not max_mve == utils.best_of_two_mves(comp_mve, max_mve, c.get_year_mve(first_common_year)):
                    matched_id = c.id
                    max_mve = c.get_year_mve(first_common_year)

            if len(longest_sub_array) > max_length:
                max_length = len(longest_sub_array)
                matched_id = c.id
                max_mve = c.get_year_mve(first_common_year)
        
        for c in c_list:
            if matched_id == c.id:
                return c
            
        return None
    
    def get_matched_longest_common_timeframe_and_mve(self, comp: Company, c_list: List[Company]):
        comp_years = list(comp.get_variables().keys())
        vec2_matches: List[List[float, Company]] = []

        for c in c_list:
            c_years = list(c.get_variables().keys())
            longest_sub_array = utils.longest_common_array(comp_years, c_years)
            if longest_sub_array:
                
                longest_sub_array.sort()
                c_mve = c.get_year_mve(longest_sub_array[0])
                comp_mve = comp.get_year_mve(longest_sub_array[0])                

                if 0.6*comp_mve >= abs(comp_mve-c_mve):
                    vec2_matches.append([self.vec_magnitude([1 - abs(comp_mve-c_mve)/(comp_mve+c_mve)/2, len(longest_sub_array)]), c])
                
                    
            
        if vec2_matches:
            matched_comp = max(vec2_matches, key=lambda x: x[0])
            print(f'matched {comp.name} with {matched_comp[1].name} with magnitude: {matched_comp[0]}')
            return(matched_comp[1])
        
        return None
        
        

    def vec_dot_product(self, vec1, vec2):
        assert len(vec1) == len(vec2)

        return sum(vec1_i * vec2_i for vec1_i, vec2_i in zip(vec1,vec2))

    def vec_sum_of_squares(self, vec1):
        return self.vec_dot_product(vec1,vec1)
    
    def vec_magnitude(self, vec1):
        return math.sqrt(self.vec_sum_of_squares(vec1))