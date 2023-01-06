import Gun

class SMG(Gun.Gun):
    def __init__(self):
        super().__init__()
        self.attatchment_name_array = ["Muzzle", "Underbarrel", "Ammunition", "Laser", "Optic","Rear_Grip"]
        self.attatchment_array = [19,26,4,11,34,3]


class VEL_46(SMG):
    def __init__(self):
        super().__init__()
        self.name = "VEL 46"
        self.attatchment_name_array.append("Magazine")
        self.attatchment_array.append(3)
        self.attatchment_name_array.append("Barrel")
        self.attatchment_array.append(7)
        self.attatchment_name_array.append("Stock")
        self.attatchment_array.append(4)

class MX9(SMG):
    def __init__(self):
        super().__init__()
        self.name = "MX9"
        self.attatchment_name_array.append("Magazine")
        self.attatchment_array.append(1)
        self.attatchment_name_array.append("Barrel")
        self.attatchment_array.append(3)
        self.attatchment_name_array.append("Stock")
        self.attatchment_array.append(2)
        self.attatchment_name_array.append("Comb")
        self.attatchment_array.append(3)

class LACHMANN_SUB(SMG):
    def __init__(self):
        super().__init__()
        self.name = "LACHMANN SUB"
        self.attatchment_name_array = ["Muzzle", "Underbarrel", "Ammunition", "Laser", "Optic","Rear_Grip","Magazine","Barrel","Stock"]
        self.attatchment_array = [19,26,4,11,34,2,3,3,4]


class VAZNEV_9K(SMG):
    def __init__(self):
        super().__init__()
        self.name = "VAZNEV 9K"
        self.attatchment_name_array.append("Magazine")
        self.attatchment_array.append(1)
        self.attatchment_name_array.append("Barrel")
        self.attatchment_array.append(2)
        self.attatchment_name_array.append("Stock")
        self.attatchment_array.append(5)

class FSS_HURRICANE(SMG):
    def __init__(self):
        super().__init__()
        self.name = "FSS-HURRICANE"
        self.attatchment_name_array = ["Muzzle", "Underbarrel", "Ammunition", "Laser", "Optic","Rear_Grip","Barrel","Stock"]
        self.attatchment_array = [19,26,4,11,34,4,2,5]

class MINIBAK(SMG):
    def __init__(self):
        super().__init__()
        self.name = "MINIBAK"
        self.attatchment_name_array.append("Magazine")
        self.attatchment_array.append(1)
        self.attatchment_name_array.append("Barrel")
        self.attatchment_array.append(1)
        self.attatchment_name_array.append("Stock")
        self.attatchment_array.append(5)


class BAS_P(SMG):
    def __init__(self):
        super().__init__()
        self.name = "BAS-P"
        self.attatchment_name_array.append("Magazine")
        self.attatchment_array.append(2)
        self.attatchment_name_array.append("Barrel")
        self.attatchment_array.append(4)
        self.attatchment_name_array.append("Stock")
        self.attatchment_array.append(3)

class PDSW_528(SMG):
    def __init__(self):
        super().__init__()
        self.name = "PDSW 528"
        self.attatchment_name_array.append("Rail")
        self.attatchment_array.append(2)
        self.attatchment_name_array.append("Barrel")
        self.attatchment_array.append(6)
        self.attatchment_name_array.append("Stock")
        self.attatchment_array.append(4)
        self.attatchment_name_array.append("Comb")
        self.attatchment_array.append(3)
    
    def PickAttatchments(self,n):
        from random import randint as rn
        a = len(self.attatchment_name_array) - 1
        array = []
        attatchment_list = []
        for _ in range(n):
            while True:
                x = rn(0,a)
                if self.Check(x,array,attatchment_list):
                    break
            array.append(x)
            number = rn(1,self.attatchment_array[x])
            picked = ("{attatchment} = {number}".format(attatchment=self.attatchment_name_array[x], number = number))
            attatchment_list.append(picked)
        
        return attatchment_list
    
    
    def Check(self,x,array,attatchment_list):
        return x not in array and self.BarrelCheck(array,attatchment_list,x) and self.RailCheck(array,attatchment_list,x)
    
    def BarrelCheck(self,array,attatchment_list,x):
        #pos = 1 Underbarrel pos = 7 barrel
        if x == 1 and 7 in array:
           #Check if correct barrel is in so that and underbarrel can be used
           for i in range(3,7):
                if "Barrel = {i}".format(i=i) in attatchment_list:
                    return True
           return False
            
        elif x == 1 and 7 not in array:
            return False
        return True
    
    def RailCheck(self,array,attatchment_list,x):
        # 6 = rail 4 = optic
        if x != 6 and x != 4: return True
        else:
            #Should be more complicated but its not possible with how the function
            #"PickAttatchments" is made
            if x == 6:
                return 4 in array
            elif x == 4:
                if 6 not in array: return True
                else:
                    return "Rail = 2" in attatchment_list
    
class FENNEC_45(SMG):
    def __init__(self):
        super().__init__()
        self.name = "FENNEC 45"
        self.attatchment_name_array.append("Magazine")
        self.attatchment_array.append(2)
        self.attatchment_name_array.append("Barrel")
        self.attatchment_array.append(5)
        self.attatchment_name_array.append("Stock")
        self.attatchment_array.append(5)

