### Plot centralized accuracies (measured by the server)
### Just define all logs and all configs
import re
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 16})
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)

filename = 'client_accuracy_fedavg-noniid_500rounds_custom.pdf'

logfiles_2clients  = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_custom/logs_500rounds_02clients_fedavg-noniid_custom/client_main_{i}_2_clients.log" for i in range(1, 2+1)]
logfiles_5clients  = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_custom/logs_500rounds_05clients_fedavg-noniid_custom/client_main_{i}_5_clients.log" for i in range(1, 5+1)]
logfiles_10clients = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_custom/logs_500rounds_10clients_fedavg-noniid_custom/client_main_{i:02d}_10_clients.log" for i in range(1, 10+1)]
logfiles_15clients = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_custom/logs_500rounds_15clients_fedavg-noniid_custom/client_main_{i:02d}_15_clients.log" for i in range(1, 15+1)]
logfiles_25clients = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_custom/logs_500rounds_25clients_fedavg-noniid_custom/client_main_{i:02d}_25_clients.log" for i in range(1, 25+1)]
logfiles_50clients = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_custom/logs_500rounds_50clients_fedavg-noniid_custom/client_main_{i:02d}_50_clients.log" for i in range(1, 50+1)]


## plot mobilenetv2

filename = 'client_accuracy_fedavg-noniid_500rounds_mobilenetv2.pdf'
logfiles_2clients  = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_mobilenetv2_not_regularized/logs_500rounds_02clients_fedavg-noniid/client_main_{i}_2_clients.log" for i in range(1, 2+1)]
logfiles_5clients  = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_mobilenetv2_not_regularized/logs_500rounds_05clients_fedavg-noniid/client_main_{i}_5_clients.log" for i in range(1, 5+1)]
logfiles_10clients = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_mobilenetv2_not_regularized/logs_500rounds_10clients_fedavg-noniid/client_main_{i:02d}_10_clients.log" for i in range(1, 10+1)]
logfiles_15clients = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_mobilenetv2_not_regularized/logs_500rounds_15clients_fedavg-noniid/client_main_{i:02d}_15_clients.log" for i in range(1, 15+1)]
logfiles_25clients = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_mobilenetv2_not_regularized/logs_500rounds_25clients_fedavg-noniid/client_main_{i:02d}_25_clients.log" for i in range(1, 25+1)]
logfiles_50clients = [f"/mnt/Shared_Folder_With_VM/logs/Non_IID_FedAVG_500rounds_mobilenetv2_not_regularized/logs_500rounds_50clients_fedavg-noniid/client_main_{i:02d}_50_clients.log" for i in range(1, 50+1)]


configs = [
  {'label1': 'Média 2 clientes', 'label2': 'Desvio padrão 2 clientes', 'color': 'cyan',},
  {'label1': 'Média 5 clientes', 'label2': 'Desvio padrão 5 clientes', 'color': 'blue',},
  {'label1': 'Média 10 clientes', 'label2': 'Desvio padrão 10 clientes', 'color': 'red',},
  {'label1': 'Média 15 clientes', 'label2': 'Desvio padrão 15 clientes', 'color': 'green',},
  {'label1': 'Média 25 clientes', 'label2': 'Desvio padrão 25 clientes', 'color': 'black',},
  {'label1': 'Média 50 clientes', 'label2': 'Desvio padrão 50 clientes', 'color': 'purple',},
]

log_groups = [logfiles_2clients, logfiles_5clients, logfiles_10clients, logfiles_15clients, logfiles_25clients, logfiles_50clients]

for log_group, config in zip (log_groups, configs):
  accuracies=[]
  for logfile in log_group:
    # Read the log file
    with open(logfile, 'r') as file:
      log_content = file.read()

    # Regular expression pattern to match accuracy values
    accuracy_pattern = r"accuracy=(\d+\.\d+)"

    # Find all accuracy values in the log content
    accuracy_values = re.findall(accuracy_pattern, log_content)

    # Convert the accuracy values to floats and store in a list
    accuracy_list = [float(value) for value in accuracy_values]

    accuracies.append(accuracy_list)

  # Calculate mean and standard deviation across the lists
  mean_values = np.mean(accuracies, axis=0)
  std_dev = np.std(accuracies, axis=0)

  # Adjust mean and std deviation for plotting
  upper_bound = mean_values + std_dev
  lower_bound = mean_values - std_dev

  # Replace incorrect negative error bars
  upper_bound = np.where(upper_bound > 1, 1, upper_bound)
  lower_bound = np.where(lower_bound < 0, 0, lower_bound)

  # Plot
  plt.plot(np.arange(len(mean_values)), mean_values, label=config['label1'], color=config['color'])
  plt.fill_between(np.arange(len(mean_values)), lower_bound, upper_bound, color=config['color'], alpha=0.2, label=config['label2'])



plt.xlabel("Rodada", fontsize=20)
plt.ylabel("Acurácia", fontsize=20)

plt.legend (loc='lower right', bbox_to_anchor=(0,0.1,1,1), ncol=1, frameon=False, markerfirst=True, labelcolor='black')

plt.gcf().set_size_inches(12, 6)
plt.xlim (0, 501)
plt.tight_layout()
#plt.show()
plt.savefig (filename)
print ('saved')
