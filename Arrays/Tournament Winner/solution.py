# Description:

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

## Optimal Space & Time Complexity:

`O(n)` time | `O(k)` space - where `n` is the number of competitions and `k` is the number of teams.

"""

HOME_TEAM_WON = 1  # Constant indicating that the home team won the match


# O(n) time | O(k) space - where `n` is the number of competitions and `k` is the number of teams
def tournament_winner(competitions, results):
    current_best_team = ""  # Tracks the current team with the highest score
    scores = {current_best_team: 0}  # Dictionary to store scores of all teams

    # Loop through each competition and its corresponding result
    for idx, competition in enumerate(competitions):
        result = results[
            idx
        ]  # The result of the current match (0 = away team won, 1 = home team won)
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
    if (
        team not in scores
    ):  # If the team is not already in the dictionary, add it with a score of 0
        scores[team] = 0

    scores[team] += points  # Add the points to the team's current score


# Example test cases to check the function's behavior
print(
    tournament_winner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1])
)  # Output: Python
# Explanation: Python beats C#, then Python beats HTML, making Python the winner with 6 points.

print(
    tournament_winner(
        [["Bulls", "Eagles"], ["Bulls", "Bears"], ["Bears", "Eagles"]], [0, 0, 0]
    )
)  # Output: Eagles
# Explanation: Eagles beat Bulls, Bears beat Bulls, and Bears beat Eagles. Eagles have the highest score of 3.

print(
    tournament_winner(
        [
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
        ],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    )
)  # Output: SQL
# Explanation: SQL wins three matches (vs. C#, Python, and Java), gaining 9 points to become the tournament winner.

print(tournament_winner([["Bulls", "Eagles"]], [1]))  # Output: Bulls
# Explanation: Bulls beat Eagles in the only match, earning 3 points and becoming the winner.


# Big O:

"""

### Time and Space Complexity

1. **O(n) Time Complexity**:
   - Iterates over the `competitions` list once, where `n` is the number of games.
   - Each lookup and update in the `scores` dictionary is O(1).
   
2. **O(k) Space Complexity**:
   - Stores scores for at most `k` teams in the `scores` dictionary, where `k` is the number of unique teams.

"""


# Code Explanation:

"""

The code calculates the winner of a sports-style tournament by keeping track of team scores across multiple games.
Each game has a winner, and points are awarded based on the results. The team with the highest score at the end
of all games is declared the winner.

#### Input and Output
- **Input**:
  - `competitions`: A list of games. Each game is represented as a list of two teams `[home_team, away_team]`.
  - `results`: A list of integers where:
    - `1` means the home team won.
    - `0` means the away team won.
- **Output**:
  - The name of the team with the highest score at the end of all games.

#### Constants
```
HOME_TEAM_WON = 1
```
This constant is used for clarity in understanding what `1` represents in the `results` list (a home team victory).

---

### Functions
#### 1. `tournament_winner()`
This function processes the games and determines the overall tournament winner.

##### Steps:
1. **Initialization**:
   - `current_best_team`: Tracks the team currently leading in scores. Initially, it's an empty string.
   - `scores`: A dictionary to store scores for each team. It starts with the `current_best_team` having a score of `0`.

   ```
   current_best_team = ""
   scores = {current_best_team: 0}
   ```

2. **Iterating through games**:
   - For each game, retrieve the `home_team` and `away_team` from `competitions`.
   - Use the `results` list to determine the winning team.
     - If `results[idx] == HOME_TEAM_WON`, the `home_team` won.
     - Otherwise, the `away_team` won.
   - Update the winning team's score by adding 3 points (using the `update_scores` function).
   - Check if the winning team's score is greater than the `current_best_team`. If yes, update the `current_best_team`.

   ```
   for idx, competition in enumerate(competitions):
       result = results[idx]
       home_team, away_team = competition

       winning_team = home_team if result == HOME_TEAM_WON else away_team

       update_scores(winning_team, 3, scores)

       if scores[winning_team] > scores[current_best_team]:
           current_best_team = winning_team
   ```

3. **Return the winner**:
   - After processing all games, return the `current_best_team`.

   ```
   return current_best_team
   ```

---

#### 2. `update_scores()`
This helper function updates the score for a given team.

##### Steps:
1. If the team is not already in the `scores` dictionary, add it with a score of `0`.
2. Add the specified `points` (3 in this case) to the team's current score.

```
def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points
```

---

### Example Walkthrough
#### Input:
```
competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]
```

#### Process:
1. **Game 1**: `["HTML", "C#"]`, `result = 0`
   - `winning_team = "C#"` (away team won).
   - Update `scores`: `{"": 0, "C#": 3}`.
   - `current_best_team = "C#"`.

2. **Game 2**: `["C#", "Python"]`, `result = 0`
   - `winning_team = "Python"` (away team won).
   - Update `scores`: `{"": 0, "C#": 3, "Python": 3}`.
   - No change to `current_best_team` (scores are tied).

3. **Game 3**: `["Python", "HTML"]`, `result = 1`
   - `winning_team = "Python"` (home team won).
   - Update `scores`: `{"": 0, "C#": 3, "Python": 6}`.
   - `current_best_team = "Python"`.

#### Final Scores:
```
scores = {"": 0, "C#": 3, "Python": 6}
```

#### Output:
```
"Python"
```

---

#### **Edge Cases**:
   - A single game: Returns the winner of that game.
   - All results favor the away team or home team.
   
---

### Outputs for Provided Test Cases
1. `tournament_winner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1])`
   - **Output**: `"Python"`

2. `tournament_winner([["Bulls", "Eagles"], ["Bulls", "Bears"], ["Bears", "Eagles"]], [0, 0, 0])`
   - **Output**: `"Eagles"`

3. `tournament_winner([...], [0, 0, 0, 0, 0, 0, 1, 0, 1, 1])`
   - **Output**: `"SQL"`

4. `tournament_winner([["Bulls", "Eagles"]], [1])`
   - **Output**: `"Bulls"`

"""
