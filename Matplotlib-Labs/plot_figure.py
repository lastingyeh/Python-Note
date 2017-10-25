import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
# y = x ** 2
y1 = 1 + x * 2
y2 = x ** 2

# 定義 figure 進行資料配置
plt.figure()
plt.plot(x, y1)

# 定義 figure 進行資料配置
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.show()
