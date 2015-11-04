#
#
#   Main
#   This module acts as the starting point for the simulation
#
#   The goal of this project is to simulate several processor scheduling algorithms.
#   The program accepts a file with any number of lines, each line consisting of two integers separated by a comma.
#
#   The algorithms are simulated in the following order:
#   - First Come First Serve (FCFS)
#   - Shortest Job Next (SJN)
#   - Shortest Remaining Time (SRT)
#   - Round Robin
#
#

import sys
from collections import deque
from lib import util, fcfs, sjn, srt, round_robin

__author__ = 'Nicholas Pickering'


location = 0
filename = ''
time_quantum = 0

generate_obj = False

#   Start Main Program
print("Uniprocessor Scheduling Algorithm Simulation")
print("Written by Nicholas Pickering")

#   Read in file for processing...
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    util.error("No filename specified... Exiting...", True)

file = open(filename, "r")
if not file:
    util.error("File could not be loaded... Exiting...", True)

#   Validate Time Quantum
if len(sys.argv) > 2 and int(sys.argv[2]) > 0:
    time_quantum = int(sys.argv[2])
else:
    util.error("Invalid Time Quantum (second argument)... Exiting...", True)

#
#   Process Input
#
jobs = util.load_file(file)

print("\nFile processed:\t{0}".format(filename))
print("Time Quantum:\t{0} \n".format(time_quantum))

results = [
    fcfs.simulate(jobs),
    sjn.simulate(jobs),
    srt.simulate(jobs),
    round_robin.simulate(jobs, time_quantum)
]

algorithms = [
    "FCFS",
    "SJN",
    "SRT",
    "Round Robin"
]

min_time = min(results)
correct_algorithms = []
for index, algorithm in enumerate(algorithms):
    if results[index] == min_time:
        correct_algorithms.append(algorithm)

print("Best Policy is {0} with an Average Turn-around Time of {1}".format(', '.join(correct_algorithms), min_time))

#print("Additional Round Robin Testing\n")

#results = []
#time_quantums = [1, 2, 5, 10, 15, 20]
#for time_quantum in time_quantums:
#    results.append(round_robin.simulate(jobs, time_quantum))

#print(results)
