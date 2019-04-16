
#Creates a network with 2 hosts connected to one switch and one controller.
sudo mn --topo minimal

#Creates a network with one switch and k hosts
sudo mn --topo single,4

#Creates a network with k switches and k hosts. It also creates a link between each switch and
#each host and among the switches
sudo mn --topo linear,4


#Creates a network with predefined depth and fanout
sudo mn --topo tree,depth=2,fanout=2

git add -A && git commit -m "updated" && git push



./pox.py --verbose openflow.of_01 --port=6343 forwarding.l2_learning

./pox.py --verbose openflow.of_01 --port=6343 forwarding.new3


#flow stats
https://github.com/hip2b2/poxstuff/blob/master/flow_stats.py

ITGSend -a <ip_of_h2> -T UDP -C <rate> -c <packet_size>
ITGSend -a 10.0.0.7 -T UDP -C 10 -c 12



sudo mun -c #clears all mininet cache

h1 ping -c 3 -i 3  h2  # -c counts -i interval in sec

tcpdump -XX -n -i h2-eth0 #to listen all tcp ping message




sudo ifconfig s3-eth1 172.16.1.1 netmask 255.255.255.0
sudo ifconfig s3-eth2 172.16.2.1 netmask 255.255.255.0
sudo ifconfig s3-eth3 172.16.3.1 netmask 255.255.255.0
sudo ifconfig s3-eth4 172.16.4.1 netmask 255.255.255.0
sudo ifconfig s3-eth5 172.16.5.1 netmask 255.255.255.0
sudo ifconfig s3-eth6 172.16.6.1 netmask 255.255.255.0
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth1 target=\"172.16.104.128:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth2 target=\"172.16.104.128:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth3 target=\"172.16.104.128:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth4 target=\"172.16.104.128:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth5 target=\"172.16.104.128:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth6 target=\"172.16.104.128:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s


sudo ifconfig s3-eth1 172.16.1.1 netmask 255.255.255.0
sudo ifconfig s3-eth2 172.16.2.1 netmask 255.255.255.0
sudo ifconfig s3-eth3 172.16.3.1 netmask 255.255.255.0
sudo ifconfig s3-eth4 172.16.4.1 netmask 255.255.255.0
sudo ifconfig s3-eth5 172.16.5.1 netmask 255.255.255.0
sudo ifconfig s3-eth6 172.16.6.1 netmask 255.255.255.0
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth1 target=\"172.16.104.128:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth2 target=\"172.16.104.128:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth3 target=\"172.16.104.128:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth4 target=\"172.16.104.128:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth5 target=\"172.16.104.128:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth6 target=\"172.16.104.128:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s





./pox.py --verbose openflow.of_01 --port=6343 forwarding.new3





sudo ifconfig s3-eth1 192.168.1.1 netmask 255.255.255.0
sudo ifconfig s3-eth2 192.168.2.1 netmask 255.255.255.0
sudo ifconfig s3-eth3 192.168.3.1 netmask 255.255.255.0
sudo ifconfig s3-eth4 192.168.4.1 netmask 255.255.255.0
sudo ifconfig s3-eth5 192.168.5.1 netmask 255.255.255.0
sudo ifconfig s3-eth6 192.168.6.1 netmask 255.255.255.0





sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth1 target=\"192.168.236.129:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth2 target=\"192.168.236.129:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth3 target=\"192.168.236.129:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth4 target=\"192.168.236.129:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth5 target=\"192.168.236.129:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth6 target=\"192.168.236.129:6343\" header=128 polling=10 -- set Bridge s3 sflow=@s

