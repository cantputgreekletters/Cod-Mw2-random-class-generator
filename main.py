from random import randint as rn

class main:
    def __init__(self, choice = "default"):
        self.choice = choice
        self.default = 19

        pass
    
    def GetGun(self,x):
        import AR,SMG
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
            case 11:
                gun = SMG.VEL_46()
            case 12:
                gun = SMG.MX9()
            case 13:
                gun = SMG.LACHMANN_SUB()
            case 14:
                gun = SMG.VAZNEV_9K()
            case 15:
                gun = SMG.FSS_HURRICANE()
            case 16:
                gun = SMG.MINIBAK()
            case 17:
                gun = SMG.BAS_P()
            case 18:
                gun = SMG.PDSW_528()
            case 19:
                gun = SMG.FENNEC_45()
        return gun
    
    
    def Choice(self):
        choice = self.choice
        if choice == "AR":
            return (1,10)
        if choice == "SMG":
            return (11,19)
        #Will add other if statements later on for other class types
        else:
            return (1,self.default)
        

    def start(self):
        a,b = self.Choice()
        x = rn(a,b)
        gun = self.GetGun(x)
        gun.use()

print("This is an early build, many features are missing!")
main = main()
for i in range(1,10000):
    main.start()
while True:
    input("Press enter to generate")
    main.start()