import math
import random 

class Stats:

    temp = 0
    def __init__(self, mean = 0, stddev = 1):
        self.mean = mean
        self.stddev = stddev
        self.data = []
        self.testPrivate = 10


    def calculate_mean(self):
        self.mean = sum(self.data)/len(self.data) 
                

    def calculate_stdev(self):
        mean = self.mean
        squared_diff = [(x-mean)**2 for x in self.data]
        self.stddev = math.sqrt(sum(squared_diff)/len(self.data))

    def generate_data(self, start=1, end = 10, count = 10):
        data_list = []
        for i in range(count):
            data_list.append(random.randint(start, end))

        self.data = data_list
        self.calculate_mean()
        self.calculate_stdev()


    def generate_normal_data(self, start=1, end = 10, count = 10):
        data_list = [random.gauss(start,end) for i in range(count)]
        self.data = data_list
        self.calculate_mean()
        self.calculate_stdev()


    @classmethod
    def get_stats_instance(cls, mean = 0, stddev = 1):
        cls.temp = 20
        return cls(mean, stddev)

    @staticmethod
    def find_max(data):
        Stats.temp=30
        return max(data)
        
    def __del__(self):
        print("Last Message before deletion")

    def find_min(data):
        return min(data)


def main():
	print("Something")
	
	instance = Stats(3,5) 	  # Create instance of Stats
	print(type(instance)) # Check type of instance
	
	print(instance.mean,"-", instance.stddev) #Accessing data of instance
        
	print(vars(instance))

	instance.generate_data() # Accessing instance methods  
	print(instance.mean,"-", instance.stddev) #Accessing data of instance

	print(instance.temp)
	new_instance = Stats.get_stats_instance(4,2)
	print(type(new_instance), new_instance.__class__)
	print(new_instance.temp, new_instance.mean)
	print("Data is: ",instance.data)  # Print Data
        

	

if __name__ == "__main__":
	main()