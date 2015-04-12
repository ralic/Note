import multiprocessing
import time


class MyFancyClass(object):
    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print "Doing something fancy in %s for %s" % (proc_name, self.name)


def worker(q):
    obj = q.get()
    obj.do_something()


class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        super(Consumer, self).__init__()
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                print '%s Exiting' % proc_name
                self.task_queue.task_done()
                break
            print "%s: %s" % (proc_name, next_task)
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)
        return

class Task(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        time.sleep(0.1)
        return '%s * %s = %s' % (self.a, self.b, self.a * self.b)


if __name__ == '__main__':
    # queue = multiprocessing.Queue()
    # p = multiprocessing.Process(target=worker, args=(queue, ))
    # p.start()
    #
    # queue.put(MyFancyClass("Fancy Dan"))
    #
    # queue.close()
    # queue.join_thread()
    # p.join()
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    num_consumers = multiprocessing.cpu_count()
    consumers = [Consumer(tasks, results) for i in xrange(num_consumers)]
    for w in consumers:
        w.start()

    num_jobs = 10
    for i in xrange(num_jobs):
        tasks.put(Task(i, i))
    for i in xrange(num_consumers):
        tasks.put(None)
    tasks.join()
    print results.qsize()
    while num_jobs:
        result = results.get()
        print "Result:", result
        num_jobs -= 1
