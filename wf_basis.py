import numpy as np
from scipy.constants import pi

# position-space functions
def Sr1s(z,r): return 2*z**(3/2) * np.exp(-z * r)
def Sr2s(z,r): return 2/np.sqrt(3) * z**(5/2) * r * np.exp(-z*r)
def Sr3s(z,r): return 2**(3/2)/(3*np.sqrt(5)) * z**(7/2) * r**2 * np.exp(-z*r)
def Sr4s(z,r): return 2/(3*np.sqrt(35)) * z**(9/2) * r**2 * np.exp(-z*r)
def Sr5s(z,r): return 2**(3/2)/(45*np.sqrt(7)) * z**(11/2) * r**4 * np.exp(-z*r)
def Sr2p(z,r): return 2/np.sqrt(3) * z**(5/2) * r * np.exp(-z*r)
def Sr3p(z,r): return 2**(3/2)/(3*np.sqrt(5)) * z**(7/2) * r**2 * np.exp(-z*r)
def Sr4p(z,r): return 2/(3*np.sqrt(35)) * z**(9/2) * r**3 * np.exp(-z*r)
def Sr5p(z,r): return 2**(3/2)/(45*np.sqrt(7)) * z**(11/2) * r**4 * np.exp(-z*r)
def Sr3d(z,r): return 2**(3/2)/(3*np.sqrt(5)) * z**(7/2) * r**2 * np.exp(-z*r)
def Sr4d(z,r): return 2/(3*np.sqrt(35)) * z**(9/2) * r**3 * np.exp(-z*r)

# Momentum-space functions
def Sk1s(z,k): return 1/(2*pi)**(3/2) * 16*pi*z**(5/2)/(z**2 + k**2)**2
def Sk2s(z,k): return 1/(2*pi)**(3/2) * 16*pi*z**(5/2)*(3*z**2-k**2)/(np.sqrt(3) * (z**2 + k**2)**3)
def Sk3s(z,k): return 1/(2*pi)**(3/2) * 64*np.sqrt(10)*pi*z**(9/2)* (z**2-k**2)/(5*(z**2+k**2)**4)
def Sk4s(z,k): return 1/(2*pi)**(3/2) * 64*pi*z**(9/2)*(5*z**4-10*z**2*k**2+k**4)/(np.sqrt(35)*(z**2+k**2)**5)
def Sk5s(z,k): return 1/(2*pi)**(3/2) * 128*np.sqrt(14)*pi*z**(13/2)*(3*z**4-10*z**2*k**2+3*k**4)/(21*(z**2+k**2)**6)
def Sk2p(z,k): return 1/(2*pi)**(3/2) * 64*pi*k*z**(7/2)/(np.sqrt(3)*(z**2+k**2)**3)
def Sk3p(z,k): return 1/(2*pi)**(3/2) * 64*np.sqrt(10)*pi*k*z**(7/2)*(5*z**2-k**2)/(15*(z**2+k**2)**4)
def Sk4p(z,k): return 1/(2*pi)**(3/2) * 128*pi*k*z**(11/2)*(5*z**2-3*k**2)/(np.sqrt(35)*(z**2 + k**2)**5)
def Sk5p(z,k): return 1/(2*pi)**(3/2) * 128*np.sqrt(14)*pi*k*z**(11/2)*(35*z**4-42*z**2*k**2+3*k**4)/(105*(z**2+k**2)**6)
def Sk3d(z,k): return 1/(2*pi)**(3/2) * 128*np.sqrt(10)*pi*k**2*z**(9/2)/(5*(z**2+k**2)**4)
def Sk4d(z,k): return 1/(2*pi)**(3/2) * 128*pi*k**2*z**(9/2)*(7*z**2-k**2)/(np.sqrt(35)*(z**2 + k**2)**5)

