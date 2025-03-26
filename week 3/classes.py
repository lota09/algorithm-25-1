class computer:
    def __init__(self,brand,cpu,memory):
        self.brand = brand
        self.cpu = cpu #GHz
        self.memory = memory #GB

    def __eq__(self, rhs):
        return self.cpu == rhs.cpu
    def __lt__(self, rhs):
        return self.cpu < rhs.cpu
    def __le__(self, rhs):
        return self.cpu <= rhs.cpu
    def __ne__(self, rhs):
        return self.cpu != rhs.cpu
    def __gt__(self, rhs):
        return self.cpu > rhs.cpu
    def __ge__(self, rhs):
        return self.cpu >= rhs.cpu

    def cpu_test(self):
        if self.memory < 2:
            print(f"{self.brand} Computer out of its memory.")
        if self.cpu <= 0:
            print(f"{self.brand} Computer is a brick.")
        else:
            elapsed_time = 1/self.cpu
            print(f"{self.brand} Computer({self.cpu}GHz) Run Program Succeed. elapsed {elapsed_time:.2f}s.")
        
    def comparecpu(self,rhs):
        if self==rhs : 
            print(f"{self.brand} Computer and {rhs.brand} Computer has Same({self.cpu}GHz) CPU Frequency.")
        elif self<rhs:
            print(f"{self.brand} Computer({self.cpu}GHz) has less CPU Frequency Then {rhs.brand} Computer({rhs.cpu}GHz).")
        elif self>rhs:
            print(f"{self.brand} Computer({self.cpu}GHz) has more CPU Frequency Then {rhs.brand} Computer({rhs.cpu}GHz).")

    def overclock(self):
        print("Overclock Unavailable without GPU")

class super_computer(computer):
    def __init__(self, brand, cpu, memory, gpu):
        super().__init__(brand, cpu, memory)
        self.gpu = gpu
        self.oc_count = 0
    
    def overclock(self):
        if self.oc_count > 1:
            print("Overclock Failed. Now your computer is a brick")
            self.cpu = 0 
            return
        self.cpu = self.cpu*1.1
        self.oc_count += 1
        print(f"Overclock({self.oc_count}) Successful. Now your computer has {self.cpu}GHz Frequency CPU")


lg_laptop = computer('LG',4.5,16)
samsung_laptop = computer('Samsung',4.5,32)
slow_computer = computer('Dell',1.2,8)
potato = computer('NOKIA',0.2,0.5)

#test cpu
"""
lg_laptop.run_program()
slow_computer.run_program()
potato.run_program()
"""
#compare cpu
"""
lg_laptop.comparecpu(samsung_laptop)
samsung_laptop.comparecpu(potato)
potato.comparecpu(slow_computer)
"""

#Test OC
"""
potato.overclock()
"""

highend_pc = super_computer('GIGABITE',4.5,32,'RTX 4080')

#test cpu (supercomputer)
"""
highend_pc.comparecpu(lg_laptop)
highend_pc.cpu_test()
highend_pc.overclock()
highend_pc.comparecpu(lg_laptop)
highend_pc.cpu_test()
highend_pc.overclock()
highend_pc.cpu_test()
highend_pc.overclock()
highend_pc.cpu_test()
"""