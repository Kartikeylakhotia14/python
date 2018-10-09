def make(key,value):
	x={}
	z=[]
	y=x.keys()
	if key in y:
		x[key].append(value)
	else:
		z.append(value)	
		x[key]=z
	print(x)
