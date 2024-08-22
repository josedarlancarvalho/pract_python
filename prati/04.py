import matplotlib.pyplot as plt
import numpy as np 

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)

plt.plot(meses, vendas)
plt.axis([0, 50, 0, max(vendas)+200])
plt.xlabel('meses')
plt.ylabel('vendas')
plt.show()

plt.plot(meses, vendas, 'ro')
plt.axis([0, 50, 0, max(vendas)+200])
plt.xlabel('meses')
plt.ylabel('vendas')
plt.show()

plt.scatter(meses, vendas)
plt.show()

plt.bair(meses, vendas)
plt.show()