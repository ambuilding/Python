import time

def c_to_f(c):
    return c*9/5 + 32

# timing
t0 = time.clock()
c_to_f(100000)
t1 = time.clock() - t0

print("t =", t0, ":", t1, "s,")

# counting
def mysum(x):
	total = 0
    for i in range(x+1):
    	total += i
return total
