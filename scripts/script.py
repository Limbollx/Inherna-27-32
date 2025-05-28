'''
 # @ Auteur: Mathéo Guillot--Eid
 # @ Crée le: 2025-05-21 11:35:50
 # @ Modifié par: Mathéo Guillot--Eid
 # @ Modifié le: 2025-05-27 19:15:59
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