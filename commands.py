
#Creates a network with 2 hosts connected to one switch and one controller.
sudo mn --topo minimal

#Creates a network with one switch and k hosts
sudo mn --topo single,4

#Creates a network with k switches and k hosts. It also creates a link between each switch and
#each host and among the switches
sudo mn --topo linear,4


#Creates a network with predefined depth and fanout
sudo mn --topo tree,depth=2,fanout=2

#open mininet editor
sudo python /home/rushi/sdn/mininet/examples/miniedit.py

sudo mun -c #clears all mininet cache

h1 ping -c 3 -i 3  h2  # -c counts -i interval in sec

tcpdump -XX -n -i h2-eth0 #to listen all tcp ping message

sudo python pox.py forwarding.l2_learning

eth* denotes * port #imp note



