class Bus:

    def __new__(cls, *args, **kwargs):
        return super('Bus', cls).__new__()

    def __init__(self):
        self.bus_num = None
        self.title=None
        self.end_point = None
        self.start_point = None
        self.direction = None
        self.time_table = None
        pass

    def set_bus_num(self):
        pass


if __name__ == '__main__':
    print("A")