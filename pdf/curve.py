diffs = 1
curven = 1
curve = []
import matplotlib.pyplot as plt
while diffs < 100: 
	diffs = diffs + 1
	curven = curven * -0.95
	curve.append(curven)
#plt.plot(times, heights, '.', label='measurements')
plt.plot(curve, diffs, 'x', label='simulation')
plt.xlabel('Time (Seconds)')
plt.ylabel('Height (Meters)')
plt.grid(True)
plt.legend()
plt.savefig('test.pdf')

