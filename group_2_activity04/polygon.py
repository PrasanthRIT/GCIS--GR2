class Polygon:
    
    #Step 1

    #Intialize Object
    def __init__(self,name,sides):
        self.name=name
        self.sides=sides
  
    #Get Name of polygon
    def get_name(self):
        return self.name
    
    #Set Sides for Polygon Object
    def set_name(self,name):
        self.name=name
    
    #Get Sides of polygon
    def get_sides(self):
        return self.sides
    
    #Set Sides for polygon
    def set_sides(self,sides):
        self.sides=sides
    #Step2
    def __eq__(self,other):
        if self.name==other.name and self.sides==other.sides:
            return True
        else:
            return False
    
    def __ne__(self,other):
        if self.__eq__(other):
            return False
        else:
            return True
        
    #Step 3
    def __str__(self):
        return f"{self.name} with sides:{self.sides}"
    
    #Step 4
    def calc_circumference(self):
        Sum=0
        for i in self.sides:
            Sum += i
        return Sum
    
#Step 5
def main():
    Polygon1=Polygon("triangle",[3.5,6.7,5])
    Polygon2=Polygon("square",[4,4,4,4])
    Polygon3=Polygon("hexagon",[6,5.4,2,6,1,5])

    print(Polygon1)
    print(Polygon2)
    print(Polygon3)

    print(f"{Polygon1.name} Circumference: {Polygon1.calc_circumference()}")
    print(f"{Polygon2.name} Circumference: {Polygon2.calc_circumference()}")
    print(f"{Polygon3.name} Circumference: {Polygon3.calc_circumference()}")

if __name__=="__main__":
    main()