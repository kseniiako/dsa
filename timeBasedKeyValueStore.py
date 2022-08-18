# Time-Based Key-Value Store (Leetcode 981)

class TimeMap:

    def __init__(self):
        # Initialize a dictionary to hold our time-based
        # key-value structure. At every key, we will hold 
        # consecutive inputs and corresponding timestamps
        # in an embedded dictionary: {'values': [list of values],
        # 'timestamps': [list of timestamps]}. Every new 
        # value/timestamp pair gets appended to the ends of two
        # arrays.
        self.dct = {}

    def set(self, key, value, timestamp):
        # Add an entry at a new key or update entry at existing
        # key by appending value and timestamp to corresponding 
        # arrays.
        if key not in self.dct:
            self.dct[key] = {'values': [value], 'timestamps': [timestamp]}
        else:
            self.dct[key]['values'].append(value)
            self.dct[key]['timestamps'].append(timestamp)
    
    def get(self, key, timestamp):
        # Return the latest value at given key
        # at the given timestamp

        # default result (for when value is not found)
        result = ""

        # check if the key is valid
        if key in self.dct:
            lst_timestamps = self.dct[key]['timestamps']
        else:
            return result

        # If the key is valid, we conduct binary search over
        # the array of timestamps in order to find the latest
        # value at a given timestamp. That is, in the timestamps
        # array we are searching for the largest number <= current
        # timestamp (passed as argument to function). Then we find
        # value at that timestamp in the values array.

        # Note that we can conduct binary search on the timestamps array
        # w/o preliminary sorting because problem constraints say 
        # timestamps array is strictly increasing (it is already sorted).
        left, right = 0, len(lst_timestamps)-1

        result = ""

        # binary search loop
        while left <= right:
            mid = (left + right) // 2

            if lst_timestamps[mid] == timestamp:
                return self.dct[key]['values'][mid]
            
            if lst_timestamps[mid] < timestamp:
                # save currenty largest found value
                # that could be a result (is smaller than or
                # equal to comparison timestamp)
                result = mid
                left = mid + 1

            if lst_timestamps[mid] > timestamp:
                right = mid - 1

        if result != "":
            return self.dct[key]["values"][result]
        
        return result

if __name__ == "__main__":
    myTimeMap = TimeMap()
    myTimeMap.set("foo", "bar", 1)
    print(myTimeMap.get("foo", 1))
    print(myTimeMap.get("foo", 3))
    myTimeMap.set("foo", "bar2", 4)
    print(myTimeMap.get("foo", 4))
    print(myTimeMap.get("foo", 5))


