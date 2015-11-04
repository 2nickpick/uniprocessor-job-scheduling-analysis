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
from lib import util, fcfs, sjn, srt

__author__ = 'Nicholas Pickering'


location = 0
filename = ''
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

#
#   Process Input
#
jobs = util.load_file(file)

print("\nFile processed: {0} \n".format(filename))

fcfs_results = fcfs.simulate(jobs)
sjn_results = sjn.simulate(jobs)
srt_results = srt.simulate(jobs)
