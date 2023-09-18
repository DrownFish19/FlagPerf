'''Cluster configs'''

# Hosts to run the benchmark. Each item is an IP address or a hostname.
HOSTS = ["127.0.0.1"]

# Hosts port to run the tensorflow distribution_strategy = 'multi_worker_mirrored'
HOSTS_PORTS = ["2222"]

# Master port to connect
MASTER_PORT = "29271"

# ssh connection port
SSH_PORT = "22"
