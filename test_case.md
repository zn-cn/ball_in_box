# ball_in_box

**Description Review**
>This program is used to solve a algorithm problem.
>The detailed description is that in a given box by [-1,1], given m balloons(they cannot overlap) with variable radio r and position mu, some tiny blocks  are in the box at given posiion {d}, which balloons cannot overlap with, we should find the optimal value of r nd mu which maxmizes sum r^2. 


#Test Case
written by Jeffcoding
May 30, 2018 10:00 PM

_ _ _
**This file describes one testing case of the program,with fixed input of m and blockers.
Detailed contents are as follows:**
**1.Prerequisites**

**2.Input**

**3.Operation method**

**4.Expected output**

**5.Actual output**



####1.Prerequisites (Preset Conditions)：

1.Running environment:Python 3.5

2.Environment are settled correctly
- number of Blockers:  2
- settled box
 - XRANGE:  (-1, 1)
YRANGE:  (-1, 1)
- Blockers 
 - [(0.5, 0.5), (0.5, -0.3)] 
- Number of circles: m = 5

3.the ``percision`` is small enough so as to workout an accurate value.


####2.Input
- "m" , "number of Blockers" and blockers' location are actually virable, depending on user's input.
 in this case, we just view them as a series of fixed values.(As written in preset conditions)

####3.Operation method

1.Find the location of the program

2.open the shell

3.type "python3 area_sym.py"
 
####4.Expected output
- Total area = 3

####5.Actual output
- circles: 
(x, y) -> ( -0.196000,   0.100000), r ->   0.802755

(x, y) -> (  0.660000,  -0.660000), r ->   0.340000

(x, y) -> (  0.708000,   0.712000), r ->   0.288000

(x, y) -> ( -0.768000,  -0.768000), r ->   0.232000

(x, y) -> (  0.792000,  -0.128000), r ->   0.208000

- Total area = 2.953247890821777
p.s. picture of actual output
![](http://chuantu.biz/t6/322/1527686475x-1376440102.jpg)
