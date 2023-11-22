from typing import List, Tuple, Any, TypeGuard
from enum import Enum
from functools import reduce
from itertools import combinations
from dataclasses import dataclass, field

import pyrsistent as pyr

@dataclass(frozen=True,order=True)
class cont:
    left  : str
    right : list[str]
    def __repr__(self) -> str: return '%s += %s' % (self.left, self.right)

conts = list[cont]

def binDec(inp : list[str]) -> list[list[cont]]:
    #--
    # ['A','B','C'] -> (['X','C'], [cont('X0',['A','B'])]), (['X','A'], [cont('X0',['C','B'])]), (['X','B'], [cont('X0',['C','A'])])
    def unit(num : int, d : list[str]) -> list[tuple[list[str],conts]]:
        X : str = 'X%d' % num
        perms : list[list[str]] = list(map(lambda p: list(p), combinations(d,2)))
        rests : list[list[str]] = list(map(lambda p: list(pyr.freeze(p).append(X)), map(lambda p: list(set(d)-set(p)), perms)))
        conts : conts           = list(map(lambda p: cont(left=X,right=p), perms))
        return list(zip(rests,conts))
    #--
    ininp   : list[list[str]] = [inp]
    contras : list[conts]     = []
    #--
    maxDepth = 10
    for depth in range(maxDepth):
        oterms, oconts, newconts = [], [], [] 
        for pos in range(len(ininp)):
            p = unit(depth,ininp[pos])
            o = list(map(lambda q: q[0], p))
            c = list(map(lambda q: q[1], p))
            # save current results
            oterms.extend(o)            
            oconts.extend(c)            
            # accumulate results                    
            for cc in c:
                if len(contras)!=0: newconts.append( list(pyr.v(cc).extend(contras[pos])) )
                else:               newconts.append([cc])
                #newconts.append(cc)
        contras = newconts
        #print('oterms [depth:%d](%5d): %s' % (depth, len(oterms ), oterms))
        #print('oconts [depth:%d](%5d): %s' % (depth, len(oconts ), oconts))
        #print('contras[depth:%d](%5d): %s' % (depth, len(contras), contras))                
        if len(oterms[0])==1: break
        else:
            ininp    = oterms
            iniconts = oconts            
    #--
    return contras

def main() -> None:
    print('====== Test1 ======')
    inp1 = ['A','B','C']
    out1 = binDec(inp1)
    print('out1: %s' % out1)
    print('====== Test2 ======')
    inp2 = ['A','B']
    out2 = binDec(inp2)
    print('out2: %s' % out2)
    print('====== Test3 ======')
    inp3 = ['A','B','C', 'D']
    out3 = binDec(inp3)
    print('out3: %s' % out3)
    print('====== Test4 ======')
    inp4 = ['A', 'B', 'C', 'D', 'E']
    out4 = binDec(inp4)
    print('out4(%5d): %s' % (len(out4), out4))
    print('====== Test5 ======')
    inp5 = ['A', 'B', 'C', 'D', 'E', 'F']
    out5 = binDec(inp5)
    print('out5(%5d): %s' % (len(out5), out5))
    
if __name__=='__main__': main()
