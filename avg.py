import math


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return self.__str__()


class Cluster(Point):

    def __init__(self, x, y, pointslist=None):
        super().__init__(x, y)
        if pointslist is None:
            pointslist = []
        self.pointslist = pointslist

    def __str__(self):
        return "Cluster around (" + str(self.x) + ", " + str(self.y) + ")" + " has the following points: " + ''.join(str(self.pointslist))


points = []

clusters = []

print("enter -1 as one of the coordinates to stop the inputs")

c = d = 0
index = 1
while c != -1 and d != -1:
    c = int(input("enter x coordinate of point "+ str(index) + ": "))
    if c != -1:
        d = int(input("enter y coordinate of point "+ str(index) + ": "))
    if c != -1 and d != -1:
        points.append(Point(c, d))
        index+=1

c = d = 0
index = 1
while c != -1 and d != -1:
    c = int(input("enter x coordinate of cluster's center "+ str(index) + ": "))
    if c != -1:
        d = int(input("enter y coordinate of cluster's center "+ str(index) + ": "))
    if c != -1 and d != -1:
        clusters.append(Cluster(c, d))
        index+=1


changed = True
oldpoints = []
while changed:

    newpoints = []
    changed = False

    for i in range(len(points)):
        minrange = 999999
        closest = None
        for j in range(len(clusters)):
            distance = points[i].distance(clusters[j].x, clusters[j].y)
            if minrange > distance:
                minrange = distance
                closest = clusters[j]

            elif minrange == distance and closest.x + closest.y < clusters[j].x + clusters[j].y:
                closest = clusters[j]


        closest.pointslist.append(points[i])

    for cluster in clusters:
        newpoints.append(cluster.pointslist)
        
    if len(oldpoints) == 0 or oldpoints != newpoints:
        changed = True
        for cluster in clusters:
            totalx = 0
            totaly = 0
            for point in cluster.pointslist:
                totalx += point.x
                totaly += point.y
            if len(cluster.pointslist) != 0:
                print("\ncluster's coordinates changed from ("+str(cluster.x)+", "+str(cluster.y)+") to (", end='')
                cluster.x = totalx / len(cluster.pointslist)
                cluster.y = totaly / len(cluster.pointslist)
                print(str(cluster.x)+", "+str(cluster.y)+")")
                cluster.pointslist = []
            
    for cluster in clusters:
        oldpoints.append(cluster.pointslist)

print("\nResults:")
print (clusters)
