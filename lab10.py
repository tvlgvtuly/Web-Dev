import numpy as np
import matplotlib.pyplot as plt
from math import log, pi, e

def differential_entropy(sigma_squared):
    """
    Compute the differential entropy of a Gaussian random variable.
    
    Parameters:
    sigma_squared (float): Variance of the Gaussian distribution
    
    Returns:
    float: Differential entropy in nats
    """
    return 0.5 * log(2 * pi * e * sigma_squared)

def gaussian_channel_capacity(P, N0):
    """
    Compute the capacity of a Gaussian channel.
    
    Parameters:
    P (float): Signal power
    N0 (float): Noise variance
    
    Returns:
    float: Channel capacity in bits
    """
    return 0.5 * log2(1 + P/N0)

def log2(x):
    """Compute log base 2"""
    return log(x) / log(2)

# Simulation parameters
SNR_dB_range = np.arange(-10, 30, 1)  # SNR range in dB
SNR_linear_range = 10**(SNR_dB_range/10)  # Convert to linear scale
P = 1  # Fixed signal power
N0_values = P / SNR_linear_range  # Corresponding noise variances

# Compute differential entropy for X ~ N(0, P)
h_X = differential_entropy(P)
print(f"Differential entropy h(X) for X ~ N(0, {P}): {h_X:.4f} nats")

# Compute mutual information I(X;Y) and capacity for each SNR
I_XY = []
capacity = []

for N0 in N0_values:
    # Y = X + N, where X ~ N(0,P), N ~ N(0,N0)
    # So Y ~ N(0, P + N0)
    h_Y = differential_entropy(P + N0)
    
    # Conditional entropy h(Y|X) = h(N) since Y = X + N
    h_Y_given_X = differential_entropy(N0)
    
    # Mutual information I(X;Y) = h(Y) - h(Y|X)
    I_XY.append(h_Y - h_Y_given_X)
    
    # Channel capacity
    capacity.append(gaussian_channel_capacity(P, N0))

# Convert mutual information from nats to bits
I_XY_bits = [i / log(2) for i in I_XY]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(SNR_dB_range, I_XY_bits, label='Mutual Information I(X;Y) (bits)')
plt.plot(SNR_dB_range, capacity, 'r--', label='Channel Capacity (bits)')
plt.xlabel('SNR (dB)')
plt.ylabel('Bits per channel use')
plt.title('Mutual Information and Capacity of Gaussian Channel')
plt.grid(True)
plt.legend()
plt.show()