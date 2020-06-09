class Aviacompany:
    def __init__(self):
        self.money = 0
        self.consumption = dict()
        self.KM_dict = dict()
        self.suml = 0
        self.sumv = 0

    def kypitplains(self, Plane_I):
        self.money += Plane_I.money
        self.consumption.update({int(Plane_I.roshodtopleva): str(Plane_I.name)})
        self.KM_dict.update({int(Plane_I.path): str(Plane_I.name)})
        self.suml += Plane_I.maxludei
        self.sumv += Plane_I.maxves

    def VsvesitReshenie(self):
        print("Прибуток авіакомпанії " + str(self.money) + " $")
        print("Загальну місткість авіакомпанії " + str(self.suml))
        print("Загальну вантажопідйомність авіакомпанії " + str(self.sumv))
        print("Cортування літаків авіакомпанії за дальністю польоту")
        min = 0
        max = 8
        for i in self.KM_dict:
            print(str(i) + ' тис. км ' + str(self.KM_dict[i]))
        for i in range(min, max):
            for j in self.KM_dict:
                if i == j:
                    print(self.KM_dict[i] + " Задовольняє діапазон")





class Plains:
    def __init__(self, maxludei, maxves, roshodtopleva, bak):
        pass


class Plain1(Plains):
    def __init__(self, maxludei, maxves, roshodtopleva, bak):
        super().__init__(maxludei, maxves, roshodtopleva, bak)
        self.maxludei = maxludei
        self.maxves = maxves
        self.roshodtopleva = roshodtopleva
        self.bak = bak
        self.name = "Plane_1"
        self.money = 500000
        self.path = self.bak / self.roshodtopleva


class Plain2(Plains):
    def __init__(self, maxludei, maxves, roshodtopleva, bak):
        super().__init__(maxludei, maxves, roshodtopleva, bak)
        self.maxludei = maxludei
        self.maxves = maxves
        self.roshodtopleva = roshodtopleva
        self.bak = bak
        self.name = "Plane_2"
        self.money = 500000
        self.path = self.bak / self.roshodtopleva


class Plain3(Plains):
    def __init__(self, maxludei, maxves, roshodtopleva, bak):
        super().__init__(maxludei, maxves, roshodtopleva, bak)
        self.maxludei = maxludei
        self.maxves = maxves
        self.roshodtopleva = roshodtopleva
        self.bak = bak
        self.name = "Plane_3"
        self.money = 750000
        self.path = self.bak / self.roshodtopleva

class Plain4(Plains):
    def __init__(self, maxludei, maxves, roshodtopleva, bak):
        super().__init__(maxludei, maxves, roshodtopleva, bak)
        self.maxludei = maxludei
        self.maxves = maxves
        self.roshodtopleva = roshodtopleva
        self.bak = bak
        self.name = "Plane_4"
        self.money = 1000000
        self.path = self.bak / self.roshodtopleva

class Main:
    Company = Aviacompany()

    A1 = Plain1(432, 500, 50, 800)
    A2 = Plain2(684, 380, 25, 600)
    A3 = Plain3(288, 640, 75, 1000)
    A4 = Plain4(410, 890, 100, 750)

    Company.kypitplains(A1)
    Company.kypitplains(A2)
    Company.kypitplains(A3)
    Company.kypitplains(A4)

    Company.VsvesitReshenie()

