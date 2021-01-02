# Nurikabe puzzle solver
## General info
In this repo i'll make script solving nurikabe, and tests in pytest. Then I want to make simple GUI for this project.

### Nurikabe rules
There are 5 rules in classic nurikabe puzzle:
* Each island contains exactly one clue.
* The number of squares in each island equals the value of the clue.
* All islands are isolated from each other horizontally and vertically.
* There are no wall areas of 2x2 or larger.
* When completed, all walls form a continuous path.

[rules form here!](https://www.conceptispuzzles.com/index.aspx?uri=puzzle/nurikabe/rules "conceptispuzzles.com")

### My notation
0 - unassigned field\
"*" - river\
"#" - island\
example:\
[0, 1, 0, 1, 0], ---> ["\*", 1 ,"\*", 1 ,"\*"]\
[0, 0, 0, 0, 0], ---> ["\*","\*","\*","\*","\*"]\
[3, 0, 0, 0, 3], ---> [ 3 ,"#","#","\*", 3 ]\
[0, 0, 0, 0, 0], ---> ["\*","\*","\*","\*","#"]\
[3, 0, 0, 0, 0], ---> [ 3 ,"#","#","\*","#"]
