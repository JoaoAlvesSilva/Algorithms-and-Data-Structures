// https://leetcode.com/problems/lru-cache

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.keys=[] #order keys, from oldest to newest
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity:
            self.cache[key] = value
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            
        else:
            if key in self.cache:
                self.cache[key] = value
                self.keys.remove(key)
                self.keys.append(key)
            else:
                to_erase = self.keys.pop(0)
                self.cache.pop(to_erase)
                self.keys.append(key)
                self.cache[key] = value
                   
        