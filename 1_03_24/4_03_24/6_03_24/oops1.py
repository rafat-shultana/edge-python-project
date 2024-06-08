class computer:
    def _init_(self, cpu, ram):
      self.cpu = cpu
      self.ram = ram
    def confing(self):
       print('Configuration:', self.cpu, self.ram)
       
comp2 = computer('Ryzen' , 8) 

computer.confing(comp2)
