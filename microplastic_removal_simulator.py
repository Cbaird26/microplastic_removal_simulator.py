import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants
initial_health = 70  # Initial health score out of 100
initial_microplastic_load = 50  # Initial microplastic load out of 100
time_steps = st.slider("Time Steps (months)", 1, 120, 60)

# Define intervention effectiveness
nanobot_effectiveness = st.slider("Nanobot Effectiveness (%)", 0, 100, 50)
enzyme_effectiveness = st.slider("Engineered Enzyme Effectiveness (%)", 0, 100, 50)
detox_therapy_effectiveness = st.slider("Detox Therapy Effectiveness (%)", 0, 100, 50)

# Simulate the effect of interventions
def simulate_interventions(initial_health, initial_microplastic_load, nanobot_eff, enzyme_eff, detox_eff, time_steps):
    health = initial_health
    microplastic_load = initial_microplastic_load
    health_over_time = []
    microplastics_over_time = []

    for t in range(time_steps):
        microplastic_load -= (nanobot_eff + enzyme_eff + detox_eff) / 3  # Combined effect of interventions
        microplastic_load = max(microplastic_load, 0)  # Ensure microplastic load doesn't go below 0
        
        health += (100 - health) * (nanobot_eff + enzyme_eff + detox_eff) / 300  # Health improvement
        health = min(health, 100)  # Ensure health doesn't exceed 100
        
        health_over_time.append(health)
        microplastics_over_time.append(microplastic_load)
    
    return health_over_time, microplastics_over_time

# Run the simulation
health_over_time, microplastics_over_time = simulate_interventions(initial_health, initial_microplastic_load, nanobot_effectiveness, enzyme_effectiveness, detox_therapy_effectiveness, time_steps)

# Plot the results
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(range(time_steps), health_over_time, label="Health")
plt.xlabel("Time (months)")
plt.ylabel("Health")
plt.title("Health Over Time")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(range(time_steps), microplastics_over_time, label="Microplastic Load", color='r')
plt.xlabel("Time (months)")
plt.ylabel("Microplastic Load")
plt.title("Microplastic Load Over Time")
plt.legend()
plt.grid(True)

st.pyplot(plt)

# Display the results
st.write(f"Initial Health: {initial_health}")
st.write(f"Initial Microplastic Load: {initial_microplastic_load}")
st.write(f"Nanobot Effectiveness: {nanobot_effectiveness}%")
st.write(f"Engineered Enzyme Effectiveness: {enzyme_effectiveness}%")
st.write(f"Detox Therapy Effectiveness: {detox_therapy_effectiveness}%")
st.write(f"Simulated Time: {time_steps} months")
