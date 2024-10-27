class RandomizedSet:

    def __init__(self):
        # Initialize an empty dictionary to store values and their indices
        self.value_to_index = {}
        # Initialize an empty list to store values
        self.values = []

    def insert(self, val: int) -> bool:
        # If the value is already in the set, return False
        if val in self.value_to_index:
            return False
        
        # Add the value to the end of the list
        self.values.append(val)
        # Store the index of the value in the dictionary
        self.value_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        # If the value is not in the set, return False
        if val not in self.value_to_index:
            return False
        
        # Get the index of the value to be removed
        index = self.value_to_index[val]
        last_val = self.values[-1]
        
        # Move the last element to the position of the removed element
        self.values[index] = last_val
        self.value_to_index[last_val] = index
        
        # Remove the last element
        self.values.pop()
        del self.value_to_index[val]
        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()