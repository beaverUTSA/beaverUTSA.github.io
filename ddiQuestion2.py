def apply_port_exclusions(include_ports, exclude_ports):
    if include_ports == []:
        return []
    include_ports.sort()
    exclude_ports.sort()
    #print("include")
    ret_ports = []
    exclude_found = False
    x = 0
    while x < len(include_ports):
        if x > 0 and include_ports[x-1][1]+1 == include_ports[x][0]:
            include_ports[x][0] = include_ports[x-1][0]
            include_ports.pop(x-1)
            x-=1
        #print(include_ports[x])
        x += 1
    for x in include_ports:
        for y in exclude_ports:  
            if(x[0] < y[0] and x[1] > y[1]):
                exclude_found = True
                #print(x[0])
                #print(y[0]-1) 
                #print(y[1]+1)
                #print(x[1])
                ret_ports.append([x[0], (y[0]-1)])
                ret_ports.append([(y[1]+1),x[1]])
        if exclude_found == False:
            ret_ports.append(x)
    return ret_ports
print(apply_port_exclusions([[8000, 9000]],[[8080, 8080]]))
print("[[8000, 8079], [8081, 9000]] expected")
print(apply_port_exclusions([[80, 80], [22, 23], [8000, 9000]],[[1024, 1024], [8080, 8080]]))
print("[[22, 23], [80, 80], [8000, 8079], [8081, 9000]] expected")
print(apply_port_exclusions([[8000, 9000], [80, 80], [22, 23]],[[1024, 1024], [8080, 8080]]))
print("[[22, 23], [80, 80], [8000, 8079], [8081, 9000]] expected")
print(apply_port_exclusions([[1,65535]],[[1000,2000], [500, 2500]]))
print("[[1, 499], [2501, 65535]] expected")
#all thats missing here is joining included ports and removing the ones out of range
print(apply_port_exclusions([[1,1], [3, 65535], [2, 2]],[[1000, 2000], [500, 2500]]))
print("[[1, 499], [2501, 65535]] expected")
print(apply_port_exclusions([],[[8080, 8080]]))
print("[] expected")
