def from_delimited_str_to_float(str_number: str):
    return float(str_number.replace(",", ""))

def longest_common_array(arr_one, arr_two):
    m = len(arr_one)
    n = len(arr_two)

    # Create a table to store the lengths of common substrings
    # dp[i][j] will store the length of the common substring ending at str1[i-1] and str2[j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to store the length of the longest common substring
    max_length = 0
    end_index = 0

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if arr_one[i - 1] == arr_two[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    # Extract the longest common substring
    longest_substring = arr_one[end_index - max_length:end_index]

    return longest_substring


def best_of_two_mves(comp_mve, mve1, mve2):
    diff_one: float = abs(comp_mve - mve1)
    diff_two:float = abs(comp_mve - mve2)

    if diff_one < diff_two:
        return mve1
    
    return mve2
    
