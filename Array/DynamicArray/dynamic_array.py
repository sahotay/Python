#!/usr/local/bin/python3
import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    def __len__(self):
        return self.n
    def __getitem__(self,k):
        if not 0 <= k < self.n:
            return IndexError("K is out of bounds!")
        return self.A[k]
    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = ele
        self.n += 1
    def _resize(self,new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap
    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()

# class constructor 
arr = DynamicArray()

#calling append
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))

print(arr[1])