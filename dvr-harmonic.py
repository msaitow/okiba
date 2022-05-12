import numpy as np
import time as tm
from functools import reduce

# -:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|
# 離散変数表現(DVR)法を用いて一次元シュレーディンガー方程式を数値的に解く。
# 各行列要素の導出など詳細は、以下の参考文献を参照。
#  D. T. Colbert, and W. H. Miller, J. Chem. Phys. 96, 1982 (1992).
# -:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|-:|

# 区間数
dim    :int   = 7000
# 積分範囲
xinit  :float = -50.0
xfinal :float =  50.0
# 一区間の長さ
dx :float = (xfinal-xinit)/dim

# プランク定数
hbar :float = 1.0
# 質量
m : float   = 1.0

# 運動エネルギー行列要素の計算
def formKinetic() -> np.ndarray:
    k :np.ndarray = np.zeros([dim,dim])
    for i in range(dim):
        for j in range(i,dim):
            fac :float = hbar**2 / (2*m) * (-1.0)**(i-j) / dx**2.0 
            if i==j: k[i,j] = fac * np.pi**2 / 3.0
            else:    k[i,j] = k[j,i] = fac * 2 / (i-j)**2
    return k

# 調和振動子ポテンシャルエネルギー行列要素の計算
def formPotential() -> np.ndarray:
    # 振動子の力定数
    k :float = 10.0
    # 振動数
    omega :np.ndarray = np.sqrt(k/m)
    v :np.ndarray = np.zeros([dim,dim])
    for i in range(dim):
        x :float = xinit + i*dx
        v[i,i] = 0.5*k*x**2
    return v

# DVR波動関数（psi）を新規ファイル（ファイル名:f_name）にcsv形式でnumstates状態だけ保存
# 生成されたcsvファイルはExcelなどで開くことができ、波動関数をプロットできる
def saveWFs(psi :np.ndarray, f_name :str, numstates :int) -> None:
    outfile = open(f_name, "w")
    #
    label :list[str] = ["x"]
    for i in range(numstates): label.append("state{0:d}".format(i))
    l_str :str = reduce(lambda x,y: x + ', ' + y, label)
    outfile.write(l_str+'\n')
    for p in range(dim):
        data :list[float] = [xinit + p*dx]
        for i in range(numstates): data.append(psi[p,i])
        d_str :str = reduce(lambda x,y: x + ', ' + y, map(lambda x: "{0:.5e}".format(x), data))
        outfile.write(d_str+'\n')
    outfile.close()
    
# 厳密な調和振動子のエネルギー（比較用）
def calcEnergies() -> np.ndarray:
    # 振動子の力定数    
    k :float = 10.0
    # 振動数
    omega :float = np.sqrt(k/m)
    e :np.ndarray = np.zeros([dim])
    for i in range(dim): e[i] = hbar*omega*(i+0.5)
    return e

# 厳密なエネルギーとDVR計算による近似値を比較し、何状態までであれば1e-10以下の桁数で厳密な値と一致するかを比較
def compareEnergies(e1: np.ndarray, e2: np.ndarray) -> int:
    error = e1-e2
    idx = -1
    for i in range(error.shape[0]):
        if abs(error[i]) >= 1.0e-10:
            idx = i
            break
    return idx

# プログラム本体
if __name__ == '__main__':
    tinit = tm.perf_counter()
    # 各行列要素を構築
    t :np.ndarray = formKinetic()
    v :np.ndarray = formPotential()
    # ハミルトニアン行列
    h :np.ndarray = t + v
    # ハミルトニアン行列を対角化し、エネルギーと波動関数を計算
    edvr, psi = np.linalg.eigh(h)
    # 厳密なエネルギーも計算し、これらを比較
    eexact :np.ndarray = calcEnergies()
    print("Energies (DVR)")
    print(edvr)
    print("Energies (Exact)")    
    print(eexact)
    print("\n==|> DVR energies match up to {0:d} states with the exact ones!".format(compareEnergies(edvr,eexact)) )
    # 50状態の波動関数をでcsvファイル（wf.csv）に保存
    saveWFs(psi,"wf.csv",50)
    tfinal = tm.perf_counter()
    # プログラムの実行時間を表示
    print("Elapsed time: {0:.2f} sec.".format(tfinal-tinit))
    
    
    
