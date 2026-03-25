import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Add src to path so we can import your logic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.meta_calculator.physics_engine import keebler_equation
from src.meta_calculator.spiritual_logic import calculate_h

# 1. Prepare the Data
masses = np.linspace(0.1, 1.0, 50) # 50 points from 0.1kg to 1kg
faith_levels = [10, 50, 90] # Low, Medium, and High Spiritual Intensity
colors = ['#ff9999', '#66b3ff', '#99ff99'] # Athletic color palette

plt.figure(figsize=(10, 6))

# 2. Run Simulations for each Faith Level
for faith, color in zip(faith_levels, colors):
    h = calculate_h(faith)
    energies = [keebler_equation(m, h) for m in masses]
    plt.plot(masses, energies, label=f'Faith Level: {faith}%', color=color, linewidth=2)

# 3. Style the Graph (The "Impressive" part)
plt.title("Meta-Energy Scaling: The Keebler Equation", fontsize=16, fontweight='bold')
plt.xlabel("Physical Mass (kg)", fontsize=12)
plt.ylabel("Total Energy (Joules)", fontsize=12)
plt.yscale('log') # Log scale handles the massive numbers elegantly
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.legend()

# 4. Save the "Proof"
plt.savefig('Keebler_Energy_Graph.png')
print(" Visualization complete! 'Keebler_Energy_Graph.png' has been generated.")
