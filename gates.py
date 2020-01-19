class Gates: 
    def NOT(a):
        if a == True:
            return False 
        else:
            return True

    def XOR(a, b):
        if a == False and b == False:
            return False
        if a == False and b == True:
            return True
        if a == True and b == False:
            return True
        else: 
            return False
    def NAND(a, b):
        if a == False and b == False:
            return True
        if a == False and b == True:
            return True 
        if a == True and b == False:
            return True 
        else:
            return False

    def AND(a, b):
        if a == True and b == True:
            return True
        else:
            return False

    def OR(a, b):
        if a == False and b == False:
            return False
        else:
            return True
    
    def NOR(a, b):
        if a == False and b == False:
            return True
        else:
            return False

class Latches(object):
    def __init__(self, s, r):
        print("SR flipflop created")
        uppernor = Gates.NOR(r, False)
        bottomnor = Gates.NOR(s, uppernor)
        self.state = Gates.NOR(r, bottomnor) 
       
