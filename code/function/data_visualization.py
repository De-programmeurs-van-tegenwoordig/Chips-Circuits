import matplotlib.pyplot as plt
import statistics
import csv

file_name = "Greedy_Astar"
data = open(f'..\\..\\{file_name}.csv')

plt.style.use('ggplot')

a = []
b = []
c = []
d = []
e = []
f = []
# g = []
# h = []

reader = csv.reader(data)
count = 0
for Algorithm, time, cost in (reader):
    if count > 0:    
        if Algorithm == "Greedy":
            print("0")
            a.append(int(float(time)))
            b.append(int(cost))
        elif Algorithm == "Astar_avoid_crosses":
            print("1")
            c.append(int(float(time)))
            d.append(int(cost))
        elif Algorithm == "Astar_does_not_avoid_crosses":
            print("2")
            e.append(int(float(time)))
            f.append(int(cost))
        # else:
        #     g.append(int(float(time)))
        #     h.append(int(cost))
    count += 1

plt.bar("A star(Crosses)", statistics.mean(f), label = "Crosses")
plt.bar("A star(Avoid crosses)", statistics.mean(d), label = "Avoid crosses")
plt.bar("Greedy", statistics.mean(b), label= "Greedy")
# plt.bar("Random", statistics.mean(h), label= "Random")
plt.xlabel("Algorithm")
plt.ylabel("Cost")
plt.show()

plt.bar("A star(Cross)", statistics.mean(e), label = "Crosses")
plt.bar("A star(Avoid Crosses)", statistics.mean(c), label = "Avoid crosses")
plt.bar("Greedy", statistics.mean(a), label= "Greedy")
# plt.bar("Random", statistics.mean(g), label = "Random")

plt.title("Low time versus Low cost")
plt.xlabel("Algorithm")
plt.ylabel("Time")
plt.show()

plt.plot(a, b,".",  color = "green", label= "Greedy")
plt.plot(c, d,".", color = "blue", label = "Astar (avoid crosses)")
plt.plot(e, f, ".",  color = "orange", label = "Astar (Crosses)")
# plt.plot(g, h, ".", color = "red", label = "Random")
plt.xlabel("time")
plt.ylabel("cost")
plt.legend()

plt.show()