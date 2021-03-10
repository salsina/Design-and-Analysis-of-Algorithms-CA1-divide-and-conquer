import math

class node:
    def __init__(self,_x,_y,i,_angle,_time):
        self.x = _x
        self.y = _y
        self.index = i
        self.angle = _angle
        self.time = _time
    def __repr__(self):
        return str(self.time)
        
def make_tree(nodes,k,i):
    if len(nodes) == 0:
        return
    if k == 0:
        root_index = find_root_index(nodes)
        root_node = nodes[root_index]
        root_node.time = i
        return
    
    root_index = find_root_index(nodes)
    root_node = nodes[root_index]
    root_node.time = i
    nodes.pop(root_index)
    set_angles(nodes,root_node)
    nodes.sort(key = lambda x:x.angle)
    k-=1
    
    make_tree(nodes[:len(nodes)//2],k,2*i)
    make_tree(nodes[len(nodes)//2:],k,2*i+1)

    nodes.append(root_node)
    
def find_root_index(nodes):
    lowest_node_index = 0
    max = nodes[0].y
    for i in range(len(nodes)):
        if nodes[i].y > max:
            max = nodes[i].y
            lowest_node_index = i
    return lowest_node_index

def set_angles(nodes,root_node):
    root_coordinates = [root_node.x,root_node.y]
    for i in range(len(nodes)):
        coordinates = [nodes[i].x,nodes[i].y]
        nodes[i].angle = find_angle(root_coordinates,coordinates)

def find_angle(first_c,second_c):
    if second_c[1] == first_c[1]:
        return 0
    if second_c[0]==first_c[0]:
        return 90
    angle = math.degrees(math.atan((first_c[1]-second_c[1])/(first_c[0] - second_c[0])))
    if angle < 0:
        angle +=180
    return angle

n,k = [int(x) for x in input().split()]
nodes = []
for i in range(n):
    x , y = [int(x) for x in input().split()]
    new_node = node(x,y,i,0,0)
    nodes.append(new_node)
    
make_tree(nodes,k,1)
nodes.sort(key = lambda x:x.index)
for i in nodes:
    print(i)