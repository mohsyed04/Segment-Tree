#implementation based on: https://bitbucket.org/StableSort/play/src/master/src/com/stablesort/segtree/SegmentTreeMax.java

class SegmentTree:
    def __init__(self, arr):
      self.arr = arr
      self.n = len(arr)
      self.tree = [0]*2*n
      self.createSegmentTree()
    
    def createSegmentTree():
        for i in range(self.n):
            self.tree[i+n] = self.arr[i]
        for j in range(self.n-1, 0, -1):
            self.tree[j] = self.tree[2 * j] ^ self.tree[2 * j + 1]
            
    def xor(self, frm, to): #return's xor of a range. frm: inclusive, to:exclusive
        frm += self.n
        to += self.n
        value = 0
        while(frm < to):
            if(frm & 1 == 1):
                value ^= self.tree[frm]
                frm += 1
            if(to & 1 == 1):
                to -= 1
                value ^= self.tree[to]
            frm >>= 1
            to >>= 1
        return value
               
    def xorQueries(self, start, end):        
        return self.xor(start, end) #end+1 if the input is inclusive
