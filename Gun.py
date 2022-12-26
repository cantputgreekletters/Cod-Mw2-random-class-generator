from random import randint as rn

class Gun:
    def __init__(self):
        self.name = None
        self.attatchment_name_array = None
        self.attatchment_array = None
        
    
    def PickAttatchments(self,n):
        a = len(self.attatchment_name_array) - 1
        array = []
        attatchment_list = []
        for _ in range(n):
            while True:
                x = rn(0,a)
                if x not in array:
                    break
            array.append(x)
            number = rn(1,self.attatchment_array[x])
            picked = ("{attatchment} = {number}".format(attatchment=self.attatchment_name_array[x], number = number))
            attatchment_list.append(picked)

        return attatchment_list
    


    def GetAttatchment(self,name,x):
        return(name, rn(1,x))



    def use(self):
        print("Gun = {name}".format(name=self.name))
        print (self.PickAttatchments(rn(1,5)))
        pass
        