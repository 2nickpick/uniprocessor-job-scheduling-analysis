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

# Main, Library
The entry point to the application is main.py. This program references several helper classes in the lib directory.

# Output Files
This program produces output to the console.

An example result set for each test is saved to the output directory, with the same name as tests.
Tests are available in the data directory.

# Test Data
The project contains a directory named "data" which contains the provided test files.

These files may be used to test the application, as well as any text file formed of any number of lines, each
with two integers comma-separated. The first integer in the list simulates the time the arrival of the process,
the second number represents the number of time cycles that job is expected to take.

# Round Robin Additional Testing
In my testing, a time quantum of 20 produced the best results. The results of my testing can be viewed in
the output directory, at output/round_robin_additional.txt.

I believe that QT = 20 produced the best results, because small QT's cause jobs that are close to completing to be
preempted, and held off until every other job has had a chance to run cycles.

If the time quantum were infinite, the Round Robin algorithm would behave essentially identical to FCFS. Each job
would run in its entirety, and then the next job in the queue would run, just like FCFS.

# Issues / Difficulties
The most difficult I had with this project was implementing the data structures necessary in Python,
specifically priority queues.

The Medium and Hard tests revealed two problems with my initial solution, that required fixes. For the medium test,
I needed to make sure that if two or more jobs arrive at the same time, they are all loaded into the queue correctly.

The hard test revealed that my program only loaded in the first job, even if there were multiple jobs available at the
beginning of the simulation.
