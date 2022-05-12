import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('plottest.csv')
df = data.iloc[0:10]
print(df.head())

#ax.plot( x,y1,'rs:',label='line1')
#ax.plot(y2,color='C0',marker='^',linestyle='-',label='line2')

fig = plt.figure()
ax = fig.add_subplot(111,xlabel=df.index.name, ylabel='number')

ax.plot(df['H'])
ax.plot(df['HR'], 'rs:', label='HR', ms=10, mew=5, mec='green')
ax.plot(df['K'], marker='^', linestyle='-')

fig.savefig('3-1_a.pdf')
