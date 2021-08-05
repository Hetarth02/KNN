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

plt.scatter(lst_1, lst_2, marker = "s", color = "g")
plt.scatter(lst_3, lst_4, marker = "v", color = "b")
plt.scatter(lst_5, lst_6, marker = "x", color = "k")
plt.xlabel("Sepal - Length")
plt.ylabel("Petal - Length")
plt.legend(["Iris-setosa", "Iris-versicolor", "Iris-virginica"], loc ="best")
plt.plot()
plt.show()