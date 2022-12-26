import AR
from random import randint as rn

class main:
    def __init__(self):
        self.Number_Of_AR = 10
        pass
    
    def GetGun(self,x):
        match x:
            case 1:
                gun = AR.M4()
            case 2:
                gun = AR.TAQ_56()
            case 3:
                gun = AR.KASTOV_762()
            case 4:
                gun = AR.LACHMANN_556()
            case 5:
                gun = AR.STB_556()
            case 6:
                gun = AR.M16()
            case 7:
                gun = AR.KASTOV_74U()
            case 8:
                gun = AR.KASTOV_545()
            case 9:
                gun = AR.CHIMERA()
            case 10:
                gun = AR.M13B()
        return gun
    def start(self):
        x = rn(1,self.Number_Of_AR)
        gun = self.GetGun(x)
        gun.use()

print("This is an early build, many features are missing!")
main = main()
while True:
    input("Press enter to generate")
    main.start()