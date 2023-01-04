class Number:
    def checkEvenOdd(self):
        if self.n%2==0:
            return "Even"
        else:
            return "Odd"
    def sumofDigits(self):
        temp=str(self.n)
        t=0
        for i in temp:
            t +=int(i)
        return t
            
    def __init__(self,n):
        self.n=n
    def Factorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n+1):
            res *=1
        return res
    def Armstrong(self):
        str1=str(self.n)
        total=0
        
        for i in str1:
            total +=int(i)**len(str1)
        if inp==total:
            return 1
        else:
            return 0
    def Prime(self):
        assert self.n>=1,'INVALID'
        if self.n==1 or self.n==2 or self.n==3:
            for i in range(2,self.n):
                if self.n%i==0:
                    return "not a prime"
            return "prime"
        

inp=int(input())
obj=Number(inp)
print(inp,"is",obj.checkEvenOdd())
print('sum of digits of',inp,'is',obj.sumofDigits())
print('Factorial of',inp,'is',obj.Factorial())
print('Armstrong of',inp,'is',obj.Armstrong())
print('prime number',inp,'is',obj.Prime())
