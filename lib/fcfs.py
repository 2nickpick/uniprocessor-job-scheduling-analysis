#
#
#   FCFS
#   This module handles the simulation of First Come, First Serve
#

from lib import util
from collections import deque
from statistics import mean

#   Simulate
#   Simulate the FCFS algorithm
#
#   jobs - the jobs to simulate


def simulate(jobs):
    print("First Come, First Serve (FCFS) Information\n")

    # don't overwrite the main jobs array
    jobs = util.deepcopy(jobs)

    # generate our queue
    jobs = deque(jobs)
    results = []

    cycle = 0
    job_id = 1

    while len(jobs) > 0:
        job = jobs.popleft()

        cycles_to_run = job[1]

        while cycles_to_run > 0:
            cycle += 1
            cycles_to_run -= 1

        results.append(cycle-job[0])
        print("Job {1} Turn-around Time: {0} ".format(cycle - job[0], job_id))

        job_id += 1

    print("Average Turn-around Time: {0}".format(mean(results)))
