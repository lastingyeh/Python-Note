import matplotlib.pyplot as plt

# example1
# (2 X 2 loc) & (line1:2,line2:2 plots)

plt.figure(figsize=(6, 4))

# r2 c2 loc1
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])

# r2 c2 loc2
plt.subplot(222)
plt.plot([0, 1], [0, 2])

# r2 c2 loc3 換行
plt.subplot(223)
plt.plot([0, 1], [0, 3])

# r2 c2 loc4
plt.subplot(224)
plt.plot([0, 1], [0, 4])

# example 2
# (2 X 2 loc) & (line1:1,line2:3 plots)
plt.figure(figsize=(6, 4))
# figure splits into 2 rows, 1 col, plot to the 1st sub-fig
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])
# figure splits into 2 rows, 3 col, plot to the 4th sub-fig
plt.subplot(234)
plt.plot([0, 1], [0, 2])

plt.subplot(235)
# figure splits into 2 rows, 3 col, plot to the 5th sub-fig
plt.plot([0, 1], [0, 3])

plt.subplot(236)
# figure splits into 2 rows, 3 col, plot to the 6th sub-fig
plt.plot([0, 1], [0, 4])

plt.show()
