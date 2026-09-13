import numpy as np
import matplotlib.pyplot as plt

# == FUNZIONI == #
def simulate_gaussian(mu, sigma, N):
    return [np.random.randn() * sigma + mu for _ in range(N)]

def infer_gaussian(data):
    return (np.mean(data), np.std(data, ddof=1))

def plot_gaussian(x_span, mu, sigma):
    return np.exp(-(x_span - mu) * (x_span - mu) / 2 / sigma / sigma) / np.sqrt(2 * np.pi * sigma * sigma)

# == PARAMETRI == #
n_gen = 1000 # numero di generazioni (oltre alla prima)
N_sample = 100 # numero di dati generati da una generazione per addestrare la generazione successiva

mu0 = 1 # media della gen 0
sigma0 = 1 # deviazione standard della gen 0

# == SIMULAZIONE == #
mu_list = [0 for _ in range(n_gen + 1)]
sigma_list = [0 for _ in range(n_gen + 1)]

mu_list[0] = mu0
sigma_list[0] = sigma0

for _n in range(n_gen):
    # simuliamo la generazione corrente
    _data = simulate_gaussian(mu_list[_n], sigma_list[_n], N_sample)
    # inferiamo la prossima generazione
    (_mu, _sigma) = infer_gaussian(_data)
    # salviamo i parametri della nuova generazione
    mu_list[_n+1] = _mu
    sigma_list[_n+1] = _sigma

# == PLOTTING == #

# andamento di mu e sigma
plt.figure()
plt.plot(mu_list, "o-", label="mu")
plt.plot(sigma_list, "s-", label="sigma")
plt.xlabel("generazione")
plt.title("parametri")
plt.legend()

# plot delle distribuzioni
x_span = np.linspace(mu0 - 5*sigma0, mu0 + 5*sigma0, 100)
plt.figure()
for _n in range(min(5, n_gen)):
    _mu = mu_list[_n]
    _sigma = sigma_list[_n]
    plt.plot(x_span, plot_gaussian(x_span, _mu, _sigma), "-", label="gen " + str(_n))
    plt.xlabel("x")

for _n in range(n_gen-5, n_gen):
    _mu = mu_list[_n]
    _sigma = sigma_list[_n]
    plt.plot(x_span, plot_gaussian(x_span, _mu, _sigma), "-", label="gen " + str(_n))
    plt.xlabel("x")

plt.title("gaussiane")
plt.legend()

plt.show()



