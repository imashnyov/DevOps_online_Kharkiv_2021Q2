  ### Configuring DHCP, DNS servers

1. I created a new network with three VMs. VM1 has NAT and internal interfaces, VM2 and VM3 - internal only interfaces.
2. At first I configured a DHCP server in VirtualBox:
    <p><img  src='images/VB_NAT_dhcp.png'></p>
    <p><img  src='images/VB_NAT2vm_dhcp.png'></p>
    <p><img  src='images/VB_dhcp_vm1.png'></p>
    <p><img  src='images/VB_dhcp_vm2.png'></p>
    <p><img  src='images/VB_dhcp_vm3.png'></p>
    <p><img  src='images/VB_dhcp_vm1_ping.png'></p>
    <p><img  src='images/VB_dhcp_vm2_ping.png'></p>
    <p><img  src='images/VB_dhcp_vm3_ping.png'></p>
3. In the second way, I set up a DHCP server using dnsmasq on VM and two VM use like clients:
   <p><img  src='images/dnsmasq.png'></p>
   <p><img  src='images/vm1_ip.png'></p>
   <p><img  src='images/vm2_ip.png'></p>
   <p><img  src='images/vm1_dig.png'></p>
   <p><img  src='images/vm1_ping.png'></p>
   <p><img  src='images/vm2_dig.png'></p>
   <p><img  src='images/vm2_ping.png'></p>
