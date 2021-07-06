import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/sdcard/Python/KNN/Datasets/Iris.csv")

data_dict = data.to_dict()
class_names = data_dict["class"]
lst = []
for j in range(150):
	if class_names[j] not in lst:
		lst.append(class_names[j])

#Iris-setosa
#Iris-versicolor
#Iris-virginica

lst_1 = []
lst_2 = []
lst_3 = []
lst_4 = []
lst_5 = []
lst_6 = []

for i in data_dict["class"]:
	if data_dict["class"][i] == lst[0]:
		lst_1.append(data_dict["sepallength"][i])
		lst_2.append(data_dict["petallength"][i])
	elif data_dict["class"][i] == lst[1]:
		lst_3.append(data_dict["sepallength"][i])
		lst_4.append(data_dict["petallength"][i])
	elif data_dict["class"][i] == lst[2]:
		lst_5.append(data_dict["sepallength"][i])
		lst_6.append(data_dict["petallength"][i])
	else:
		pass

plt.scatter(lst_1, lst_2, marker = "s")
plt.scatter(lst_3, lst_4, marker = "v")
plt.scatter(lst_5, lst_6, marker = "o")
plt.plot()
plt.show()

sl = input("Enter value of Sepallength: ")
sw = input("Enter value of SepalWidth: ")
pl = input("Enter value of Petallength: ")
pw = input("Enter value of PetalWidth: ")
n_neighs = input("Enter number of neighbours you want to see: ")

u_input = []

u_input.append(float(sl))
u_input.append(float(sw))
u_input.append(float(pl))
u_input.append(float(pw))
u_input.append(int(n_neighs))

def sl():
	i = u_input[0]
	final_dict = {}
	k = 0
	
	for j in data_dict["sepallength"]:
		d = (i - data_dict["sepallength"][j])**2
		d = round(d**0.5, 1)
		final_dict[j] = (d, data_dict["class"][j])
	
	for w in sorted(final_dict, key = final_dict.get):
		lst.append((w, final_dict[w]))

	while k < u_input[4]:
		print(lst[k])
		k = k + 1

def sw():
	i = u_input[1]
	final_dict = {}
	k = 0

	for j in data_dict["sepalwidth"]:
		d = (i - data_dict["sepalwidth"][j])**2
		d = round(d**0.5, 1)
		final_dict[j] = (d, data_dict["class"][j])
		
	for w in sorted(final_dict, key = final_dict.get):
		lst.append((w, final_dict[w]))

	while k < u_input[4]:
		print(lst[k])
		k = k + 1

def pl():
	i = u_input[2]
	final_dict = {}
	k = 0
	
	for j in data_dict["petallength"]:
		d = (i - data_dict["petallength"][j])**2
		d = round(d**0.5, 1)
		final_dict[j] = (d, data_dict["class"][j])
	
	for w in sorted(final_dict, key = final_dict.get):
		lst.append((w, final_dict[w]))

	while k < u_input[4]:
		print(lst[k])
		k = k + 1

def pw():
	i = u_input[3]
	final_dict = {}
	k = 0
	
	for j in data_dict["petalwidth"]:
		d = (i - data_dict["petalwidth"][j])**2
		d = round(d**0.5, 1)
		final_dict[j] = (d, data_dict["class"][j])
	
	for w in sorted(final_dict, key = final_dict.get):
		lst.append((w, final_dict[w]))

	while k < u_input[4]:
		print(lst[k])
		k = k + 1

method = int(input("Which char. do you want to compare with? \n1. SepalLength\n2. SepalWidth\n3. PetalLength\n4. PetalWidth\n"))

if method == 1:
	sl()
elif method == 2:
	sw()
elif method == 3:
	pl()
elif method == 4:
	pw()
else:
	pass