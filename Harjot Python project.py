import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

a=pd.read_csv('water_potability.csv')
print(a)

print('\n','Row x Column of the Data=',a.shape)

print('\n','Total Number of Elements in Data Frame=',a.size)

print('\n','Name of columns present in the data frame=',a.columns)

print('\n','Data type of each Column=\n',a.dtypes)

print(a.Hardness)
print(a.iloc[:, 0])

print('\n','Informartion regarding Data frame=')
print(a.info()) 

plt.figure()
x=a.Hardness
y=a.Solids
plt.title('Hardness VS Solids present in the water')
plt.xlabel('Hardness->')
plt.ylabel('Solids->')
y=a.Solids
plt.plot(x,y,'.',c='blue')

plt.figure()
m=a.Conductivity
n=a.Organic_carbon
plt.title('Conductivity VS Organic carbon')
plt.xlabel('Conductivity->')
plt.ylabel('Organic carbon->')
plt.plot(m,n,'.',c='red')

plt.figure()
f=a.Chloramines
g=a.Sulfate
plt.title('Chloramines VS Sulfate')
plt.xlabel('Chloramines->')
plt.ylabel('Sulfates->')
plt.plot(f,g,'.',c='green')

plt.figure()
o=a.Trihalomethanes
p=a.Turbidity
plt.title('Trihalomethanes VS Turbidity')
plt.xlabel('Trihalomethanes->')
plt.ylabel('Turbidity->')
plt.plot(o,p,'.',c='violet')

plt.figure(figsize=(15,10))
plt.plot(a.Potability,c='orange')
plt.title("Distribution of Unsafe and Safe Water")
plt.xlabel('Count')
plt.ylabel('Potability')
plt.show()

plt.figure()
o=a.Turbidity
p=a.Potability
plt.title('Turbidity VS Potability')
plt.xlabel('Turbidity->')
plt.ylabel('Potability->')
plt.plot(o,p,'.',c='orange')


plt.figure()
plt.title('Average composition of Salts present in Water')
labels=['Chloramines','Organic_carbon','Turbidity','Trihalomethanes']
sizes=[7,14,4,60]
colors=['gold','red','blue','skyblue','orange']
plt.pie(sizes, colors=colors,labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()