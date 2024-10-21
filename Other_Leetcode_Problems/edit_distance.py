import unittest


def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    rows = m + 1
    cols = n + 1
    dp = [[None] * cols for i in range(rows)]

    for i in range(rows):
        dp[i][0] = i

    for j in range(cols):
        dp[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


class test_cases(unittest.TestCase):

    def test_case_cat_cut(self):
        str1 = "cat"
        str2 = "cut"
        desired_output = 1
        actual_output = edit_distance(str1=str1, str2=str2)
        message = "Desired and actual values are not equal"
        self.assertEqual(desired_output, actual_output, message)

    def test_case_horse_ros(self):
        str1 = "horse"
        str2 = "ros"
        desired_output = 3
        actual_output = edit_distance(str1=str1, str2=str2)
        message = "Desired and actual values are not equal"
        self.assertEqual(desired_output, actual_output, message)

    def test_case_intention_execution(self):
        str1 = "intention"
        str2 = "execution"
        desired_output = 5
        actual_output = edit_distance(str1=str1, str2=str2)
        message = "Desired and actual values are not equal"
        self.assertEqual(desired_output, actual_output, message)


if __name__ == '__main__':
    unittest.main()
