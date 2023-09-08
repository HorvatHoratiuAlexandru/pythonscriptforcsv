from company.company_model import Company
from typing import List

class CompanyMatcher:

    def __init__(self, list_one, list_two) -> None:
        self.list_one:List[Company] = list_one
        self.list_two:List[Company] = list_two
        self.matched_l1:List[Company] = []
        self.matched_l2:List[Company] = []


    def exec(self):
        matches_list:List[Company] = []
        for comp in self.list_one:
            print(f"Working on company:")
            print(comp)
            matches_list = self.get_matched_industry_comps(comp, self.list_two)
            matches_list = self.get_matched_mve_comps(comp, matches_list)
            matched_list = self.get_matched_longest_common_timeframe(comp, matches_list)


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

            diff: float = abs(comp_mve - c_mve)

            if 0.5 * comp_mve > diff:
                matched.append(c)
        
        print(f"matched {len(matched)} companies by mve in ifrs adoption year")

        return matched
    
    def get_matched_longest_common_timeframe(self, comp: Company, c_list: List[Company]):
        m = len(str1)
        n = len(str2)
    
        # Create a table to store the lengths of common substrings
        # dp[i][j] will store the length of the common substring ending at str1[i-1] and str2[j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
    
        # Variables to store the length of the longest common substring
        max_length = 0
        end_index = 0
    
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        end_index = i
    
        # Extract the longest common substring
        longest_substring = str1[end_index - max_length:end_index]
    
        return longest_substring
