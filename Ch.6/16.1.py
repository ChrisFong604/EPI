# Using a bottom-up approach, the iterative sub-problem 

def computeScoreSequences(final_score: int, plays: list[int]) -> int:
    dp = [0] * (final_score + 1)

    # Initialize base cases
    for score in plays:
        dp[score] = 1

    for i in range(plays[0] + 1, final_score + 1):
        for score in plays:
            if i >= score:
                dp[i] += dp[i-score]              

    print(dp)

computeScoreCombinations(12, [2,3,7])