import numpy as np
import matplotlib.pyplot as plt
import functions as fun

# ============================================
# Model of thermal stress at the borehole wall
# ============================================
# Kerish equations from Jayger and Cook
# with some implemtation method from Zoback


# Thermal Stress Magnatude
# ------------------------
'''
Calculate the magnatude of thermally induced stess [MPa] for a  
range of reservior tempratures and assuming steady state conditions.
The convention of - as tensile and + as compressive is used here
'''
Twell = 40 + 273.14 # drilling gluid temp in Kelvin
therex = 1.e-5 # coefficent of thermal expansion
nu = 0.25 # Possions ratio
K = 1.e10 # bulk modulus

# thermal stress for reservior temps 50-300
sigma_Dt_lst = []   
for n in [50,100,150,200,250,300]:
    Tres = n + 273.14 # convert to Kelvin
    x = fun.fsigma_Dt(therex, K, nu, Tres, Twell)
    sigma_Dt_lst.append(x)

print(sigma_Dt_lst)

sigma_Dt = np.asarray(sigma_Dt_lst)
print(sigma_Dt)

# Geomechanical model paramaters
# ------------------------------
'''
Stress state and fluid pressures for a single depth 
'''

# strike slip faulting case
# stress/pressure in MPa
'''
SHmax = 90
Sv = 88.2
Shmin = 51.5 
Pp = 31.5  # why is this Pp so high?
Pmud = Pp 
'''

# normal faulting case
# stress/pressure in MPa
SHmax = 26
Sv = 88.232 
Shmin = 20 
Pp = 13.
Pmud = 14.75

# fixed paramaters 
nu = 0.1
R = 1
r = 1.0
n = 200


plt.figure('Sigma rr',figsize=(10,5))

# angles around the borehole wall
theta = fun.ftheta(n)


#rr = stress.fsigma_rr(SHmax, Shmin, Pp, Pmud, R, r, theta)
#plt.plot(theta*180/np.pi,rr,label=r'$\sigma_{rr}$')

#zz = stress.fsigma_zz(SHmax,Sv,Shmin,nu,Pp,R,r,theta,sigma_Dt) # the mean of this should = the mean stress?
#plt.plot(theta*180/np.pi,zz,label=r'$\sigma_{zz}$')

tt = stress.fsigma_tt(SHmax, Shmin, Pp, Pmud, 0., R, r, theta)
plt.plot(theta*180/np.pi,tt,label=r'$\sigma_{\theta \theta}$ with DT = 0')

tt = stress.fsigma_tt(SHmax, Shmin, Pp, Pmud, -2., R, r, theta)
plt.plot(theta*180/np.pi,tt,label=r'$\sigma_{\theta \theta}$ with DT = 10')

tt = stress.fsigma_tt(SHmax, Shmin, Pp, Pmud, -12., R, r, theta)
plt.plot(theta*180/np.pi,tt,label=r'$\sigma_{\theta \theta}$ with DT = 80')

tt = stress.fsigma_tt(SHmax, Shmin, Pp, Pmud, -22., R, r, theta)
plt.plot(theta*180/np.pi,tt,label=r'$\sigma_{\theta \theta}$ with DT = 110')

tt = stress.fsigma_tt(SHmax, Shmin, Pp, Pmud, -32., R, r, theta)
plt.plot(theta*180/np.pi,tt,label=r'$\sigma_{\theta \theta}$ with DT = 160')

tt = stress.fsigma_tt(SHmax, Shmin, Pp, Pmud, -42., R, r, theta)
plt.plot(theta*180/np.pi,tt,label=r'$\sigma_{\theta \theta}$ with DT = 210')

tt = stress.fsigma_tt(SHmax, Shmin, Pp, Pmud, -52., R, r, theta)
plt.plot(theta*180/np.pi,tt,label=r'$\sigma_{\theta \theta}$ with DT = 260')

plt.xlabel(r'$\theta$ (degrees)')
plt.ylabel('Effective stress (MPa)')
plt.legend()
plt.show()


