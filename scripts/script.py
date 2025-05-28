'''
 # @ Auteur: Mathéo Guillot--Eid
 # @ Crée le: 2025-05-21 11:35:50
 # @ Modifié par: Basri
 # @ Modifié le: 28/05/2025 12:09:24
 # @ Description: Script de simulation
 '''

import numpy as np
import matplotlib.pyplot as plt

#%%
#====Code 2=====#
# je sais pas pourquoi ça monte à 100 mètres


import numpy as np
import matplotlib.pyplot as plt

# --- Paramètres physiques ---
T_lunaire = 44714  # période de marée lunaire M2 en secondes (~12h25)
T_solaire = 43200  # période de marée solaire S2 en secondes (~12h)

omega_lunaire = 2 * np.pi / T_lunaire
omega_solaire = 2 * np.pi / T_solaire

F_lunaire = 1e-6
F_solaire = 0.46 * F_lunaire

omega0 = omega_lunaire * omega_solaire

# --- Paramètres numériques ---
dt = 10
Tmax = 29 * 86400
N = int(Tmax / dt)

# --- Initialisation ---
t = np.linspace(0, Tmax, N)
h = np.zeros(N)
v = np.zeros(N)

# Conditions initiales
h[0] = 0.0
v[0] = 0.0

gamma = 1e-5

for i in range(N - 1):
    force = F_lunaire * np.cos(omega_lunaire * t[i]) + F_solaire * np.cos(omega_solaire * t[i])
    a = -2 * gamma * v[i] - omega0**2 * h[i] + force
    v[i+1] = v[i] + a * dt
    h[i+1] = h[i] + v[i] * dt

# --- Tracé ---
plt.figure(figsize=(12, 5))
plt.plot(t / 3600 / 24, h)
plt.xlabel("Temps (jours)")
plt.ylabel("Hauteur h(t) (m)")
plt.title("Modèle de marée d'un bassin (lunaire + solaire)")
plt.grid(True)
plt.tight_layout()
plt.show()


# %%
