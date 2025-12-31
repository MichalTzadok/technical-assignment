import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")

# Check if the image was successfully loaded
if image is None:
    print("Error: image.jpg not found")
    exit()

# Define color channels in BGR order (OpenCV reads images in BGR format)
colors = ("b", "g", "r")
histograms = []

# Compute histogram for each color channel
for i, col in enumerate(colors):
    # np.histogram returns a tuple: (histogram_values, bin_edges)
    hist = np.histogram(image[:, :, i], bins=256, range=(0, 256))
    histograms.append(hist[0])  # store only the counts
    print(f"{col.upper()} histogram:", hist[0])  # print the histogram values

# Plot histograms using matplotlib
plt.figure(figsize=(10, 5))
for hist, col in zip(histograms, colors):
    plt.plot(hist, color=col)  # plot each channel in its color
plt.title("RGB Histogram")
plt.xlabel("Pixel Value (0-255)")
plt.ylabel("Number of Pixels")
plt.show()
