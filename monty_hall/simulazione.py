import random
from matplotlib import pyplot as plt

def prepara_il_gioco():
    # inizializziamo il gioco
    porte = [0, 0, 0]
    # scegliamo dietro quale porta mettere il montepremio
    premio_pos = random.choice([0, 1, 2])
    # piazziamo il montepremio
    porte[premio_pos] = 1
    return porte

def prima_scelta():
    # il concorrente sceglie randomicamente una delle porte
    return random.choice([0, 1, 2])

def rivela_porta(porte, scelta_conc):
    porte_che_si_possono_aprire = []
    for _idx in range(3):
        if (porte[_idx] == 0) and (not(_idx == scelta_conc)):
            # se la porta non contiene il montepremi e non è stata scelta dal
            # concorrente, allora viene aggiunta alla lista delle porte che
            # il presentatore può aprire
            porte_che_si_possono_aprire.append(_idx)
    # il presentatore sceglie una porta a caso tra quelle papabili
    return random.choice(porte_che_si_possono_aprire)

def ultima_scelta(scelta_conc, porta_aperta):
    # Strategia 1: il concorrente non cambia
    scelta_mantenere = scelta_conc
    # Strategia 2: il concorrente cambia
    lista_porte = [0, 1, 2]
    # togliamo dalle possibili porte sia la scelta del concorrente che quella
    # aperta dal presentatore
    lista_porte.remove(scelta_conc)
    lista_porte.remove(porta_aperta)
    # scegliamo l'unica porta rimanente
    scelta_cambiare = lista_porte[0]
    return (scelta_mantenere, scelta_cambiare)

# SIMULAZIONE #

N_simul = 500 # numero di simulazioni
num_vittoria_mant = [0]
num_vittoria_camb = [0]

for _n in range(N_simul):
    porte = prepara_il_gioco()
    scelta_conc = prima_scelta()
    porta_aperta = rivela_porta(porte, scelta_conc)
    (scelta_mant, scelta_camb) = ultima_scelta(scelta_conc, porta_aperta)
    # aggiungiamo una vittoria alla scelta vincente ma non alla perdente
    if porte[scelta_mant] == 1:
        num_vittoria_mant.append(num_vittoria_mant[-1] + 1)
        num_vittoria_camb.append(num_vittoria_camb[-1])
    elif porte[scelta_camb] == 1:
        num_vittoria_mant.append(num_vittoria_mant[-1])
        num_vittoria_camb.append(num_vittoria_camb[-1] + 1)

# Rimuoviamo il tempo 0 dalle liste
num_vittoria_mant = num_vittoria_mant[1:]
num_vittoria_camb = num_vittoria_camb[1:]

# calcoliamo le percentuali di vittoria
perc_vittoria_mant = [100 * num_vittoria_mant[_n] / (_n+1) for _n in range(N_simul)]
perc_vittoria_camb = [100 * num_vittoria_camb[_n] / (_n+1) for _n in range(N_simul)]

plt.figure()
plt.plot(perc_vittoria_mant, label="mantenere")
plt.plot(perc_vittoria_camb, label="cambiare")
plt.xlabel("num simul")
plt.ylabel("percentuali vittoria")
plt.yticks([0, 33, 67, 100])
plt.grid(axis="y")
plt.legend(loc="best")

plt.show()


