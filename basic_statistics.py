from collections import Counter

class CentralTendency:
    def __init__(self, data):
        self.data = data

    def calculate_mean (self):

        if not self.data:
            return None
        
        total = 0
        for num in self.data:
            total += num
        return total/len(self.data)
    
    def calculate_median(self):
        if not self.data:
            return None
        sorted_data = sorted(self.data)
        n=len(sorted_data)
        mid = n//2
        if n%2==0: #the data list has an even number of points
            return (sorted_data[mid-1]+sorted_data[mid])/2
        else:
            return sorted_data[mid]

    def calculate_mode(self):
        if not self.data:
            return None
        count = Counter(self.data)
        max_count = max(count.values())  # Get the highest frequency
        modes = [k for k, v in count.items() if v == max_count]  # Get all modes
        return modes if len(modes) > 1 else modes[0]  # Return single value if only one mode