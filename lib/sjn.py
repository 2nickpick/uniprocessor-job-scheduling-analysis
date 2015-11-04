#
#
#   SJN
#   This module handles the simulation of Shortest Job Next
#
import heapq

from lib import util
from collections import deque
from statistics import mean

#   Simulate
#   Simulate the SJN algorithm
#
#   jobs - the jobs to simulate


def simulate(jobs):
    print("Shortest Job Next (SJN) Information:")

    # initialize variables
    results = []

    current_cycle = 0
    job_id = 1

    # don't overwrite the main jobs array
    jobs = util.deepcopy(jobs)

    # sort jobs by arrival
    jobs.sort(key=lambda x: x[0])

    # add Job IDs to jobs
    i = 0
    for job in jobs:
        job.append(i)
        i += 1

    # start our queue
    jobs = deque(jobs)
    job_queue = []
    heapq.heapify(job_queue)

    while len(jobs) > 0 and jobs[0][0] == current_cycle:
        job_queue.append(jobs.popleft())

    while len(job_queue) > 0:
        # grab the next job to process (sort by priority first)
        job_queue.sort(key=lambda x: x[1])
        job = heapq.heappop(job_queue)

        job_arrived = job[0]
        cycles_to_run = job[1]
        job_id = job[2]

        # simulate each cycle
        while cycles_to_run > 0:
            current_cycle += 1
            cycles_to_run -= 1

            # if a job is available, move it to the queue
            while len(jobs) > 0 and jobs[0][0] == current_cycle:
                job_queue.append(jobs.popleft())

        results.append([job_id, current_cycle - job_arrived])

    results.sort(key=lambda x: x[0])

    for result in results:
        print("Job {1} Turn-around Time: {0} ".format(result[1], chr(result[0] + 65)))

    print("Average Turn-around Time: {0}\n".format(mean([result[1] for result in results])))
