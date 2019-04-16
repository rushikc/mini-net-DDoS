./pox.py --verbose openflow.of_01 --port=6343 forwarding.new3


sudo ifconfig s3-eth1 192.168.1.1 netmask 255.255.255.0
sudo ifconfig s3-eth2 192.168.2.1 netmask 255.255.255.0
sudo ifconfig s3-eth3 192.168.3.1 netmask 255.255.255.0
sudo ifconfig s3-eth4 192.168.4.1 netmask 255.255.255.0
sudo ifconfig s3-eth5 192.168.5.1 netmask 255.255.255.0
sudo ifconfig s3-eth6 192.168.6.1 netmask 255.255.255.0

sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth1 target=\"192.168.236.129:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth2 target=\"192.168.236.129:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth3 target=\"192.168.236.129:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth4 target=\"192.168.236.129:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth5 target=\"192.168.236.129:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
sudo ovs-vsctl -- --id=@s create sFlow agent=s3-eth6 target=\"192.168.236.129:6343\" header=128 polling=1 -- set Bridge s3 sflow=@s
