from numpy import linalg as la
import numpy as np
from functools import reduce

# -:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|
# 離散変数表現(DVR)法を用いて一次元シュレーディンガー方程式を数値的に解く。
# 各行列要素の導出など詳細は、以下の参考文献を参照。
#  D. T. Colbert, and W. H. Miller, J. Chem. Phys. 96, 1982 (1992).
# -:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|

# 区間数
dim    = 2000
# 積分範囲
xinit  = -20.0
xfinal =  20.0
# 一区間の長さ
dx     = (xfinal-xinit)/dim

# プランク定数
hbar = 1.0
# 質量
m    = 1.0

# 運動エネルギー行列要素の計算
def formKinetic():
    k = np.zeros([dim,dim])
    for i in range(dim):
        for j in range(i,dim):
            fac = hbar**2 / (2*m) * (-1.0)**(i-j) / dx**2.0 
            if i==j: k[i,j] = fac * np.pi**2 / 3.0
            else:    k[i,j] = k[j,i] = fac * 2 / (i-j)**2
    return k

# 調和振動子ポテンシャルエネルギー行列要素の計算
def formPotential():
    # 振動子の力定数
    k     = 10.0
    # 振動数
    omega = np.sqrt(k/m)
    v = np.zeros([dim,dim])
    for i in range(dim):
        x = xinit + i*dx
        v[i,i] = 0.5*k*x**2
    return v

# 厳密な調和振動子のエネルギー（比較用）
def calcEnergies():
    # 振動子の力定数    
    k     = 10.0
    # 振動数
    omega = np.sqrt(k/m)
    e = np.zeros([dim])
    for i in range(dim): e[i] = hbar*omega*(i+0.5)
    return e

if __name__ == '__main__':
    # 各行列要素を構築
    t = formKinetic()
    v = formPotential()
    # ハミルトニアン行列
    h = t + v
    # ハミルトニアン行列を対角化
    edvr, psi = la.eigh(h)
    # 厳密なエネルギーも計算し、これらを比較
    eexact = calcEnergies()
    print("Energies (DVR)")
    print(edvr)
    print("Energies (Exact)")    
    print(eexact)

    # 50状態の波動関数をでcsvファイル（wf.csv）に保存
    numstates = 50
    outfile   = open("wf.csv", "w")

    label = ["x"]
    for i in range(numstates): label.append("state{0:d}".format(i))
    l_str = reduce(lambda x,y: x + ', ' + y, label)
    outfile.write(l_str+'\n')
    for p in range(dim):
        data = [xinit + p*dx]
        for i in range(numstates): data.append(psi[p,i])
        #d_str = []
        #for d in data: d_str.append("{0:.5e}".format(d))
        d_str = reduce(lambda x,y: x + ', ' + y, map(lambda x: "{0:.5e}".format(x), data))
        outfile.write(d_str+'\n')
        #print(d_str)

    outfile.close()
    
        
    
    
