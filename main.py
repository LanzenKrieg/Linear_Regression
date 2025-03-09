# Libraries


import matplotlib.pyplot as plt
import pandas as pd

# Function


def gradient(m_cur, b_cur, points, L):
    m_gr = 0
    b_gr = 0
    n = len(points)

    for i in range(n):
        x = points.iloc[i].x
        y = points.iloc[i].y

        m_gr += - (2 / n) * x * (y - (m_cur * x + b_cur))
        b_gr += - (2 / n) * (y - (m_cur * x + b_cur))

    m = m_cur - m_gr * L
    b = b_cur - b_gr * L
    return m, b


# Main


m = 0
b = 0
L = 0.0001
epochs = 1000
data = pd.read_csv("test.csv")

for i in range(epochs):
    if i % 100 == 0:
        print(f"Epochs: {i}")
    m, b = gradient(m, b, data, L)

print(m, b)
plt.scatter(data.x, data.y, color="black")
plt.plot(list(range(0, 105)), [m * x + b for x in range(0, 105)], color="red")
plt.show()
