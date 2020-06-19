import matplotlib.pyplot as plt
import csv

file_name_1 = "Cost"
file_name_2 = "Time"

file_list_1 = []
file_list_2 = []
for i in range(2):
    if i == 0:
        file_name = file_name_1
        file_list = file_list_1
    else:
        file_name= file_name_2
        file_list = file_list_2

    with open(f'..\\..\\{file_name}.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for count, data in enumerate(csv_reader):
            if count == 0:
                continue
            file_list.append(int(float(data[0])))

a = []
b = []
c = []
d = []

print(len(file_list_1), len(file_list_2))
for i in range(len(file_list)):
    if file_list_1[i] > 10000:
        a.append(file_list_1[i])
        b.append(file_list_2[i])
    else:
        c.append(file_list_1[i])
        d.append(file_list_2[i])

plt.plot(a, b, "ro", label= "Avoid crosses")
plt.plot(c, d, "bo", label = "Crosses" )
plt.title("Low time versus Low cost")
plt.legend()
plt.xlabel("time(m)")
plt.ylabel("cost")
plt.show()