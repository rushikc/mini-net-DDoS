#!/usr/bin/python


from pox.core import core

from pox.lib.addresses import IPAddr

from pox.lib.addresses import EthAddr

import pox.openflow.libopenflow_01 as of

from pox.lib.util import dpid_to_str, str_to_bool

from pox.lib.packet.arp import arp

from pox.lib.packet.ethernet import ethernet, ETHER_BROADCAST

 

log = core.getLogger()

 

#flow3:

switch2 = 0000000000000003

flow2msg = of.ofp_flow_mod()

flow2msg.cookie = 0

# flow2msg.match.in_port = 1

flow2msg.match.dl_type = 0x0800

flow2msg.match.nw_dst = IPAddr("10.0.0.7")
# flow2msg.match.nw_src = IPAddr("10.0.0.1")

# ACTIONS---------------------------------

flow2out = of.ofp_action_output (port = 6)

flow2dstIP = of.ofp_action_nw_addr.set_dst(IPAddr("10.0.0.6"))

flow2srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:04"))

flow2dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:06"))

flow2msg.actions = [flow2dstIP, flow2srcMAC, flow2dstMAC, flow2out]

 

#flow4:

switch3 = 0000000000000003

flow3msg = of.ofp_flow_mod()

flow3msg.cookie = 0

flow3msg.match.in_port = 6

flow3msg.match.dl_type = 0x0800

flow3msg.match.nw_src = IPAddr("10.0.0.6")
flow3msg.match.nw_dst = IPAddr("10.0.0.1")

# ACTIONS---------------------------------

flow3out = of.ofp_action_output (port = 1)

flow3srcIP = of.ofp_action_nw_addr.set_src(IPAddr("10.0.0.7"))

flow3srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:03"))

flow3dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:01"))

flow3msg.actions = [flow3srcIP, flow3srcMAC, flow3dstMAC, flow3out]


#flow4:

switch4 = 0000000000000003

flow4msg = of.ofp_flow_mod()

flow4msg.cookie = 0

flow4msg.match.in_port = 6

flow4msg.match.dl_type = 0x0800

flow4msg.match.nw_src = IPAddr("10.0.0.6")
flow4msg.match.nw_dst = IPAddr("10.0.0.2")

# ACTIONS---------------------------------

flow4out = of.ofp_action_output (port = 2)

flow4srcIP = of.ofp_action_nw_addr.set_src(IPAddr("10.0.0.7"))

flow4srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:03"))

flow4dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:02"))

flow4msg.actions = [flow4srcIP, flow4srcMAC, flow4dstMAC, flow4out]

 
#flow4:

switch5 = 0000000000000003

flow5msg = of.ofp_flow_mod()

flow5msg.cookie = 0

flow5msg.match.in_port = 6

flow5msg.match.dl_type = 0x0800

flow5msg.match.nw_src = IPAddr("10.0.0.6")
flow5msg.match.nw_dst = IPAddr("10.0.0.3")

# ACTIONS---------------------------------

flow5out = of.ofp_action_output (port = 3)

flow5srcIP = of.ofp_action_nw_addr.set_src(IPAddr("10.0.0.7"))

flow5srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:03"))

flow5dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:03"))

flow5msg.actions = [flow5srcIP, flow5srcMAC, flow5dstMAC, flow5out]



#flow4:

switch6 = 0000000000000003

flow6msg = of.ofp_flow_mod()

flow6msg.cookie = 0

flow6msg.match.in_port = 6

flow6msg.match.dl_type = 0x0800

flow6msg.match.nw_src = IPAddr("10.0.0.6")
flow6msg.match.nw_dst = IPAddr("10.0.0.4")

# ACTIONS---------------------------------

flow6out = of.ofp_action_output (port = 4)

flow6srcIP = of.ofp_action_nw_addr.set_src(IPAddr("10.0.0.7"))

flow6srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:03"))

flow6dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:04"))

flow6msg.actions = [flow6srcIP, flow6srcMAC, flow6dstMAC, flow6out]

#flow4:

switch7 = 0000000000000003

flow7msg = of.ofp_flow_mod()

flow7msg.cookie = 0

flow7msg.match.in_port = 6

flow7msg.match.dl_type = 0x0800

flow7msg.match.nw_src = IPAddr("10.0.0.6")
flow7msg.match.nw_dst = IPAddr("10.0.0.5")

# ACTIONS---------------------------------

flow7out = of.ofp_action_output (port = 5)

flow7srcIP = of.ofp_action_nw_addr.set_src(IPAddr("10.0.0.7"))

flow7srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:03"))

flow7dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:05"))

flow7msg.actions = [flow7srcIP, flow7srcMAC, flow7dstMAC, flow7out]


#flow4:

switch8 = 0000000000000003

flow8msg = of.ofp_flow_mod()

flow8msg.cookie = 0

flow8msg.match.in_port = 6

flow8msg.match.dl_type = 0x0800

flow8msg.match.nw_src = IPAddr("10.0.0.6")
flow8msg.match.nw_dst = IPAddr("10.0.0.6")

# ACTIONS---------------------------------

flow8out = of.ofp_action_output (port = 6)

flow8srcIP = of.ofp_action_nw_addr.set_src(IPAddr("10.0.0.7"))

flow8srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:03"))

flow8dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:06"))

flow8msg.actions = [flow8srcIP, flow8srcMAC, flow8dstMAC, flow8out]



def install_flows():

   log.info("    *** Installing static flows... ***")

   # Push flows to switches

   core.openflow.sendToDPID(switch2, flow2msg)

   core.openflow.sendToDPID(switch3, flow3msg)
   core.openflow.sendToDPID(switch4, flow4msg)
   core.openflow.sendToDPID(switch5, flow5msg)
   core.openflow.sendToDPID(switch6, flow6msg)
   core.openflow.sendToDPID(switch7, flow7msg)
   core.openflow.sendToDPID(switch8, flow8msg)

   log.info("    *** Static flows installed. ***")

 

def _handle_ConnectionUp (event):

   log.info("*** install flows ***")

   install_flows()

 

def _handle_PacketIn (event):

   #log.info("*** _handle_PacketIn... ***")

   dpid = event.connection.dpid

   inport = event.port

   packet = event.parsed

   if not packet.parsed:

      log.warning("%i %i ignoring unparsed packet", dpid, inport)

      return

 

   a = packet.find('arp')

   if not a: return

 

   log.info("%s ARP %s %s => %s", dpid_to_str(dpid),

      {arp.REQUEST:"request",arp.REPLY:"reply"}.get(a.opcode,

      'op:%i' % (a.opcode,)), str(a.protosrc), str(a.protodst))

    

   if a.prototype == arp.PROTO_TYPE_IP:

     if a.hwtype == arp.HW_TYPE_ETHERNET:

       if a.opcode == arp.REQUEST:

        r = arp()

        r.hwtype = a.hwtype

        r.prototype = a.prototype

        r.hwlen = a.hwlen

        r.protolen = a.protolen

        r.opcode = arp.REPLY

        r.hwdst = a.hwsrc

        r.protodst = a.protosrc

        r.protosrc = a.protodst

        if str(a.protodst)=="10.0.0.1":

          r.hwsrc = EthAddr("00:00:00:00:00:03")

        if str(a.protodst)=="10.0.0.7":

          r.hwsrc = EthAddr("00:00:00:00:00:04")

        e = ethernet(type=packet.type, src=r.hwsrc,

                        dst=a.hwsrc)

        e.payload = r

        log.info("%s answering ARP for %s" % (dpid_to_str(dpid),

            str(r.protosrc)))

        msg = of.ofp_packet_out()

        msg.data = e.pack()

        msg.actions.append(of.ofp_action_output(port =

                                                of.OFPP_IN_PORT))                            

        msg.in_port = inport

        event.connection.send(msg)

 

def launch ():

   log.info("*** Starting... ***")

   log.info("*** Waiting for switches to connect.. ***")

   core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)

   core.openflow.addListenerByName("PacketIn", _handle_PacketIn)