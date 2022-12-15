# CS466-final-project-space-efficient-alignments

## Introduction and motivation:¶
This project is to implement space-efficient sequence alignment. Given two sequences `v` (with length m) and `w` (with length n, m < n), this algorithm can run global / fitting / local alignments in `O(mn)` time and `O(m)` space. Compare to standard dynamic programming algorithm which takes `O(mn)` time and `O(mn)` space, this algorithm uses similar time but can save space significantly.

## Usage:
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
Another way to run this algorithm is to use [the website](https://github.com/yuehaoshi/SpaceEfficientAlignmentWeb) developed by the team.  

You'll find details about how to run and use it inside its "ReadMe" file.
