class car:
    def __init__(self,cc,TopSpeed):
        self.cc=cc
        self.TopSpeed=TopSpeed
    def spc(self):
        print(f'Engin CC:-{self.cc}CC')
        print(f'Top Speed;-{self.TopSpeed}Km/H')

    def brand(self):
        print('brand:-Audi')

class bike:
    def __init__(self,cc,TopSpeed):
        self.cc=cc
        self.TopSpeed=TopSpeed

    def spc(self):
        print(f'Engin CC:-{self.cc}cc')
        print(f'Top Speed;-{self.TopSpeed}Km/H')

    def brand(self):
        print('brand:-Kawasaki')


a1=bike(1000,160)
c1=car(1200,200)
a1.brand()
a1.spc()
print('\n')
c1.brand()
c1.spc()
