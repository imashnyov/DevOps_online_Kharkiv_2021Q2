 
### Networking Fundamentals

---------
#### <center>Configuring routing through 2 routers</center>
 <p><img src='images/4.4_1.gif'></p>
<p><img src='images/4.4_1.png'></p>
<p><img src='images/4.4_1_2.png'></p>

> <b>The operation of the router in the OSI model:</b> a signal arrives at the port, and the router recognizes it. The recognized signal (bits) form frames (frames). The checksum in the trailer and the recipient's MAC address are checked. If all checks are successful, the frames form a packet. At the third level, the router examines the packet header. It contains the IP address of the destination (recipient). Based on the IP address and its own routing table, the router chooses the best route for the packets to reach the destination. Having chosen the path, the router encapsulates the packet into frames, and then sends them in bits as signals to the corresponding port (selected in the routing table).


---------
#### <center>Organization of 2 subnets. Configuring DNS on servers</center>
 <p><img src='images/4.4_2.gif'></p>
<p><img src='images/4.4_2.png'></p>
<p><img src='images/4.4_2_2.png'></p>
<p><img src='images/4.4_2_3.png'></p>

> DNS is a technology that allows you to find a requested host by its domain. 