n = int(input())

class Queen:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def is_attacked(self, q:"Queen"):
        if q.c == self.c or q.r == self.r:
            return True
        
        for i in range(q.c-n, n-q.c):
            if i == self.c:
                return True
        
        for i in range(q.r-n, n-q.r):
            if i == self.r:
                return True
            
        return False
        
    def at_end(self):
        if self.q == n and self.r == n:
            return True
        
        return False
    
def attempt(arr:list[Queen], q:Queen):
    for Q in arr:
        if Q.is_attacked(q):
            return arr
        
    
    arr.append(q)
    return arr
        
    


def main():
    valids = set()

    