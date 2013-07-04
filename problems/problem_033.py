def cancel_fractions():
	for y in range(1,10):
	    for z in range(y,10):
	        x=float(9)*y*z/(10*y-z)
	        if int(x) == x and y/z < 1 and x<10:
	            return x, y, z, str(10*y+x)+'/'+str(z+10*x), str(y)+'/'+str(z)
