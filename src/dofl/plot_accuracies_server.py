### Plot centralized accuracies (measured by the server)
import re
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 16})
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)

first_logfiles = [
  'logs_plot/6-6-25.log',
  'logs_plot/12-12-25.log',
  'logs_plot/19-19-25.log',
]
second_logfiles = [
  'logs_plot/6-25-25.log',
  'logs_plot/12-25-25.log',
  'logs_plot/19-25-25.log',
]
labels = [
  'Clientes com mais dados primeiro (25%)',
  'Clientes com mais dados primeiro (50%)',
  'Clientes com mais dados primeiro (75%)',
]

all_clients = 'logs_plot/25-25-25.log'

for first_logfile, second_logfile, label in zip(first_logfiles, second_logfiles, labels):
  # Read the log file
  with open(first_logfile, 'r') as file:
    log_content = file.read()

  # Regular expression pattern to match accuracy values
  accuracy_pattern = r"'accuracy': (\d+\.\d+)"

  # Find all accuracy values in the log content
  accuracy_values = re.findall(accuracy_pattern, log_content)

  # Convert the accuracy values to floats and store in a list
  accuracy_list1 = [float(value) for value in accuracy_values]

  with open(second_logfile, 'r') as file2:
    log_content = file2.read()

  # Regular expression pattern to match accuracy values
  accuracy_pattern = r"'accuracy': (\d+\.\d+)"

  # Find all accuracy values in the log content
  accuracy_values = re.findall(accuracy_pattern, log_content)

  # Convert the accuracy values to floats and store in a list
  accuracy_list2 = [float(value) for value in accuracy_values]


  accuracy_list = accuracy_list1[:250] + accuracy_list2[:250]
  x = list(range(1, len(accuracy_list)+ 1))
  plt.plot(x, accuracy_list, label=label, marker='', alpha=0.8)


### Plot all 25 clients (regular fedavg)
with open(all_clients, 'r') as file:
  log_content = file.read()

# Regular expression pattern to match accuracy values
accuracy_pattern = r"'accuracy': (\d+\.\d+)"

# Find all accuracy values in the log content
accuracy_values = re.findall(accuracy_pattern, log_content)

# Convert the accuracy values to floats and store in a list
accuracy_list = [float(value) for value in accuracy_values]

x = list(range(1, len(accuracy_list)+ 1))
plt.plot(x, accuracy_list, label='FedAVG (25 clientes)', marker='.', color='k', alpha=0.3)


plt.xlabel("Rodada")
plt.ylabel("Acurácia")

plt.legend (loc='lower right', ncol=1, frameon=False, markerfirst=True, labelcolor='black')
plt.xlim (0, 501)
plt.gcf().set_size_inches(12, 6)  # Adjust the figure size (width, height) to fit the legend
plt.tight_layout()
#plt.show()
plt.savefig ('server_accuracy_dofl_500rounds_custom_mnist.pdf')
print ('saved')
