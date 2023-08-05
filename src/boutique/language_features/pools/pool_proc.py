"""
Pool distributes the tasks to the available processors using a FIFO
scheduling. It works like a map reduce architecture. It maps the input to the
different processors and collects the output from all the processors. After the
execution of code, it returns the output in form of a list or array. It waits
for all the tasks to finish and then returns the output. The processes in
execution are stored in memory and other non-executing processes are stored out
of memory.
Process puts all the processes in memory and schedules execution
using FIFO policy. When the process is suspended, it pre-empts and schedules
new process for execution.
"""

from multiprocessing import Pool
from multiprocessing import Process
import os


def f1(x):  # for Pool
    return x * x


def info(title):
    print(title)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())


def f2(name):  # for Process
    info("function f2")
    print("hello", name)


if __name__ == "__main__":
    print("part 1 Pool")
    with Pool(5) as p1:
        print(p1.map(f1, [10, 11, 12]))
    print()

    print("part 2 Process")
    info("main line")
    p2 = Process(target=f2, args=("bob",))
    p2.start()
    p2.join()

"""
part 1 Pool
[100, 121, 144]
part 2 Process
main line
module name: __main__
parent process: 5
process id: 2706
function f2
module name: __main__
parent process: 2706
process id: 2715
hello bob
"""
