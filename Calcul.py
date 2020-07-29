from matplotlib import pyplot as plt
from math import *

# cout_installation en kg de CO2
# Le rendement définit le nombre d'unité de chaleur que produit chaque unité d'énergie mis dans le système (un rendement de 2 signifie que chaque kWh est transformé en 2 kWh d'énergie thermique)


def nb_kg_co2(nb_annee, cout_installation, kwh_par_an, rendement, kgco2_par_kwh):
    return cout_installation + nb_annee * kwh_par_an / rendement * kgco2_par_kwh


plt.style.use("seaborn")
x_pompe_a_chaleur = range(0, 11)
y_pompe_a_chaleur = [nb_kg_co2(n, 0, 4000, 2, 0.080) for n in x_pompe_a_chaleur]

x_chaudiere_charbon = range(0, 11)
y_chaudiere_charbon = [nb_kg_co2(n, 0, 4000, 0.7, 0.404) for n in x_chaudiere_charbon]

x_chaudiere_gaz = range(0, 11)
y_chaudiere_gaz = [nb_kg_co2(n, 0, 4000, 0.86, 0.258) for n in x_chaudiere_gaz]

x_chaudiere_fioul = range(0, 11)
y_chaudiere_fioul = [nb_kg_co2(n, 0, 4000, 0.83, 0.335) for n in x_chaudiere_fioul]

plt.plot(x_pompe_a_chaleur, y_pompe_a_chaleur, label="Pompe à chaleur")
plt.plot(x_chaudiere_charbon, y_chaudiere_charbon, label="Chaudière à charbon")
plt.plot(x_chaudiere_gaz, y_chaudiere_gaz, label="Chaudière à gaz")
plt.plot(x_chaudiere_fioul, y_chaudiere_fioul, label="Chaudière à fioul")

plt.xlabel("Nombre d'années")
plt.ylabel("kg de CO2 émis")
plt.title(label="kg de CO2 émis cumulé selon l'appareil en France pour 4000kWh d'énergie thermique fourni par an", fontsize=11)
plt.legend()
plt.tight_layout()
plt.show()
