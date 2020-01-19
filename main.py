import gates
import memory

memory = memory.Memory
gate = gates.Gates

memory.mem_bus[0] = gates.NANDFF("set").q
print(memory.mem_bus[0])
memory.mem_bus[0] = gates.NANDFF("reset").q
print(memory.mem_bus[0])
