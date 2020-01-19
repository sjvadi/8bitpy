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

class NANDFF(object):
    def __init__(self, action):
        #these are default values
        self.q = False
        self.nq = True
        if action == "set":
            self.q = Gates.NOR(Gates.NOR(True, self.q), False)
            self.nq = Gates.NOR(True, self.q)
        if action == "reset":
            self.q = Gates.NOR(True, Gates.NOR(False, self.q))
            self.nq = Gates.NOR(False, self.q)
