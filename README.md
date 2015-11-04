Nicholas Pickering
Operating Systems COP4610
Project 2 - Analysis of Uniprocessor Scheduling Algorithms
Professor Littleton
Date Due: 11/15/2015
Date Submitted 11/15/2015

# Introduction
This program simulates several uniprocessor scheduling aglorithms including:
- First Come, First Serve (FCFS),
- Shortest Job Next (SJN),
- Shortest Remaining Time (SRT),
- and Round Robin.

# Invoking the application
Invoke the application by calling:
    ./p2 filename time_quantum

    where filename points to a file containing a sequence of jobs
    and time_quantum is the value to be used by Round Robin as the Time Quantum

# Output Files
This program produces a single output file: results.txt.

results.txt contains the output of the program after it has completed.

The file is stored in the output directory.

# Test Data
The project contains a directory named "data" which contains the provided test files.

These files may be used to test the application, as well as any text file formed of any number of lines, each
with two integers comma-separated. The first integer in the list simulates the time the arrival of the process,
the second number represents the number of time cycles that job is expected to take.
