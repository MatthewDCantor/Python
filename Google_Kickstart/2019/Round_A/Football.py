"""
------ Summary -----

N students
P size team
with S[i] = skill rating per student

For a team to be deemed fair, everyone on team P must have the same skill
as the player with the highestvskill. If we train a student for 1 hour,
their skill rating is raised by 1.
What is the minimum number of hours spent train to have a fair team?
---------------------------

------ Sample input & output ------

INPUT
'3'
'4 3'
'3 1 9 100'
'6 2'
'5 5 1 2 3 4'
'5 5'
'7 7 1 7 7'

OUTPUT
Case #1: 14
Case #2: 0
Case #3: 6

"""

"""
Get input
"""

T = int(input())

for t in range(T):
    N,P = list(map(int, input().split(' ')))
    student_skill = list(map(int, input().split(' ')))
    student_skill.sort()
    s = [0]
    for i in student_skill:
        s.append(s[-1] + i)
    x = float("inf")
    for i in range(N-P+1):
        y = student_skill[i+P-1]*P
        y -= s[i+P] - s[i]
        x = min(x,y)



    print("Case #" + str(t+1) + ": " + str(x))
