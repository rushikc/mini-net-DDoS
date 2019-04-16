#!/usr/bin/python


from pox.core import core
from pox.lib.addresses import IPAddr
from pox.lib.addresses import EthAddr
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str, str_to_bool
from pox.lib.packet.arp import arp
from pox.lib.packet.ethernet import ethernet, ETHER_BROADCAST
import time

from pox.lib.util import dpidToStr
from pox.openflow.of_json import *
from pox.lib.revent import *  
from pox.lib.recoco import Timer  
from collections import defaultdict  
from pox.openflow.discovery import Discovery  
from pox.lib.util import dpid_to_str 

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




#fake flow:

switch9 = 0000000000000003

flow9msg = of.ofp_flow_mod()

flow9msg.cookie = 0

# flow9msg.match.in_port = 1

flow9msg.match.dl_type = 0x0800

flow9msg.match.nw_dst = IPAddr("10.0.0.7")
# flow9msg.match.nw_src = IPAddr("10.0.0.1")

# ACTIONS---------------------------------

flow9out = of.ofp_action_output (port = 7)

flow9dstIP = of.ofp_action_nw_addr.set_dst(IPAddr("10.0.0.7"))

flow9srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:04"))

flow9dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:06"))

flow9msg.actions = [flow9dstIP, flow9srcMAC, flow9dstMAC, flow9out]



#flow4:

switch10 = 0000000000000003

flow10msg = of.ofp_flow_mod()

flow10msg.cookie = 0

flow10msg.match.in_port = 6

flow10msg.match.dl_type = 0x0800

flow10msg.match.nw_src = IPAddr("10.0.0.6")
flow10msg.match.nw_dst = IPAddr("10.0.0.3")

# ACTIONS---------------------------------

flow10out = of.ofp_action_output (port = 3)

flow10srcIP = of.ofp_action_nw_addr.set_src(IPAddr("10.0.0.8"))

flow10srcMAC = of.ofp_action_dl_addr.set_src(EthAddr("00:00:00:00:00:03"))

flow10dstMAC = of.ofp_action_dl_addr.set_dst(EthAddr("00:00:00:00:00:03"))

flow10msg.actions = [flow10srcIP, flow10srcMAC, flow10dstMAC, flow10out]



ls = []
stat_dict = {}
port_to_ip={1:'10.0.0.1',2:'10.0.0.2',3:'10.0.0.3',4:'10.0.0.4',5:'10.0.0.5',6:'10.0.0.6'}
ddos_port = []
ddos_ip = []
avg = 0
rx_packets = 0
diff = 0


def install_flows():

   # log.info("    *** Installing static flows... ***")

   # Push flows to switches

   core.openflow.sendToDPID(switch2, flow2msg)
   core.openflow.sendToDPID(switch3, flow3msg)
   core.openflow.sendToDPID(switch4, flow4msg)
   core.openflow.sendToDPID(switch5, flow5msg)
   core.openflow.sendToDPID(switch6, flow6msg)
   core.openflow.sendToDPID(switch7, flow7msg)
   core.openflow.sendToDPID(switch8, flow8msg)
   core.openflow.sendToDPID(switch10, flow10msg)


 

def _handle_ConnectionUp (event):
   install_flows()




def _handle_PacketIn (event):

   dpid = event.connection.dpid
   inport = event.port
   packet = event.parsed

   if not packet.parsed:
      return

   a = packet.find('arp')   

   if not a: return

   global ddos_ip
   if str(a.protosrc) in ddos_ip :
        return


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


        e = ethernet(type=packet.type, src=r.hwsrc,dst=a.hwsrc)
        e.payload = r
        msg = of.ofp_packet_out()
        msg.data = e.pack()
        msg.actions.append(of.ofp_action_output(port = of.OFPP_IN_PORT))                            
        msg.in_port = inport
        event.connection.send(msg)




def timer_func ():
  con = core.openflow._connections
  connection = con[3]
  # connection.send(of.ofp_stats_request(body=of.ofp_flow_stats_request()))
  connection.send(of.ofp_stats_request(body=of.ofp_port_stats_request()))
  





def ddos_analyser(n1):
  global ls
  global avg

  if avg == 0:
    if len(ls) == 20:
      ls = ls[1:]
      ls.append(n1)
    else:
      ls.append(n1)

    avg = int(sum(ls)/len(ls))
  else:
    if n1 > (3*avg):
      print '\n   ..............DDoS attack detected................    \n'
      core.openflow.sendToDPID(switch9, flow9msg) # drop packets for next 't' sec
      print '\n.............Dropping packets for next 30 secs...........\n'
      ddos_mitigation(avg)
      time.sleep(30)
      print 'waking.....'
      core.openflow.sendToDPID(switch2, flow2msg) # restore regular flow

    else:

      if len(ls) == 20:
        ls = ls[1:]
        ls.append(n1)
      else:
        ls.append(n1)
      avg = int(sum(ls)/len(ls))

      print '\n********************   Normal Flow   *************************'
  print avg
  print ls



def ddos_mitigation(avg):
  global stat_dict
  global port_to_ip

  global ddos_port
  global ddos_ip

  t_port = []
  t_ip = []

  # print stat_dict
  for st1 in stat_dict.keys():
    if stat_dict[st1][1] > avg:
      ddos_port.append(st1)
      ddos_ip.append(port_to_ip[st1])
      t_port.append(st1)
      t_ip.append(port_to_ip[st1])


  for k in range(len(t_ip)):
    print "Attack is originated from ==> ",t_ip[k]
    print "Restricting access to IP ==> ",t_ip[k]




# handler to display port statistics received in JSON format
def handle_portstats_received (event):
  stats = flow_stats_to_list(event.stats)
  # st1 = stats[0]
  global rx_packets
  global diff
  global stat_dict 



  #collecting stats for all hosts
  for st1 in stats:
    if st1['port_no'] < 6 :
      pno = st1['port_no']
      if pno in stat_dict.keys():
        diff1 = st1['tx_packets']-stat_dict[pno][0]
        stat_dict[pno] = [st1['tx_packets'],diff1]
      else:
        stat_dict[pno] = [st1['tx_packets'],0]


  # print stat_dict
  # collecting stats for our server i.e port 6 (h6)
  for st1 in stats:
    if st1['port_no'] == 6:
      if rx_packets != 0:
        diff = st1['rx_packets']-rx_packets

      rx_packets = st1['rx_packets']
      if diff != 0:
        # print diff
        ddos_analyser(diff)

  


def launch ():

   core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
   core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
   # core.openflow.addListenerByName("FlowStatsReceived", 
   #  _handle_flowstats_received) 
   core.openflow.addListenerByName("PortStatsReceived", 
    handle_portstats_received) 

   # timer set to execute every five seconds
   Timer(5, timer_func, recurring=True)



