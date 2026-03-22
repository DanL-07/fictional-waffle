import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2)) + z0
A = 1.0
x0 = 0.0
sig = 2.0
z0 = 0.0
x = np.linspace(-10,10,200)
y = gauss(x,A,x0,sig,z0)


#Plot gaussian alone
plt.plot(x,y,label="Gaussian")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gaussian Function")
plt.show()

#Calculate area
area, error = quad(gauss,0,2.5,args=(A,x0,sig,z0))
print("Area between 0 and 2.5 =",area)
print("Estimated error =",error)
x_fill = np.linspace(0,2.5,200)

#Plot 2, with area 
plt.plot(x,y,label="Gaussian")
plt.fill_between(x_fill,gauss(x_fill,A,x0,sig,z0),label=f"Area = {area:.3f}",alpha=0.3)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gaussian with Integration Area")
plt.legend()
plt.show()

#Use quad to calculate the total area of the gaussian
analytic = A*sig*np.sqrt(2*np.pi)
atotal, err = quad(gauss,-np.inf,np.inf,args=(A,x0,sig,z0))
print("Total area =",atotal)


print("Analytical result =",analytic)
print("Difference =",abs(atotal-analytic))

if abs(atotal-analytic)<10**(-10): print ("The result from quad and the equation shown are the same, at least for any practical usecase")
else: print("Something went wrong")

#7
    
#User values
A = float(input("Enter A: "))
x0 = float(input("Enter x0: "))
sig = float(input("Enter sigma: "))
z0 = float(input("Enter z0: "))
x_min = float(input("Lower integration limit: "))
x_max = float(input("Upper integration limit: "))

#Set plotting parameters
x = np.linspace(x_min-5,x_max+5,200)
y = gauss(x,A,x0,sig,z0)
area,err = quad(gauss,x_min,x_max,args=(A,x0,sig,z0))
#Plot
plt.plot(x,y,label="Gaussian")
x_fill = np.linspace(x_min,x_max,200)
plt.fill_between(x_fill,gauss(x_fill,A,x0,sig,z0),alpha=0.3,label=f"Area = {area:.3f}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Gaussian Area")
plt.show()

print("Area between limits =",area)





