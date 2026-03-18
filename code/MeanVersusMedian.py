import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# 1. Initial Data
initial_data = [12, 12, 14, 15, 200]
num_points = len(initial_data)

# Calculate initial statistics
initial_mean = np.mean(initial_data)
initial_median = np.median(initial_data)

# 2. Set up the figure and adjust the layout to make room for 5 sliders
fig, ax = plt.subplots(figsize=(10, 6))
# Leave the bottom 45% of the window empty for the sliders
plt.subplots_adjust(bottom=0.45) 

# 3. Plot the initial data
points_plot, = ax.plot(initial_data, np.zeros_like(initial_data), 'ko', markersize=12, zorder=3)

# Plot the Mean (Red Dashed) and Median (Blue Solid)
mean_line = ax.axvline(initial_mean, color='red', linestyle='--', linewidth=2.5, zorder=2)
median_line = ax.axvline(initial_median, color='blue', linestyle='-', linewidth=2.5, zorder=2)

# Text annotations
mean_text = ax.text(initial_mean, 0.05, f'Mean: {initial_mean:.1f}', color='red', ha='center', fontweight='bold')
median_text = ax.text(initial_median, -0.05, f'Median: {initial_median:.1f}', color='blue', ha='center', fontweight='bold')

# Format the axis to look like a 1D seesaw
ax.set_xlim(0, 250)
ax.set_ylim(-0.2, 0.2)
ax.set_yticks([]) 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_position('zero')
ax.set_title("Interactive: Mean vs. Median", pad=20, fontsize=14, fontweight='bold')

# 4. Create the 5 Interactive Sliders
sliders = []
slider_axes = []

# Loop to create a vertically stacked slider for each data point
for i in range(num_points):
    # Calculate vertical position for each slider (stacking them from bottom up)
    y_pos = 0.35 - (i * 0.07)
    ax_slider = plt.axes([0.15, y_pos, 0.7, 0.03])
    
    slider = Slider(
        ax=ax_slider,
        label=f'Packet {i+1} (ms)',
        valmin=0.0,
        valmax=250.0,
        valinit=initial_data[i],
        color='gray'
    )
    sliders.append(slider)
    slider_axes.append(ax_slider)

# 5. The Update Function
def update(val):
    # Read the current value of all 5 sliders
    new_data = [slider.val for slider in sliders]
    
    # Recalculate stats
    new_mean = np.mean(new_data)
    new_median = np.median(new_data)
    
    # Update points and lines
    points_plot.set_xdata(new_data)
    mean_line.set_xdata([new_mean, new_mean])
    median_line.set_xdata([new_median, new_median])
    
    # Update text positions and values
    mean_text.set_position((new_mean, 0.05))
    mean_text.set_text(f'Mean: {new_mean:.1f}')
    
    median_text.set_position((new_median, -0.05))
    median_text.set_text(f'Median: {new_median:.1f}')
    
    fig.canvas.draw_idle()

# 6. Link all sliders to the update function
for slider in sliders:
    slider.on_changed(update)

# 7. Add a Reset Button (Optional but very helpful!)
ax_reset = plt.axes([0.8, 0.02, 0.1, 0.04])
btn_reset = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    for slider in sliders:
        slider.reset()
btn_reset.on_clicked(reset)

plt.show()