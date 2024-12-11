# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:52:15 2024

@author: josea
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import OrthogonalMatchingPursuit

# Funções auxiliares
def omp(Phi, u, s):
    """Aplicação de Orthogonal Matching Pursuit (OMP)."""
    omp_model = OrthogonalMatchingPursuit(n_nonzero_coefs=s)
    omp_model.fit(Phi, u)
    return omp_model.coef_

def calculate_prd(original, reconstructed):
    """Cálculo do PRD (Percent Root-Mean-Square Difference)."""
    return np.sqrt(np.sum((original - reconstructed) ** 2) / np.sum(original ** 2)) * 100

# Parâmetros do sinal
Nppc = 128  # Número de pontos por ciclo
Nc = 12     # Número de ciclos
f = 60      # Frequência fundamental (Hz)
Fs = Nppc * f  # Frequência de amostragem
Ts = 1 / Fs     # Período de amostragem
# Vetor de tempo
#t = np.arange(0, Nppc * Nc) * Ts  # Tempo para Nppc ciclos
t = np.linspace(0, (Nppc * Nc - 1) * Ts, Nppc * Nc)  # Tempo para Nppc ciclos
# Sinal harmônico com componentes fundamentais e harmônicos ímpares
X = np.cos(2 * np.pi * f * t)  # Componente fundamental (60 Hz)

Y = np.zeros_like(X)

for i in range(3, 22, 2):  
    Y += (1 / i) * np.cos(2 * np.pi * i * f * t)

Y += X  # Sinal final

#plt.plot(Y)

# Medição da FFT original
original_fft = 2*np.abs(np.fft.fft(Y)/len(X))[:len(Y)//2]
frequencies = np.fft.fftfreq(len(Y), d=Ts)[:len(Y)//2]
#plt.figure(figsize=(14, 10))
#plt.stem(frequencies,original_fft, basefmt=" ")

# Amostragem aleatória
CR = 50
N = Nppc*Nc
M = np.round(N*(100-CR)/100).astype(int)  # Número de medições
amostras_aleatorias = np.round((len(Y)-1) * np.random.rand(M)).astype(int)
amostras_aleatorias.sort()
s = Y[amostras_aleatorias]
plt.figure(figsize=(14, 10))
plt.plot(amostras_aleatorias,s)
#plt.plot(Y)

#ale = np.random.randn(M, len(Y)) 
#Phi = np.random.randn(M, len(Y)) / np.sqrt(M)  # Matriz de medição aleatória normalizada
#u = Phi @ Y  # Sinal comprimido
Phi = np.fft.ifft(np.eye(len(X), len(X)))
CPhi = np.imag(Phi[amostras_aleatorias, :])

# Reconstrução usando OMP
#u = 50  # Número de coeficientes não nulos
reconstructed_coefficients = omp(CPhi, s, M)

# Reconstrução do sinal no domínio original
Y_reconstructed = reconstructed_coefficients  # Já no domínio original

# Medição da FFT do sinal reconstruído
#reconstructed_fft = np.abs(np.fft.fft(Y_reconstructed))[:len(Y)//2]
reconstructed_fft = np.abs(np.fft.fft(Y_reconstructed))[:len(X)//2]
plt.figure(figsize=(14, 10))
plt.plot(frequencies,reconstructed_fft)

# Cálculo do PRD
prd = calculate_prd(Y, Y_reconstructed)
print(prd)

# Plotando os sinais no domínio do tempo e da frequência
plt.figure(figsize=(14, 10))

# Subplot 1: Sinal original e reconstruído
plt.subplot(3, 1, 1)
plt.plot(t, Y, label="Sinal Original")
plt.plot(t, Y_reconstructed, label="Sinal Reconstruído", linestyle='--')
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("Sinal no Domínio do Tempo")
plt.legend()
plt.grid(True)

# Subplot 2: FFT do sinal original
plt.subplot(3, 1, 2)
plt.plot(frequencies, original_fft, label="FFT Original")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.title("Espectro de Frequência (Original)")
plt.legend()
plt.grid(True)

# Subplot 3: FFT do sinal reconstruído
plt.subplot(3, 1, 3)
plt.plot(frequencies, reconstructed_fft, label="FFT Reconstruído", color="orange")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.title("Espectro de Frequência (Reconstruído)")
plt.legend()
plt.grid(True)

print(f"PRD entre o sinal original e reconstruído: {prd:.2f}%")

plt.tight_layout()
plt.show()


