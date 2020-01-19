import gates
import memory

memory = memory.Memory
gate = gates.Gates


s = True
reset = False 

memory.mem_bus[0] = gates.Latches(s, reset).state
print(memory.mem_bus[0])
