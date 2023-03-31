from time import sleep


# def set_blocking_interval(func, sec, max=0, params=[],  runs=1):
#     def func_wrapper():

#     func_wrapper()


class BlockingInterval:
    is_on = False

    def __init__(self, func, time, params=[]):
        self.func = func
        self.time = time
        self.params = params

    def __func_wrapper(self):
        self.func(*self.params)

    def __run(self):
        self.__func_wrapper()
        sleep(self.time)
        if self.is_on:
            self.__run()

    def start(self):
        self.is_on = True
        self.__run()

    def stop(self):
        self.is_on = False
