#!/usr/bin/python



from mininet.net import Mininet

from mininet.node import Controller, RemoteController, OVSKernelSwitch, IVSSwitch, UserSwitch

from mininet.link import Link, TCLink

from mininet.cli import CLI

from mininet.log import setLogLevel

 

def topology():

 

    "Create a network."

    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

 

    print "*** Creating nodes"

    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/24' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:03', ip='10.0.0.3/24' )
    h4 = net.addHost( 'h4', mac='00:00:00:00:00:04', ip='10.0.0.4/24' )
    h5 = net.addHost( 'h5', mac='00:00:00:00:00:05', ip='10.0.0.5/24' )
    h6 = net.addHost( 'h6', mac='00:00:00:00:00:06', ip='10.0.0.6/24' )

    s3 = net.addSwitch( 's3', protocols='OpenFlow10', listenPort=6673)
    s2 = net.addSwitch( 's2', protocols='OpenFlow10', listenPort=6672)
    s1 = net.addSwitch( 's1', protocols='OpenFlow10', listenPort=6671)

    c4 = net.addController( 'c4', ip='127.0.0.1', port=6633 )

 

    print "*** Creating links"
    # net.addLink(s1, s2)
    # net.addLink(s2, s3)
    net.addLink(h1, s3)
    net.addLink(h2, s3)
    net.addLink(h3, s3)
    net.addLink(h4, s3)
    net.addLink(h5, s3)
    net.addLink(h6, s3)

    print "*** Starting network"

    net.build()

    c4.start()

    s3.start( [c4] )
    s2.start( [c4] )
    s1.start( [c4] )

 

    print "*** Running CLI"

    h2.cmd("ip route add default via 192.168.1.1 dev h2-eth0")

    h1.cmd("ip route add default via 10.0.0.2 dev h1-eth0")

    CLI( net )

 

    print "*** Stopping network"

    net.stop()

 

if __name__ == '__main__':

    setLogLevel( 'info' )

    topology()