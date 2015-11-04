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

    # don't overwrite the main jobs array
    jobs = util.deepcopy(jobs)

    jobs.sort(key=lambda x: x[0])

    # start our queue
    jobs = deque(jobs)
    job_queue = [jobs.popleft()]
    heapq.heapify(job_queue)

    print(jobs)
    print(job_queue)

    results = []

    current_cycle = 0
    job_id = 1

    while len(job_queue) > 0:
        # grab the next job to process (sort by priority first)
        job_queue.sort(key=lambda x: x[1])
        job = heapq.heappop(job_queue)

        job_arrived = job[0]
        cycles_to_run = job[1]

        # simulate each cycle
        while cycles_to_run > 0:
            current_cycle += 1
            cycles_to_run -= 1

            # if a job is available, move it to the queue
            if len(jobs) > 0 and jobs[0][0] == current_cycle:
                job_queue.append(jobs.popleft())

        results.append(current_cycle - job_arrived)
        print("Job {1} Turn-around Time: {0} ".format(current_cycle - job_arrived, job_id))

        job_id += 1

    print("Average Turn-around Time: {0}\n".format(mean(results)))
