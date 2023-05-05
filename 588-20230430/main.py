"""
Problem - Easy
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""

class SparseArray:

    # initialize with the original large array and size
    def __init__(self, arr, size):
        self.array = {}
        self.size = size

        # initialize array
        for i in range(0, size):
            if arr[i] != 0:
                self.array[i] = arr[i]

    # updates index at i with val
    def set(self, i, val):
        self.array[i] = val 

    # gets the value at index i  
    def get(self, i):
        if i in self.array.keys():
            return self.array[i]
        else:
            return 0

    
if __name__ == '__main__':
    sample_array = [0,0,1,0,0,5,0,0,0,4,0,0,0,0,9]
    print(f'The starting array is: {sample_array}')
    new_array = SparseArray(sample_array,len(sample_array))
    print(f'At position 5 on the array we have value: {new_array.get(5)}')
    new_array.set(5, 10)
    print(f'After setting 10 as value for position 5, the get method returns {new_array.get(5)}')