import matplotlib.pyplot as plt


def mean():
    file = open("Sales_01_20.csv", "r")
    avg_year_amount = {"List Year": ["Sale Amount", "Count", "Mean"]}
    for row in file:
        year, amount = row.split(",")
        amount = amount.replace("\n", "")
        if year not in avg_year_amount:
            avg_year_amount[year] = [float(amount), 1, 0]
        else:
            if year != "List Year":
                avg_year_amount[year][0] += float(amount)
                avg_year_amount[year][1] += 1

    for item in avg_year_amount:
        if item != "List Year":
            avg_year_amount[item][2] = avg_year_amount[item][0] / avg_year_amount[item][1]

    return avg_year_amount


def standard_deviation(year_mean):
    file = open("Sales_01_20.csv", "r")
    standard_dev = {"List Year": ["Sample Variance", "Count", "Standard_Deviation"]}
    for row in file:
        year, amount = row.split(",")
        amount = amount.replace("\n", "")
        if year not in standard_dev:
            standard_dev[year] = [((float(amount) - year_mean[year][2]) ** 2), 1, 0]
        else:
            if year != "List Year":
                standard_dev[year][0] += ((float(amount) - year_mean[year][2]) ** 2)
                standard_dev[year][1] += 1

    for item in standard_dev:
        if item != "List Year":
            standard_dev[item][2] = (standard_dev[item][0] / (standard_dev[item][1])) ** 0.5

    return standard_dev


def year_probability(min, max, inclusive=True):
    file = open("Sales_01_20.csv", "r")
    probability = {"List Year": ["Event", "Count", "Probability"]}
    for row in file:
        year, amount = row.split(",")
        amount = amount.replace("\n", "")
        if inclusive == True:
            if year not in probability:
                if min <= float(amount) <= max:
                    probability[year] = [1, 1, 0]
                else:
                    probability[year] = [0, 1, 0]
            else:
                if year != "List Year":
                    if min <= float(amount) <= max:
                        probability[year][0] += 1
                        probability[year][1] += 1
                    else:
                        probability[year][1] += 1
        else:
            if year not in probability:
                if min < float(amount) < max:
                    probability[year] = [1, 1, 0]
                else:
                    probability[year] = [0, 1, 0]
            else:
                if year != "List Year":
                    if min < float(amount) < max:
                        probability[year][0] += 1
                        probability[year][1] += 1
                    else:
                        probability[year][1] += 1

    for item in probability:
        if item != "List Year":
            probability[item][2] = probability[item][0] / probability[item][1]

    return probability


the_mean = mean()
the_standard_deviation = standard_deviation(the_mean)
mini = 200_000
maxi = 300_000
the_probability = year_probability(mini, maxi, inclusive=True)

print(the_mean)
print(the_standard_deviation)
print(the_probability)

included_year = []
included_mean = []
included_sd = []
included_prob = []
for year in the_mean:
    if year != "List Year":
        if year not in included_year:
            included_year.append(year)

sorted_year = sorted(included_year)

for year in sorted_year:
    included_mean.append(the_mean[year][2])
    included_sd.append(the_standard_deviation[year][2])
    included_prob.append(the_probability[year][2])

plt.bar(sorted_year, included_mean)
plt.title("Mean Sales Per Year")
plt.xlabel("List Year")
plt.ylabel("Sales Average")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()

plt.bar(sorted_year, included_sd)
plt.title("Standard Deviation of Sales Per Year")
plt.xlabel("List Year")
plt.ylabel("Sales Standard Deviation")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()

plt.bar(sorted_year, included_prob)
plt.title("Probability of Range of Sales Per Year")
plt.xlabel("List Year")
plt.ylabel("Sales Probability")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()
plt.show()

