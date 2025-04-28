# Problem Description:

"""
                                         Tournament Winner

There's an algorithms tournament taking place in which teams of programmers compete against each other to solve
algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces off against all
other teams. Only two teams compete against each other at a time, and for each competition, one team is designated
the home team, while the other team is the away team. In each competition there's always one winner and one loser;
there are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the
team that receives the most amount of points.

Given an array of pairs representing the teams that have competed against each other and an array containing the results
of each competition, write a function that returns the winner of the tournament. The input arrays are named `competitions`
and `results`, respectively. The `competitions` array has elements in the form of `[home_team, away_team]`, where each
team is a string of at most 30 characters representing the name of the team. The`results` array contains information about
the winner of each corresponding competition in the `competitions` array. Specifically, `results[i]` denotes the winner of
`competitions[i]`, where a`1` in the `results` array means that the home team in the corresponding competition won and
a `0` means that the away team won.

It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams
exactly once. It's also guaranteed that the tournament will always have at least two teams.


## Sample Input:
```
competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
]
results = [0, 0, 1]
```

## Sample Output:
```
"Python"

// C# beats HTML, Python Beats C#, and Python Beats HTML.
// HTML - 0 points
// C# -  3 points
// Python -  6 points
```

## Optimal Time & Space Complexity:
```
O(n) time | O(k) space - where `n` is the number of competitions and `k` is the number of teams.
```

"""

# =========================================================================================================================== #

# Solution:


HOME_TEAM_WON = 1  # Constant indicating that the home team won the match


# O(n) time | O(k) space
def tournament_winner(competitions, results):
    current_best_team = ""  # Tracks the current team with the highest score
    scores = {current_best_team: 0}  # Dictionary to store scores of all teams

    # Loop through each competition and its corresponding result
    for idx, competition in enumerate(competitions):
        # The result of the current match (0 = away team won, 1 = home team won)
        result = results[idx]

        home_team, away_team = competition  # Extract home and away teams for the match

        # Determine the winning team based on the result
        winning_team = home_team if result == HOME_TEAM_WON else away_team

        # Update the winning team's score by adding 3 points
        update_scores(winning_team, 3, scores)

        # Check if the winning team's score is higher than the current best team's score
        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team  # Update the current best team

    return current_best_team  # Return the team with the highest score after all matches


# Function to update the score of a team in the scores dictionary
def update_scores(team, points, scores):
    if team not in scores:
        # If the team is not already in the dictionary, add it with a score of 0
        scores[team] = 0

    scores[team] += points  # Add the points to the team's current score


# Test Cases
competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]

competitions_2 = [["Bulls", "Eagles"], ["Bulls", "Bears"], ["Bears", "Eagles"]]
results_2 = [0, 0, 0]

competitions_3 = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
    ["SQL", "C#"],
    ["HTML", "SQL"],
    ["SQL", "Python"],
    ["SQL", "Java"],
]
results_3 = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]


print(tournament_winner(competitions, results))
# Output: Python
# Explanation: Python beats C#, then Python beats HTML, making Python the winner with 6 points.

print(tournament_winner(competitions_2, results_2))
# Output: Eagles
# Explanation: Eagles beat Bulls, Bears beat Bulls, and Bears beat Eagles. Eagles have the highest score of 3.

print(tournament_winner(competitions_3, results_3))
# Output: SQL
# Explanation: SQL wins three matches (vs. C#, Python, and Java), gaining 9 points to become the tournament winner.

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

The time complexity of the `tournament_winner` function is **O(n)**, where `n` is the number of competitions.

#### Explanation:
1. **Loop through competitions**: The function iterates through the `competitions` list once. Since there are `n`
competitions, this loop runs `n` times.

2. **Dictionary operations**: Inside the loop, the function performs dictionary operations like checking if a team
exists in the `scores` dictionary and updating its score. These operations are **O(1)** on average because dictionaries
in Python are implemented as hash tables.

3. **Overall**: Since the loop runs `n` times and each operation inside the loop is **O(1)**, the total time complexity is **O(n)**.

---

### Space Complexity:

The space complexity of the `tournament_winner` function is **O(k)**, where `k` is the number of unique teams.

#### Explanation:
1. **Scores dictionary**: The `scores` dictionary stores the points for each unique team. If there are `k` unique teams,
the dictionary will store `k` key-value pairs.

2. **Auxiliary space**: Apart from the `scores` dictionary, the function uses a constant amount of additional space 
(e.g., variables like `current_best_team`, `result`, `home_team`, `away_team`, etc.). This does not depend on the
input size and is considered **O(1)**.

3. **Overall**: The dominant factor in space complexity is the `scores` dictionary, which grows with the number of unique teams.
Thus, the space complexity is **O(k)**.

---

### Summary:
- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(k)**

Where:
- `n` = number of competitions
- `k` = number of unique teams

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Detailed Explanation of the Code**

This Python function `tournament_winner` determines the winner of a tournament given a list of matches and their results.
Let's break it down step by step.

---

## **1. Function Definition**
```
def tournament_winner(competitions, results):
```
- This function takes two parameters:
  1. `competitions`: A list of lists, where each sub-list contains two teams (`home_team` and `away_team`) competing
  against each other.
  2. `results`: A list of integers (either `0` or `1`), where:
     - `0` means the **away team** won.
     - `1` means the **home team** won.

---

## **2. Initialization**
```
    current_best_team = ""  # Tracks the current team with the highest score
    scores = {current_best_team: 0}  # Dictionary to store scores of all teams
```
- `current_best_team` is initially an empty string (`""`) because no matches have been played yet.
- `scores` is a dictionary that stores each team's total score. Initially, it contains `{"": 0}` to prevent key errors.

---

## **3. Iterating Through Each Match**
```
    for idx, competition in enumerate(competitions):
```
- We use `enumerate(competitions)` to iterate through each competition along with its index (`idx`), which helps us
retrieve the corresponding match result from `results`.

---

## **4. Determining the Winning Team**
```
        result = results[idx]  # Get the result for the current match
        home_team, away_team = competition  # Extract home and away teams
```
- `result` gets the outcome of the current match from `results` (either `0` or `1`).
- `home_team` and `away_team` are extracted from `competition`.

```
        winning_team = home_team if result == HOME_TEAM_WON else away_team
```
- `winning_team` is determined:
  - If `result == 1`, the `home_team` wins.
  - If `result == 0`, the `away_team` wins.

---

## **5. Updating the Scores**
```
        update_scores(winning_team, 3, scores)
```
- The `update_scores` function is called to add **3 points** to the winning team's score.

### **How `update_scores` Works**
```
def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0  # If the team is not in the dictionary, initialize its score

    scores[team] += points  # Add the points to the team's score
```
- If the `team` is not in `scores`, it is added with an initial score of `0`.
- The `points` (3 points per win) are added to the team's total.

---

## **6. Updating the Current Best Team**
```
        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team  # Update the current best team
```
- If the `winning_team` now has a higher score than `current_best_team`, we update `current_best_team`.

---

## **7. Returning the Final Winner**
```
    return current_best_team
```
- After all matches are processed, the team with the highest score is returned as the **tournament winner**.

---

## **Example Walkthrough**

Let's analyze the first test case:

### **Input**
```
competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]
```

### **Step-by-step Execution**

| Match | Home Team | Away Team | Result             | Winning Team | Scores Update                       |
|-------|-----------|-----------|--------------------|--------------|-------------------------------------|
| 1     | HTML      | C#        | 0 (Away team wins) | C#           | `{'C#': 3}`                         |
| 2     | C#        | Python    | 0 (Away team wins) | Python       | `{'C#': 3, 'Python': 3}`            |
| 3     | Python    | HTML      | 1 (Home team wins) | Python       | `{'C#': 3, 'Python': 6, 'HTML': 0}` |

### **Final Winner**
- `Python` has **6 points**, making it the tournament winner.

### **Output**
```
print(tournament_winner(competitions, results))  # Output: "Python"
```

---

## **Summary**
- The function iterates through all matches.
- It determines the winning team for each match.
- It updates the scores in a dictionary.
- It tracks the team with the highest score.
- It returns the tournament winner.

This algorithm runs in **O(N) time complexity**, where `N` is the number of matches, since it iterates 
through `competitions` once and updates scores in constant time.

"""
