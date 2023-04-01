from time import sleep


class BlockingIntervalManager:
    def __init__(self, intervals=()):
        self.is_all_on = False
        self.intervals = list(intervals)

    def add_interval(self, interval):
        self.intervals.append(interval)

    def start_all(self):
        self.is_all_on = True
        self.__run_all()

    def __run_all(self):
        for interval in self.intervals:
            print(interval.id)
            interval.run(False)

        if self.is_all_on:
            self.__run_all()


class BlockingInterval:

    def __init__(self, func, time, params=()):
        self.id = id(self)
        self.func = func
        self.time = time
        self.params = list(params)
        self.is_on = False

    def __func_wrapper(self):
        self.func(*self.params)

    def run(self, should_auto_run=True):
        self.__func_wrapper()
        sleep(self.time)
        if should_auto_run and self.is_on:
            self.run()

    def start(self):
        self.is_on = True
        self.run()

    def stop(self):
        self.is_on = False


def func_test(num):
    print("running {num}".format(num=num))


def test():
    interval1 = BlockingInterval(func_test, 1, [1])
    interval2 = BlockingInterval(func_test, 1, [2])

    manager = BlockingIntervalManager()
    manager.add_interval(interval2)
    manager.add_interval(interval1)
    manager.start_all()
    # manager.start('')


test()
