import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

st.title("📡 Signal Processing Visualizer")

# Sidebar controls
st.sidebar.header("Signal Controls")

signal_type = st.sidebar.selectbox(
    "Select Signal Type",
    ["Sine", "Square", "Triangle"]
)

amplitude = st.sidebar.slider("Amplitude", 1.0, 10.0, 5.0)
frequency = st.sidebar.slider("Frequency (Hz)", 1, 50, 5)
noise_level = st.sidebar.slider("Noise Level", 0.0, 2.0, 0.5)

# Time array
t = np.linspace(0, 1, 1000)

# Generate signal
if signal_type == "Sine":
    y = amplitude * np.sin(2 * np.pi * frequency * t)
elif signal_type == "Square":
    y = amplitude * signal.square(2 * np.pi * frequency * t)
elif signal_type == "Triangle":
    y = amplitude * signal.sawtooth(2 * np.pi * frequency * t, 0.5)

# Add noise
noise = noise_level * np.random.randn(len(t))
y_noisy = y + noise

# FFT
fft_vals = np.fft.fft(y_noisy)
fft_vals = np.abs(fft_vals)
freqs = np.fft.fftfreq(len(t), d=t[1] - t[0])

# ---- Plot Time Domain ----
st.subheader("📉 Time Domain Signal")

fig1, ax1 = plt.subplots()
ax1.plot(t, y_noisy, label="Noisy Signal")
ax1.plot(t, y, linestyle='dashed', label="Original Signal")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")
ax1.legend()
st.pyplot(fig1)

# ---- Plot Frequency Domain ----
st.subheader("📊 Frequency Domain (FFT)")

fig2, ax2 = plt.subplots()
ax2.plot(freqs[:len(freqs)//2], fft_vals[:len(freqs)//2])
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude")
st.pyplot(fig2)

st.success("✅ Adjust parameters from sidebar to explore signals!")
