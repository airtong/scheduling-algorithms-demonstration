import time
import pandas as pd
import threading
import os
from tabulate import tabulate

# sleep time in seconds
sleep_time = 1

softwares = {
    1: {
        "name": "Microsoft Excel",
        "priority": 1,
        "burst": 100,
    },
    2: {
        "name": "Microsoft Teams",
        "priority": 4,
        "burst": 500,
    },
    3: {
        "name": "Microsoft Edge",
        "priority": 3,
        "burst": 800,
    },
    4: {
        "name": "Google Chrome",
        "priority": 3,
        "burst": 600,
    },
    5: {
        "name": "Visual Studio Code",
        "priority": 2,
        "burst": 200,
    }
}

# table with columns: fcfs, sjf, ps and rows from 100 ms to 2200 ms, jumping by 100 ms, filled with ''
table = pd.DataFrame(index=range(100, 2201, 100), columns=['fcfs', 'sjf', 'ps']).fillna('')

def custom_print():
    for i in range(0, 23, 1):
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Format table
        formatted_table = tabulate(table, headers='keys', tablefmt='pretty', showindex=True, numalign='center')
        formatted_table = formatted_table.replace(" ms", "")
        print(formatted_table)
        time.sleep(sleep_time)

# first-come-first-served algorithm
def fcfs():
    fcfs_softwares = softwares
    row = 0
    for order, software in fcfs_softwares.items():
        for i in range (100, software['burst'] + 1, 100):
            row += 100
            table.loc[row, 'fcfs'] = software['name']
            time.sleep(sleep_time)

# shortest-job-first algorithm
def sjf():
    sjf_softwares = softwares
    # sort sjf_softwares by burst
    sjf_softwares = sorted(sjf_softwares.values(), key=lambda x: x['burst'])

    row = 0
    for software in sjf_softwares:
        for i in range(100, software['burst'] + 1, 100):
            row += 100
            table.loc[row, 'sjf'] = software['name']
            time.sleep(sleep_time)

# priority scheduling algorithm
def ps():
    ps_softwares = softwares
    # sort ps_softwares by priority
    ps_softwares = sorted(ps_softwares.values(), key=lambda x: x['priority'])

    row = 0
    for software in ps_softwares:
        for i in range(100, software['burst'] + 1, 100):
            row += 100
            table.loc[row, 'ps'] = software['name']
            time.sleep(sleep_time)

# Thread instances for each algorithm
thread1 = threading.Thread(target=fcfs)
thread2 = threading.Thread(target=sjf)
thread3 = threading.Thread(target=ps)
thread4 = threading.Thread(target=custom_print)

# Initializing the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Waiting for the threads to finish
thread1.join()
thread2.join()
thread3.join()
thread4.join()
