class TimeMap:

    def __init__(self):
        # create a dictionary based on value with key 
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value,timestamp])
        else:
            self.store[key] = [[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        # let me do a bs on it 
        arr = []
        if key in self.store:
            arr.extend(self.store[key])
        else:
            return ""
        l = 0 
        r = len(arr) - 1 
        while l <= r:
            m = l + (r-l) // 2 
            if arr[m][1] == timestamp:
                return arr[m][0]
            elif arr[m][1] > timestamp:
                r = m - 1 
            else:
                l = m + 1 
        # i know that lowest will be on that left so highest should be on the right in bs 
        return arr[r][0]

    
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)