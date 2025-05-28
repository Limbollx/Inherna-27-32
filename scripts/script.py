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

omega_0 = 1.0                       # Fréquence propre du bassin, omega_0 [rad/s]
F = 0.05                            # Amplitude de la force périodique, F [m]
omega_force = 0.9                   # Fréquence de la force périodique, omega_force [rad/s]
h_0 = 0.0                           # Hauteur initiale, h_0 [m]
v_0 = 0.0                           # Vitesse initiale, v_0 [m/s]
tf = 120                            # Temps final de simulation, tf [s]
dt = 0.01                           # Pas de temps, dt [s]

h = np.array([h_0])                 # Tableau des hauteurs, h [m]
v = np.array([v_0])                 # Tableau des vitesses verticales, v [m/s]
time = np.arange(0, tf, dt)         # Tableau de temps, time [s]

for t in time[:-1]:
    v_nv = v[-1] + dt * (-omega_0**2 * h[-1] + F * np.cos(omega_force * t))
    h = np.append(h, h[-1] + dt * v[-1])
    v = np.append(v, v_nv)

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(time, h, linestyle='-', color=(1, 0.5, 0.7), linewidth=2)
plt.title("Hauteur du bateau en fonction du temps")
plt.xlabel('Temps [s]')
plt.ylabel('Hauteur [m]')
plt.grid(color=(0.75, 0.75, 0.75), linestyle='--')

plt.subplot(1, 2, 2)
plt.plot(time, v, linestyle='-', color=(0.4, 0.8, 0.6), linewidth=2)
plt.title("Vitesse verticale en fonction du temps")
plt.xlabel('Temps [s]')
plt.ylabel('Vitesse [m/s]')
plt.grid(color=(0.75, 0.75, 0.75), linestyle='--')

plt.tight_layout()
plt.show()


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
