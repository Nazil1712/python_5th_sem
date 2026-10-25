import math
import random 

class Stats:
    def __init__(self, mean=0, stddev=1):
        self.mean = mean
        self.stddev = stddev
        self.data = []
        self.testPrivate = 10

    def calculate_mean(self):
        self.mean = sum(self.data) / len(self.data)

    def calculate_stdev(self):
        mean = self.mean
        squared_diff = [(x - mean) ** 2 for x in self.data]
        variance = sum(squared_diff) / len(self.data)
        self.stddev = math.sqrt(variance)

    def generate_data(self, start=1, end=10, count=10):
        data_list = []
        for _ in range(count):
            data_list.append(random.randint(start, end))
        self.data = data_list
        self.calculate_mean()
        self.calculate_stdev()

    def generate_normal_data(self, mean=0, stddev=1, count=10):
        self.data = [random.gauss(mean, stddev) for _ in range(count)]
        self.mean = mean
        self.stddev = stddev

    @classmethod
    def get_stats_instance(cls, mean=0, stddev=1):
        cls.temp = 20
        return cls(mean, stddev)

    @staticmethod
    def find_max(data):
        return max(data)

    @staticmethod
    def find_min(data):
        return min(data)

    def __del__(self):
        print("Last Message before deletion")

def main():
    instance = Stats(3, 5)
    print(instance.mean, "-", instance.stddev)

    instance.generate_data()
    print(instance.mean, "-", instance.stddev)

    print("Data is:", instance.data)
    del instance
    print("Max is:", Stats.find_max(instance.data))
    print("Min is:", Stats.find_min(instance.data))

if __name__ == "__main__":
    main()
