import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

#from matplotlib.ticker import MultipleLocator

data = pd.read_csv('comparison.csv')
df = data.iloc[0:21]
print(df.head())

#ax.plot( x,y1,'rs:',label='line1')
#ax.plot(y2,color='C0',marker='^',linestyle='-',label='line2')

fig = plt.figure()
ax = fig.add_subplot(111,xlabel='Value of $\lambda$', ylabel='Effective Energy (No Unit)')

ax.plot(df['lambda'], df['epsilon0(PT1)' ], markersize=4, marker='D', linestyle='-' , label='$\epsilon_0$ (PT1)')
ax.plot(df['lambda'], df['epsilon1(PT1)' ], markersize=4, marker='o', linestyle='--' , label='$\epsilon_1$ (PT1)')
ax.plot(df['lambda'], df['epsilon2(PT1)' ], markersize=4, marker='^', linestyle=':' , label='$\epsilon_2$ (PT1)')

ax.plot(df['lambda'], df['epsilon0(Exact)' ], markersize=4, marker='v', linestyle='-' , label='$\epsilon_0$ (Exact)')
ax.plot(df['lambda'], df['epsilon1(Exact)' ], markersize=4, marker='+', linestyle='--' , label='$\epsilon_1$ (Exact)')
ax.plot(df['lambda'], df['epsilon2(Exact)' ], markersize=4, marker='*', linestyle=':' , label='$\epsilon_2$ (Exact)')

#ax.plot(df['TCutDOI'], df['PMPNO' ], markersize=4, marker='o', linestyle='--', label='PM-LVMO')
#ax.plot(df['TCutDOI'], df['PAOPNO'], markersize=4, marker='^', linestyle=':' , label='PAO')
ax.set_ylim(0,15)

################################################
##labels= []
##for tick in ax.get_yticks():
##    label= f'{tick:0<.1f}'
##    labels.append(label[:-1].rstrip('.'))
##    
##ax.set_yticks(ax.get_yticks())    
##ax.set_yticklabels(labels)
################################################

# effective digits for y axis
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
ax.xaxis.grid(True, which='minor',linestyle='solid', linewidth=0.3)
ax.minorticks_on()

#ax.grid(linestyle='dotted', linewidth=1)
ax.grid(True)
ax.legend()
#ax.set_xlim(0.8e-4,0.5e-1)
#ax.set_xlim(0.8e-4,1.0e-1)
#ax.invert_xaxis()
#plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_xscale('log')
#plt.yscale('log')

### subplot
##sub_axes = plt.axes([0.5, 0.38, .35, .25])
##sub_axes.grid()
##sub_axes.set_xlim(1.0e-4,1e-2)
##sub_axes.set_ylim(99.8, 100.0)
##sub_axes.invert_xaxis()
##sub_axes.plot(df['TCutDOI'], df['FPPNO' ], markersize=4, marker='D', linestyle='-' , label='FB-LVMO')
##sub_axes.plot(df['TCutDOI'], df['PMPNO' ], markersize=4, marker='o', linestyle='--', label='PM-LVMO')
##sub_axes.plot(df['TCutDOI'], df['PAOPNO'], markersize=4, marker='^', linestyle=':' , label='PAO')
##sub_axes.xaxis.grid(True, which='minor',linestyle='solid', linewidth=0.3)
##sub_axes.set_xscale('log')

#sub_axes.set_xticks([5.0e-3],minor=True)
#sub_axes.set_xticklabels([5e-3],minor=True)

#fig.subplots_adjust(bottom=0.2)

fig.savefig('comp.pdf')
