class Polygon:

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