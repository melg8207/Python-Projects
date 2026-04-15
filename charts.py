import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,25,30]
plt.plot(x,y)
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

categories=['A','B','C','D']
values=[5,7,3,8]
plt.bar(categories,values)
plt.title("Bar Chart")
plt.show()

labels=['Python','Java','C++']
sizes=[40,35,25]
plt.pie(sizes, labels=labels,autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

x=[1,2,3,4,5]
y=[5,7,8,7,6]
plt.scatter(x,y)
plt.title("Scatter Plot")
plt.show()

data=[1,2,2,3,3,3,4,4,5]
plt.hist(data)
plt.title("Histogram")
plt.show()

x=[1,2,3,4]
y1=[10,20,30,40]
y2=[5,15,25,35]
plt.plot(x,y1,label="Line 1")
plt.plot(x,y2,label="Line 2")
plt.legend()
plt.title("Multiple Lines")
plt.show()

data=[10,20,30,40,50]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()

x=[1,2,3,4]
y=[3,5,7,9]
plt.fill_between(x,y)
plt.title("Area Plot")
plt.show()

plt.subplot(1,2,1)
plt.plot([1,2,3],[4,5,6])
plt.title("Plot 1")
plt.subplot(1,2,2)
plt.plot([1,2,3],[6,5,4])
plt.title("Plot 2")
plt.show()

x=['Mon','Tue','Wed']
y=[10,20,15]
plt.bar(x,y)
for i in range(len(x)):
    plt.text(i,y[i],y[i])
plt.title("Bar Chart with Values")
plt.show()