# Name: Ogunsesan Abdulmalik Aderemi
# Matric-No: RUN/IFT/22/13195

import matplotlib.pyplot as pt

with_music = [304, 257, 174, 214, 69, 317, 387, 47, 157, 0, 332, 308, 317, 286, 236, 299, 206, 278, 188, 43, 0, 0, 0, 0, 0]
without_music = [292, 270, 47, 288, 324, 292, 364, 316, 287, 75, 282, 149, 274, 319, 213, 3, 324, 2, 128, 219, 94, 164, 0, 0, 0]

# Dot Plot: With Music
pt.figure(figsize=(8, 5))
pt.scatter(range(len(with_music)), with_music, color='blue', label='With Music')
pt.title("Dot Plot: With Music")
pt.xlabel("Plant Index")
pt.ylabel("Growth (mm)")
pt.legend()
pt.show()

# Dot Plot: Without Music
pt.figure(figsize=(8, 5))
pt.scatter(range(len(without_music)), without_music, color='green', label='Without Music')
pt.title("Dot Plot: Without Music")
pt.xlabel("Plant Index")
pt.ylabel("Growth (mm)")
pt.legend()
pt.show()

# Histogram: With Music
pt.figure(figsize=(8, 5))
pt.hist(with_music, bins=10, color='blue', alpha=0.7, label='With Music')
pt.title("Histogram: With Music")
pt.xlabel("Growth (mm)")
pt.ylabel("Frequency")
pt.legend()
pt.show()

# Histogram: Without Music
pt.figure(figsize=(8, 5))
pt.hist(without_music, bins=10, color='green', alpha=0.7, label='Without Music')
pt.title("Histogram: Without Music")
pt.xlabel("Growth (mm)")
pt.ylabel("Frequency")
pt.legend()
pt.show()
