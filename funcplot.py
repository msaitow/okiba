import matplotlib.pyplot as plt
import numpy as np
z = np.linspace( 0, 4, 80)   # linspace(min, max, N) で範囲 min から max を N 分割します
e = z*z-27.0/8.0*z
de = 2.0*z-27.0/8.0


fig = plt.figure()
#ax = fig.add_subplot(111,xlabel='Value of parameter Z', ylabel='Energy of Helium atom/ Eh')

plt.xlabel('Value of parameter Z', fontsize=14)
plt.ylabel('Energy of Helium atom/ Eh', fontsize=14)
plt.grid(which='major', color='gray', linestyle='--')
plt.grid(which='minor', color='gray', linestyle='--')
plt.tick_params(labelsize=11)
plt.plot(z,  e, label='$E[Z]$')
plt.plot(z, de, label='$\\frac{\\partial E[Z]}{\\partial Z}$')
#plt.legend()
plt.legend(fontsize=14)
plt.show()
