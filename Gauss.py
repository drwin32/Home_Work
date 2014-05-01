class Gauss(object):

    A = None
    B = None
    
    def __init__(self, n):
        self.A = [[1.0 / j for j in xrange(i,n+i)] for i in xrange(1,n+1)]
        self.B = [sum(row) for row in self.A]

    def __repr__(self):
        return "A:" +self.A.__str__()+"\nB:"+self.B.__str__()
        
    def solve(self):       
        n = len(self.A)
        for i in xrange(0, n-1):
            for m in xrange(i+1, n):
                c = self.A[m][i]/self.A[i][i]
                self.B[m]-=c*self.B[i]
                for j in xrange(i, n):
                    self.A[m][j]-=c*self.A[i][j]
                                                     
        x = [0]*n
        x[n-1]=self.B[n-1]/self.A[n-1][n-1]        
        for i in xrange(n-2,-1,-1):
            s = 0
            for k in xrange(i+1, n):
                s += self.A[i][k]*x[k]
            x[i]=(self.B[i]-s)/self.A[i][i] 
        return x

print "n="
n = int(raw_input())
obj = Gauss(n)
print obj
print "X:", obj.solve()
    
