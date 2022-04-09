import matplotlib.pyplot as plt

def rng(m=2 ** 32, a=1103515245, c=12345):
    rng.current = (a * rng.current + c) % m
    return rng.current / m

rng.current = id(69)

Constems = 1000

y = []
x = []
for i in range(1, Constems+1):
    y.append(rng())

for i in range(0, Constems):
    x.append(i)

print("Random Numbers are: ",y)

#plotting graph

plt.plot(x, y)
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')

plt.title('RANDOM VALUE')
plt.show()

Constems_AI = 0
for i in range(0, 999):
    distance = (y[i] * y[i] + y[i+1] * y[i+1]) ** 0.5

    if distance < 1:
        Constems_AI += 1

pi = 4 * Constems_AI / 1000
print("Approx value of pi is",pi)