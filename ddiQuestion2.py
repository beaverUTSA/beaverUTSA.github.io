def apply_port_exclusions(include_ports, exclude_ports):
    if include_ports == []:
        return []
    include_ports.sort()
    exclude_ports.sort()
    ret_ports = []
    exclude_found = False
    x = 0
    while x < len(include_ports):
        if x > 0 and include_ports[x-1][1]+1 == include_ports[x][0]:
            include_ports[x][0] = include_ports[x-1][0]
            include_ports.pop(x-1)
            x-=1
        x += 1
    index = 0
    while index < len(exclude_ports):
        if index > 0 and (exclude_ports[index-1][0] < exclude_ports[index][0]) and (exclude_ports[index-1][1] > exclude_ports[index][1]):
            exclude_ports[index][0] = exclude_ports[index-1][0]
            exclude_ports[index][1] = exclude_ports[index-1][1]
            exclude_ports.pop(index-1)
        index += 1
    for x in include_ports:
        for y in exclude_ports:  
            if(x[0] < y[0] and x[1] > y[1]):
                exclude_found = True
                ret_ports.append([x[0], (y[0]-1)])
                ret_ports.append([(y[1]+1),x[1]])
        if exclude_found == False:
            ret_ports.append(x)
    return ret_ports
