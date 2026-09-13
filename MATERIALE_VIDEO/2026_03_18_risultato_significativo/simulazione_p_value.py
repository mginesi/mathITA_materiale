import numpy as np
import scipy.stats as stat

def zvalue_to_pvalue(z):
    return stat.norm.sf(z) * 2

Np = 50 # numero test con placebo
Nt = 50 # numero test con trattamento
kp = 16 # numero superati con placebo
kt = 24 # numero superati con trattamento
# probabilità campionarie
pp = kp / Np
pt = kt / Nt
phat = (kp + kt) / (Np + Nt)
# errore standard
SE = np.sqrt(phat * (1-phat) * (1/Np + 1/Nt))
# z-value
z = (pt - pp) / SE

print("d = " + str(pt - pp))
print("phat = " + str(phat))
print("SE = " + str(SE))
print("z-value = " + str(z))
print("p-value = " + str(zvalue_to_pvalue(z)))

