# Gull Code 2019 Problems

Problems from the 2019 Gull Code Competition at SU.  (None of the files included were coded at the competition, these are practice files)

Each of these problems were completed without internet sources, otherwise it wouldn't even be practice.  I coded them in both C++ and Python, giving myself limited time to work on these and attempted to make them as efficient as possible (tested each input/output on the old Gull Code 2019 link from the actual competition to ensure completeness).  This is mostly just practice for Gull Code 2020, so any problems that are incomplete/broken will eventually be fixed.  Below are my team's actual statistics at the competition:

## Gull Code 2019 (November 16) Results

Competition Information (my first ever coding comp!):

- Team Members: myself (CS & DS double major, sophomore), Ian Thomas (CS major & web dev god, junior), Michael Mandulak (CS major, junior).
- Team Name: Stable Marriage.
- Language & tech used: C++, Ian's macbook air, a sick gaming keyboard & mouse, and a mousepad.


Competition Results:

- Team Score & Standing: 251/600, 5th/17th place.
- Problems Completed: (5) Nth Prime, (7) Bulls & Heifers, (8) Rainfall, (12) Out of the box adding, (2) Count Down.
- Problems Nearly Completed: (6) 101doors, (4) SkyScraper Skyline.
- Problems Attempted & Missed: (1) Knights Tour, (9) Paper Strip Game.
- Problems Not Attempted: (3) Loopy Robots, (10) SAT Problem, (11) Random Dataset Linear Regression.

## Problem List


### (1) Knight's Tour

In the game of chess, a knight can move in a very special way. It travels a total of three spaces per move in an 'L' shape fashion. For example, if the knight is in square (1, 1) on an empty standard 8x8 chessboard, it can move it down two and right one (3, 2), or right two and down one. (2, 3). 

Your task is to calculate all series of 64 legal knight moves that result in the knight visiting every square on the chessboard exactly once, when the knight starts from a given coordinate. This is known as the Knight's Tour. The input is the starting row and column (starting at 1) of the knight, the output should be the number of possible paths that the Knight's Tour can follow.

Sample Input: 1 1

Sample Output:2


### (2) Count Down

Sometimes you ask, "How long until my 21st birthday?" or, "When does Thanksgiving Break start?". Your task is to count down how far away a certain date is from today, Nov. 16th, 2019. Input will be 3 integers consisting of YYYY MM DD, and output should be an integer representing the number of days away it is.

Output is # days from the start date to the end date, but not including the end date.

Sample Input: 2019 11 20

Sample Output: 4


### (3) Loopy Robots

We have a robot that has been deployed on an infinite plane at position (0, 0) facing North. It is programmed to indefinitely execute a command string. He has been programmed with the following commands:

F: Step one in the direction that he is facing
+: Rotate 90 degrees clockwise
- : Rotate 90 degrees counter-clockwise
 When the execution reaches the end of the command string, it repeats.

Your job is to determine if a command string results in the robot repeating the same path, or not. In simpler terms, will the robot "loop" on any set of coordinates? The input will consist one string with a combination of the letters: "F", "+", "-". Your output should contain 0 if there is not a loop, and 1, #number of command strings it took to reach the loop, if there is a loop.

Note: Not all command strings will contain at least one of each instruction

Sample Input 1: F+

Sample Output 1: 1 4

Sample Input 2: F

Sample Output 2: 0


### (4) SkyScraper Skyline

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B). The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

