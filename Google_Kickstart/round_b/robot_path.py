"""------------Problem-------------

Your country's space agency has just landed a rover on a new planet, which
can be thought of as a grid of squares containing 109 columns (numbered starting
from 1 from west to east) and 109 rows (numbered starting from 1 from north to
south). Let (w, h) denote the square in the w-th column and the h-th row.
The rover begins on the square (1, 1).

The rover can be maneuvered around on the surface of the planet by sending
it a program, which is a string of characters representing movements
in the four cardinal directions.
The robot executes each character of the string in order:
N: Move one unit north.
S: Move one unit south.
E: Move one unit east.
W: Move one unit west.
There is also a special instruction X(Y), where X is a number between 2 and 9
inclusive and Y is a non-empty subprogram. This denotes that the robot should
repeat the subprogram Y a total of X times. For example:
2(NWE) is equivalent to NWENWE.
3(S2(E)) is equivalent to SEESEESEE.
EEEE4(N)2(SS) is equivalent to EEEENNNNSSSS.

Since the planet is a torus, the first and last columns are adjacent,
so moving east from column 109 will move the rover to column 1 and moving south
from row 109 will move the rover to row 1. Similarly, moving west from column 1
will move the rover to column 109 and moving north from row 1 will move
the rover to row 109. Given a program that the robot will execute,
determine the final position of the robot after it has finished
all its movements.


-------------Input & Output--------------

'4'
'SSSEEE'
'N'
'N3(S)N2(E)N'
'2(3(NW)2(W2(EE)W))'


Case #1: 4 4
Case #2: 1 1000000000
Case #3: 3 1
Case #4: 3 999999995

------------Solution-----------------

use x,y trackers instead of creating a matrix of 10e9*10e9

if 10e9 > x,y > 0 then make the tracker back on the grid.

if command of N,S,E,W is given, then increment the respective counter.
if X() is encountered then collect increments until ) is encountered. Once ) is
found, then multiply all increments by X. This function will be called
recursively when there are nested parenthesis.


"""
def navigate():

    command = input()
    command += "X"
    x,y = [1,1]
    special_numbers = ['2','3','4','5','6','7','8','9']


    def special(index,X,command):


        temp_x = 0
        temp_y = 0

        while command[index] != ")":

            if command[index] == 'S':
                temp_y += 1
                index += 1

            if command[index] == 'N':
                temp_y -= 1
                index +=1

            if command[index] == 'E':
                temp_x += 1
                index += 1

            if command[index] == 'W':
                temp_x -= 1
                index += 1

            if command[index] in special_numbers:
                index += 2
                special_x,special_y,index = special(index,int(command[index-2]),command)
                temp_x += special_x
                temp_y += special_y
                index += 1

        return X*temp_x,X*temp_y,index


    i = 0

    while i <= len(command)-1:


        if command[i] == 'S':
            y += 1
            i += 1

        if command[i] == 'N':
            y -= 1
            i += 1

        if command[i] == 'E':
            x += 1
            i += 1

        if command[i] == 'W':
            x -= 1
            i += 1

        if command[i] in special_numbers:
            i += 2
            special_x,special_y,i = special(i,int(command[i-2]),command)
            x += special_x
            y += special_y
            i += 1


        while x > 1000000000:
            x -= 1000000000
        while x <= 0:
            x += 1000000000
        while y > 1000000000:
            y -= 1000000000
        while y <= 0:
            y += 1000000000


        if command[i] == "X":
            return x,y


rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split( )))

test_cases = rri()

for t in range(1,test_cases+1):

    answer = navigate()

    print("Case #{}: {} {}".format(t,answer[0],answer[1]))
