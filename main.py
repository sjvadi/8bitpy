import gates

gate = gates.gates

a = True
b = False

c = gate.XOR(gate.OR(a,b),gate.NAND(a,b))

print(c)
