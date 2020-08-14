This is the source code for the coding challenge from OverBond AI. 

Challenge 1:

Approach:

Used Pandas to read input csv. Filtered the data based on corporate and government bond types, found the minimum difference in bond terms and found the yield spread.




Output
bond,benchmark,spread_to_benchmark
C1 G1 1.6%
C2 G2 1.5%
C3 G3 2.0%
C4 G3 2.9%
C5 G4 0.9%
C6 G5 1.8%
C7 G6 2.5%

Challenge 2:

Approach:

Used Pandas to read input csv. Filtered the data based on corporate and government bond types, created a function to find the interpolated output for the corporate bond and based on the interpolated values calculated the yield spread to curve

Output
bond,spread_to_curve
C1 1.43%
C2 1.63%
C3 2.47%
C4 2.27%
C5 1.9%
C6 1.57%
C7 2.83%
