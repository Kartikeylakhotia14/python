y=[{0,1},{1,2},{3,4}]
for i in y:
    for j in y:
        if i&j!=set() and i!=j:
            y.append(i|j)
            y.remove(i)
            y.remove(j)
for k in y:
    print("Network"+str(k))
                
