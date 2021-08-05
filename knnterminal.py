import pandas as pd

data = pd.read_csv("/sdcard/Python/KNN/Datasets/Iris.csv")

data_dict = data.to_dict()

#Iris-setosa
#Iris-versicolor
#Iris-virginica

u_input = [6.5, 5.5, 7.5, 8.5, 11]
lst = []
check_lst = []
pred_lst = []
final_dict = {}

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

def sl():
	i = u_input[0]
	k = 0
	
	for j in data_dict["sepallength"]:
		d = (i - data_dict["sepallength"][j])**2
		d = round(d**0.5, 1)
		final_dict[j] = (d, data_dict["class"][j])
	
	for w in sorted(final_dict, key = final_dict.get):
		lst.append((w, final_dict[w]))

	while k < u_input[4]:
		print(lst[k])
		check_lst.append(lst[k])
		k = k + 1
	predict(check_lst)

def sw():
	i = u_input[1]
	k = 0

	for j in data_dict["sepalwidth"]:
		d = (i - data_dict["sepalwidth"][j])**2
		d = round(d**0.5, 1)
		final_dict[j] = (d, data_dict["class"][j])
		
	for w in sorted(final_dict, key = final_dict.get):
		lst.append((w, final_dict[w]))

	while k < u_input[4]:
		print(lst[k])
		check_lst.append(lst[k])
		k = k + 1
	predict(check_lst)

def pl():
	i = u_input[2]
	k = 0
	
	for j in data_dict["petallength"]:
		d = (i - data_dict["petallength"][j])**2
		d = round(d**0.5, 1)
		final_dict[j] = (d, data_dict["class"][j])
	
	for w in sorted(final_dict, key = final_dict.get):
		lst.append((w, final_dict[w]))

	while k < u_input[4]:
		print(lst[k])
		check_lst.append(lst[k])
		k = k + 1
	predict(check_lst)

def pw():
	i = u_input[3]
	k = 0
	
	for j in data_dict["petalwidth"]:
		d = (i - data_dict["petalwidth"][j])**2
		d = round(d**0.5, 1)
		final_dict[j] = (d, data_dict["class"][j])
	
	for w in sorted(final_dict, key = final_dict.get):
		lst.append((w, final_dict[w]))

	while k < u_input[4]:
		print(lst[k])
		check_lst.append(lst[k])
		k = k + 1
	predict(check_lst)

def super():
	input_total = 0
	input_mean = 0
	data_total = 0
	data_mean = 0
	k = 0
	
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
		check_lst.append(lst[k])
		k = k + 1
	predict(check_lst)

def predict(check_lst):
	pred_class = check_lst
	count_setosa = 0
	count_versicolor = 0
	count_virginica = 0
	for i in range(len(pred_class)):
		if pred_class[i][1][1] == "Iris-setosa":
			count_setosa += 1
		elif pred_class[i][1][1] == "Iris-versicolor":
			count_versicolor += 1
		elif pred_class[i][1][1] == "Iris-virginica":
			count_virginica += 1
		else:
			print("Cannot predict accurately.")
	
	if count_setosa > count_versicolor:
		if count_setosa > count_virginica:
			print("Predicted Class: Iris-setosa.")
		else:
			print("Predicted Class: Iris-virginica.")
	elif count_versicolor > count_virginica:
		print("Predicted Class: Iris-versicolor.")
	else:
		print("Predicted Class: Iris-virginica.")

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