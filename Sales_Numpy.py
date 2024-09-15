import matplotlib.pyplot as plt
import numpy as np

all_sales = np.loadtxt("Sales_01_20.csv", delimiter=",", skiprows=1)
index_year = all_sales[:, 0].argsort()
all_sales = all_sales[index_year]

earning = []
section = [all_sales[0][1], all_sales[1][1]]

unique_years = [str(int(all_sales[0][0]))]

for i in range(2, len(all_sales)):
    if all_sales[i - 1][0] == all_sales[i][0]:
        section.append(all_sales[i][1])
    else:
        np_arr = np.array(section)
        earning.append(np_arr)
        unique_years.append(str(int(all_sales[i][0])))
        section = [all_sales[i][1]]
np_arr = np.array(section)
earning.append(np_arr)

the_mean = []
the_sd = []
the_prob = []
for item in earning:
    the_mean.append(item.mean())
    the_sd.append(item.std())

for i in range(len(earning)):
    total = len(earning[i])
    event = 0
    for j in range(total):
        if 200_000 <= earning[i][j] <= 300_000:
            event += 1
    the_prob.append(event / total)

plt.bar(unique_years, the_mean)
plt.title("Mean Sales Per Year")
plt.xlabel("List Year")
plt.ylabel("Sales Average")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()

plt.bar(unique_years, the_sd)
plt.title("Standard Deviation of Sales Per Year")
plt.xlabel("List Year")
plt.ylabel("Sales Standard Deviation")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()

plt.bar(unique_years, the_prob)
plt.title("Probability of Goal Sales Per Year")
plt.xlabel("List Year")
plt.ylabel("Sales Probability")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()
