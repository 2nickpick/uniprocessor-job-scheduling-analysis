#
#
#   Round Robin
#   This module handles the simulation of Round Robin
#
import heapq

from lib import util
from collections import deque
from statistics import mean

#   Simulate
#   Simulate the Round Robin algorithm
#
#   jobs - the jobs to simulate


def simulate(jobs, time_quantum):
    print("Round Robin Information (Time Quantum = {0}):".format(time_quantum))

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
    job_queue = deque()

    while len(jobs) > 0 and jobs[0][0] == current_cycle:
        job_queue.append(jobs.popleft())

    #print("Cycle\tJob\t\tCycles Left\t\tQuantum Left")
    while len(job_queue) > 0:
        # grab the next job to process
        job = job_queue.popleft()

        job_arrived = job[0]
        cycles_to_run = job[1]
        job_id = job[2]

        # new job starting, reset time quantum
        time_quantum_left = time_quantum

        # simulate each cycle
        preempt = False
        while cycles_to_run > 0 and not preempt:
            current_cycle += 1
            cycles_to_run -= 1
            time_quantum_left -= 1

            #print("{0}\t\t{1}\t\t{3}\t\t\t\t{2}".format(current_cycle, chr(job_id+65), time_quantum_left, cycles_to_run))
            #print(job_queue)

            # if a job is available, move it to the queue
            while len(jobs) > 0 and jobs[0][0] == current_cycle:
                new_job = jobs.popleft()
                job_queue.append(new_job)

            # check if we need to preempt
            if time_quantum_left == 0 and cycles_to_run > 0:
                job_queue.append([job_arrived, cycles_to_run, job_id])
                preempt = True

        if cycles_to_run == 0 and not preempt:
            results.append([job_id, current_cycle - job_arrived])

    results.sort(key=lambda x: x[0])

    for result in results:
        print("Job {1} Turn-around Time: {0} ".format(result[1], chr(result[0] + 65)))

    time = mean([result[1] for result in results])
    print("Average Turn-around Time: {0}\n".format(time))

    return time
