import matplotlib.pyplot as plt
x=[1,3,3,1,1,2,3]
y=[1,1,3,3,1,4,3]
plt.plot(x,y,color='brown',linewidth=3)
plt.fill(x,y,color='lightblue')
plt.title("House")
plt.axis('equal')
plt.show()