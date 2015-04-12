import multiprocessing
import time


def worker():
    p = multiprocessing.current_process()
    print p.name, "Starting...", p.pid
    time.sleep(3)
    print p.name, "Exiting..."


def my_service():
    p = multiprocessing.current_process()
    print p.name, "Starting...", p.pid
    time.sleep(3)
    print p.name, "Exiting..."


if __name__ == '__main__':
    service = multiprocessing.Process(name="service", target=my_service)
    worker1 = multiprocessing.Process(name="worker1", target=worker)
    worker2 = multiprocessing.Process(name="worker2", target=worker)
    worker1.start()
    worker2.start()
    service.start()