### K: Tempos em s
import random
from random import randint
from random import seed
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 16})
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)

RODADAS = 500
TOTAL_CLIENTES = 50
CLIENTES_RAPIDOS = 10
CLIENTES_LENTOS = TOTAL_CLIENTES - CLIENTES_RAPIDOS
TEMPOS_CLIENTES_LENTOS = [63, 68, 72]
TEMPOS_CLIENTES_RAPIDOS = [27, 23, 21]

#TAMANHO_CNN_MNIST = 1.53 # <MB>
#L_ts = [53.2*(10**6), 51.8*(10**6), 94.0*(10**6)]  # <Mb> * [<b/s>] ### K: Velocidades medidas com o iPerf.
#L_ts = [TAMANHO_MODELO / x for x in L_ts] # [<b/s>] / b = <s>



clientes_rapidos = 12 ### 25%
x = [*range (1, 501)]; y1 = []; latencia_total = 0
for rodada in range (RODADAS):
  if (rodada < 250):
    latencia_rodada = random.choice (TEMPOS_CLIENTES_RAPIDOS * clientes_rapidos)
  else:
    latencia_rodada = random.choice (TEMPOS_CLIENTES_LENTOS * CLIENTES_LENTOS + TEMPOS_CLIENTES_RAPIDOS * clientes_rapidos)
  latencia_total += latencia_rodada
  y1.append (latencia_total)
plt.plot(x, y1, 'r-', markersize=6, label='Clientes mais rápidos primeiro (25%)')

clientes_rapidos = 25 ### 50%
x = [*range (1, 501)]; y1 = []; latencia_total = 0
for rodada in range (RODADAS):
  if (rodada < 250):
    latencia_rodada = random.choice (TEMPOS_CLIENTES_RAPIDOS * clientes_rapidos)
  else:
    latencia_rodada = random.choice (TEMPOS_CLIENTES_LENTOS * CLIENTES_LENTOS + TEMPOS_CLIENTES_RAPIDOS * clientes_rapidos)
  latencia_total += latencia_rodada
  y1.append (latencia_total)
plt.plot(x, y1, 'b-', markersize=6, label='Clientes mais rápidos primeiro (50%)')

clientes_rapidos = 37 ### 75%
x = [*range (1, 501)]; y1 = []; latencia_total = 0
for rodada in range (RODADAS):
  if (rodada < 250):
    latencia_rodada = random.choice (TEMPOS_CLIENTES_RAPIDOS * clientes_rapidos)
  else:
    latencia_rodada = random.choice (TEMPOS_CLIENTES_LENTOS * CLIENTES_LENTOS + TEMPOS_CLIENTES_RAPIDOS * clientes_rapidos)
  latencia_total += latencia_rodada
  y1.append (latencia_total)
plt.plot(x, y1, 'g-', markersize=6, label='Clientes mais rápidos primeiro (75%)')



x = [*range (1, 501)]; y2 = []; latencia_total = 0
for rodada in range (RODADAS):
  latencia_rodada = random.choice (TEMPOS_CLIENTES_LENTOS * CLIENTES_LENTOS + TEMPOS_CLIENTES_RAPIDOS * clientes_rapidos)
  latencia_total += latencia_rodada
  y2.append (latencia_total)
plt.plot(x, y2, 'k-', markersize=6, label='Latência convencional')


for var in (y1[-1], y2[-1]):
    plt.annotate('%0.2f' % int(var), xy=(1, int(var)), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')



plt.legend (loc='upper left', ncol=1, frameon=False, markerfirst=True, labelcolor='black')
#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           #ncol=2, mode="expand", borderaxespad=0.)
#plt.legend(loc='upper center', bbox_to_anchor=(1, 1))
plt.gcf().set_size_inches(10, 7)  # Adjust the figure size (width, height) to fit the legend
plt.xlabel ('Rodada')
plt.ylabel ('Latência total em segundos')
plt.xlim (0, 502)
#plt.ylim (0, 500)
plt.tight_layout()
plt.show()
#plt.savefig ('unified_monte_carlo.pdf')
print ('saved')