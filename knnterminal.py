import pandas as pd

data = pd.read_csv("/sdcard/Python/KNN/Datasets/Iris.csv")

data_dict = data.to_dict()

#Iris-setosa
#Iris-versicolor
#Iris-virginica

u_input = [4.5, 3.6, 3.4, 1.3, 3]
lst = []

"""
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
"""

def predict():
	for i in data_dict:
		while i == "sepallength":
			for j in data_dict[i]:
				d = (u_input[0] - data_dict[i][j])**2

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

def super():
	input_total = 0
	input_mean = 0
	data_total = 0
	data_mean = 0
	k = 0
	final_dict = {}
	
	for i in range(len(u_input) - 1):
		input_total = input_total + u_input[i]

	input_mean = input_total / (len(u_input) - 1)
	
	for i in data_dict["sepallength"]:
			data_total = data_dict["sepallength"][i] + data_dict["petallength"][i] + data_dict["sepalwidth"][i] + data_dict["petalwidth"][i]
			data_mean = data_total / 4
			d = (input_mean - data_mean)**2
			d = round(d**0.5, 1)
			final_dict[i] = (d, data_dict["class"][i])
		
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
	super()