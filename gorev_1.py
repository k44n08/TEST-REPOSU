import numpy as np
import matplotlib.pyplot as plt

# Örnek değerler (gerçek pod değerleri değil)
m = 100.0        # kütle (kg)
F_itki = 500.0   # itki kuvveti (N)
F_direnc = 100.0 # sabit direnç (N)

dt = 0.01        # zaman adımı (s)
T = 10.0         # toplam süre (s)

t = np.arange(0, T, dt)
x = np.zeros(len(t))   # konum
v = np.zeros(len(t))   # hız

for i in range(1, len(t)):
    a = (F_itki - F_direnc) / m      # m*a = itki - direnç
    v[i] = v[i-1] + a * dt           # hız = eski hız + ivme*dt
    x[i] = x[i-1] + v[i] * dt        # konum = eski konum + hız*dt

plt.plot(t, x)
plt.xlabel("Zaman (s)")
plt.ylabel("Konum (m)")
plt.title("Pod 1 boyutlu hareket")
plt.grid()
plt.savefig("zaman_konum.png")
plt.show()