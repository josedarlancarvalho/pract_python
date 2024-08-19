import matplotlib.pyplot as plt

vendas_meses = [1224,1215,1668,1234,1342,1123,1254,1645,1607,1353,1256, 2112]
meses = ['jan', 'fev', 'mar', 'abr','mai', 'jun','jul', 'ago','set', 'out','nov', 'dez']

plt.plot(meses, vendas_meses)
plt.ylabel('vendas')
plt.xlabel('meses')
plt.axis([0,12,0,max(vendas_meses)+500])
plt.show()

