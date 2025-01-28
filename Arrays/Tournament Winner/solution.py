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

HOME_TEAM_WON = 1


# O(n) time | O(k) space - where `n` is the number
# of competitions and `k` is the number of teams
def tournament_winner(competitions, results):
    current_best_team = ""
    scores = {current_best_team: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition

        winning_team = home_team if result == HOME_TEAM_WON else away_team

        update_scores(winning_team, 3, scores)

        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team

    return current_best_team


def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points


print(
    tournament_winner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1])
)  # Output: Python
print(
    tournament_winner(
        [["Bulls", "Eagles"], ["Bulls", "Bears"], ["Bears", "Eagles"]], [0, 0, 0]
    )
)  # Output: Eagles
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
print(tournament_winner([["Bulls", "Eagles"]], [1]))  # Output: Bulls

# Big O:

"""

### Time and Space Complexity


"""


# Code Explanation:

"""



"""
