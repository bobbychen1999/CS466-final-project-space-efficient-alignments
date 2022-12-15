# Space Efficient Alignments

## Introduction and motivation
This project is to implement space-efficient sequence alignment. Given two sequences `v` (with length m) and `w` (with length n, m < n), this algorithm can run global / fitting / local alignments in `O(mn)` time and `O(m)` space. Compare to standard dynamic programming algorithm which takes `O(mn)` time and `O(mn)` space, this algorithm uses similar time but can save space significantly.

## Usage
In `main_algorithm` file, there are three function calls:
- `global_alignment(v, w)`, which calls the space-efficient global alignment function
- `fitting_alignment(v, w)`, which calls the space-efficient fitting alignment function
- `local_alignment(v, w)`, which calls the space-efficient local alignment function

To use any of those three function for global, fitting or local alignment, you need to:
1. clone this whole repository in your local
2. in Terminal, direct to the repository directory in your local
3. Take global alignment of "ACT" and "TAC" as an example, you can call `python3 -c 'import main_alignment; main_alignment.global_alignment("ACT", "TAC")'` in your Terminal
4. You'll get a string printed out like: `-ACT TAC-`, this will be the aligned sequences, separated by a space in the middle

## Visualization
Another way to run this algorithm is to use [the website](https://github.com/yuehaoshi/SpaceEfficientAlignmentWeb) developed by the team:

<a href="https://github.com/yuehaoshi/SpaceEfficientAlignmentWeb" target="_blank">
<img width="541" alt="Screenshot 2022-12-15 at 01 04 12" src="https://user-images.githubusercontent.com/70357591/207794707-303696c8-da02-4163-a77f-8236c7d42e3b.png">
</a>

You'll find details about how to run and use it inside its "ReadMe" file.

## Testing
- For correctness, since there might be break-tie cases where will cause slight difference in alignment results, the team choose the alignment scores generated by two methods as comparison goal. First, the team randomly generates v and w of lengths from 10 to 100, then testing them using our algorithms and the base cases, reporting failures if the alignment our algorithm returned has the incorrect score or print out score comparison result if succeed. After iteratively running the test for 100 times, no error had occurred. 

- For space and time efficiency, the team used “memory_profiler” package in python to measure the space consumption by print out memory usage in each step of two methods, and used “timeit” package to measure the time consumption. The team generate random sequences with length from 2000 to 2500 to compare the space and time consumption by running fitting alignment test with those generated sequences. The space consumption result shows that the space-effieicient alignment saves space significantly compared to standard dynamic programming alignment algorithm, and are 2-log smaller compared to standard DP alignment method shown in the log scale plot. The time consumption result shows that the space-efficient alignment spends around three more amount of time compared to the standard DP method, this is reasonable because in space-efficient fitting alignment, we calculated “findStart()”, “findEnd()” and then call Hersenberg, which is taking O(3mn) time, whereas the standard DP method only takes O(1*mn) time. The log scale plot for time shows that the difference of both methods are within 1-log scope.

- Detailed Testing result can be found in this file: `Space_Efficient_Alignment_Test.ipynb`, which contains testing results for emmory & time consumption, corresponding plot, as well as real-life alignment results using human genome sequence.
