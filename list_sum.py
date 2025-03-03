class ListSum:
    def __init__(self, data):
        self.data = data

    def sum_list_entries(self):
        total = 0
        for number in self.data:
            total+=number
        return total
    
user_input = input ('Please enter a list of numbers separated by commas. Hit enter to confirm the list: ')

data = [float(num.strip()) for num in user_input.split(',')]
sum_data = ListSum(data)
print(f'The sum of numbers provided is: {sum_data.sum_list_entries()}')
