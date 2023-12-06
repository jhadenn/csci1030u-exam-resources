import math

class Point3D :
    def __init__(self, x, y, z) : 
        self.x = x
        self.y = y
        self.z = z
    
    def get_distance_to(self, p2) :
        dx = self.x - p2.x
        dy = self.y - p2.y
        dz = self.z - p2.z
        distance = math.sqrt(math.pow(dx,2) + math.pow(dy,2) + math.pow(dz,2))
        
        return distance
    

if __name__ == '__main__':

    p1 = Point3D(2.0, 2.0, 4.0)

    p2 = Point3D(3.0, 1.0, 2.0)

    print(f'distance between p1 and p2: {p1.get_distance_to(p2)}')

    # output:  distance between p1 and p2: 2.449489742783178