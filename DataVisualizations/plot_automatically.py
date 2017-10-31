import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]

plt.scatter(x_values, y_values,edgecolor='none', s=40)
#set chart title and label axis
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.axis([0,1100,0,1100000])
#set size of tick labels
plt.tick_params(axis='both', which='major',labelsize=14)
##Saves the image as a png
plt.savefig('plot_automatically.pdf',bbox_inches='tight')
#shows the plot
plt.show()
