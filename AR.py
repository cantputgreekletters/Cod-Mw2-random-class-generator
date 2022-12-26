import Gun


class AR(Gun.Gun):
    def __init__(self):
        super().__init__()
        self.attatchment_name_array = ["Magazine","Ammunation","Underbarrel","Muzzle","Barrel","Laser","Optic","Stock","Rear Grip"]
        self.attatchment_array = [2,5,20,22,None,11,44,None,3]

class M4(AR):
    def __init__(self):
        super().__init__()
        self.name = "M4"
        self.attatchment_array[4] = 7
        self.attatchment_array[7] = 6
        self.attatchment_array[-1] = 5

class TAQ_56(AR):
    def __init__(self):
        super().__init__()
        self.name = "TAQ_56"
        self.attatchment_array[4] =  2
        self.attatchment_array[7] =  4

class KASTOV_762(AR):
    def __init__(self):
        super().__init__()
        self.name = "KASTOV_762"
        self.attatchment_array[4] =  5
        self.attatchment_array[7] =  6

class LACHMANN_556(AR):
    def __init__(self):
        super().__init__()
        self.name = "LACHMANN_556"
        self.attatchment_array[0] =  3
        self.attatchment_array[4] =  5
        self.attatchment_array[7] =  5

class STB_556(AR):
    def __init__(self):
        super().__init__()
        self.name = "STB_556"
        self.attatchment_array[4] =  6
        self.attatchment_array[7] = 2
        self.attatchment_name_array.append("Comb")
        self.attatchment_array.append(3)

class M16(AR):
    def __init__(self):
        super().__init__()
        self.name = "M16"
        self.magazine = 3
        self.attatchment_array[4] =  4
        self.attatchment_array[7] = 4
        self.attatchment_array[-1] = 4


class KASTOV_74U(AR):
    def __init__(self):
        super().__init__()
        self.name = "KASTOV_74U"
        self.attatchment_array[4] =  3
        self.attatchment_array[7] = 7


class KASTOV_545(AR):
    def __init__(self):
        super().__init__()
        self.name = "KASTOV_545"
        self.magazine = 3
        self.attatchment_array[4] =  4
        self.attatchment_array[7] = 6


class CHIMERA(AR):
    def __init__(self):
        super().__init__()
        self.name = "CHIMERA"
        self.attatchment_array[4] =  3
        self.attatchment_array[7] = 2


class M13B(AR):
    def __init__(self):
        super().__init__()
        self.name = "M13B"
        self.attatchment_array[4] =  2
        self.attatchment_array[7] =  3
