'''
 # @ Auteur: Mathéo Guillot--Eid
 # @ Crée le: 2025-05-21 11:35:50
 # @ Modifié par: Basri
 # @ Modifié le: 28/05/2025 15:01:14
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

# --- Calcul des fréquences angulaires ---
omega_lunaire = 2 * np.pi / T_lunaire  # fréquence angulaire lunaire
omega_solaire = 2 * np.pi / T_solaire  # fréquence angulaire solaire

# --- Amplitudes des forces ---
F_lunaire = 1e-6  # amplitude de la force lunaire
F_solaire = 0.5 * F_lunaire  # amplitude de la force solaire (50% de la force lunaire)

omega0 = omega_lunaire  # fréquence naturelle du système

# --- Paramètres numériques ---
dt = 10  # pas de temps en secondes
Tmax = 29 * 86400  # durée totale de simulation (29 jours en secondes)
N = int(Tmax / dt)  # nombre de points de calcul

# --- Initialisation ---
t = np.linspace(0, Tmax, N)  # vecteur temps
h = np.zeros(N)  # vecteur hauteur d'eau
v = np.zeros(N)  # vecteur vitesse
gamma = -3e-3  # coefficient de frottement (amortissement)

# --- Conditions initiales ---
h[0] = 0.0  # hauteur initiale
v[0] = 0.0  # vitesse initiale

# --- Schéma d'Euler explicite ---
for i in range(N - 1):
    # Calcul de la force totale (lunaire + solaire)
    force = F_lunaire * np.cos(omega_lunaire * t[i]) + F_solaire * np.cos(omega_solaire * t[i])
    # Calcul de l'accélération
    a = gamma * v[i] - omega0**2 * h[i] + force
    # Mise à jour de la vitesse
    v[i+1] = v[i] + a * dt
    # Mise à jour de la position
    h[i+1] = h[i] + v[i] * dt

# --- Tracé ---
plt.figure(figsize=(12, 5))
plt.plot(t / 3600 / 24, h)
plt.xlabel("Temps (jours)")
plt.ylabel("Hauteur h(t) (m)")
plt.title("Modèle de marée d'un bassin (lunaire + solaire)")
plt.grid(True)
plt.tight_layout()
plt.savefig("../img/marée_lunaire_solaire.png",dpi = 300)
plt.show()


# %%