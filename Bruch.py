class bruch():
    
    def __init__(self,z,n=1):     
        self.z=int(z)
        self.n=int(n)
        self.__reduce()
        
    def __reduce(self):
        a=self.z
        b=self.n
        while a!=b and a!=1 and b!=1:
            a,b=min(a,b), abs(a-b)
        if a==b:
            self.z=self.z//a
            self.n=self.n//a
            
    def __mul__(self,other):
        return bruch(self.z*other.z,self.n*other.n)
    
    def __str__(self) :
        return str(self.z)+'/'+str(self.n)
    
x=bruch(21,15)
y=bruch(2,7)
print(x)
print(y)
print(x*y)

