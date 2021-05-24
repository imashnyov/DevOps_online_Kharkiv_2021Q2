### Configuration Management. Ansible.

I installed ansible on my laptop from Fedor 34. 
 <p><img  src='images/ansible_tree.png'></p>
<br>
The Host file contains the static IPs of my EC2 inputs instance:
 <p><img  src='images/ansible_hosts.png'></p>
This is how the config file for ansible looks like:
 <p><img  src='images/ansible_config.png'></p>
<br>
Variables for different servers are moved to group_vars:

For all servers:  
 <p><img  src='images/vars_all.png'></p>
For AMI Linux (Server for Jenkins):  
 <p><img  src='images/vars_jenkins.png'></p>
For AMI Ubuntu 20.04 (Server for project):  
 <p><img  src='images/vars_projservers.png'></p>
<br>
Ad-Hoc commands for my servers:
 <p><img  src='images/ad_hoc1.png'></p>
 <p><img  src='images/ad_hoc2.png'></p>
 <p><img  src='images/ad_hoc3.png'></p>
 <p><img  src='images/ad_hoc4.png'></p>

-------------------------

### Playbooks
Next, I launched my first playbook (ping servers):
 <p><img  src='images/playbook1.png'></p>
<p><a href="files/playbook1.yml">files/playbook1</a></p>
<br>
My second playbook (Apache installation on AMI Linux):
 <p><img  src='images/playbook2.png'></p>
<p><a href="files/playbook2.yml">files/playbook2</a></p>
<br>
Then I tried a playbook with a loop:
 <p><img  src='images/playbook_loop.png'></p>
 <p><a href="files/playbook_loop.yml">files/playbook_loop</a></p>
<br>
In playbook number 3, the following steps were combined and used:

 1. Check Linux distro;
 2. Install Apache Web Server on Ubuntu and AMI Linux;
 1. Start Apache and enable it during boot;
 2. Generate index.html using Jinja template;
 3. Copy dir to target server;
 4. Restart web-server (Apach) use handlers;
<p><img  src='images/playbook3.png'></p>
<p><img  src='images/playbook3_2.png'></p>
<p><a href="files/playbook3.yml">files/playbook3</a></p>
<p><img  src='images/j2_template.png'></p>
<p><a href="files/index.j2">files/index.j2</a></p>

Displaying the imported page:
<p><img  src='images/web1.png'></p>
<p><img  src='images/web2.png'></p>

Next, I experimented with encryption using Vault by HashiCorp.
<p><img  src='images/vault.png'></p>
<p><img  src='images/vault2.png'></p>

-------------------------

### Roles

I created my first role
<p><img  src='images/roles_init.png'></p>
<br>
And turned my playbook3 into a role
<p><img  src='images/roles_files.png'></p>
<p><img  src='images/roles_templates.png'></p>
<p><img  src='images/roles_default_vars.png'></p>
<p><img  src='images/roles_handlers.png'></p>
<p><img  src='images/roles_tasks.png'></p>
<br>
Created a playbook to play the role
<p><img  src='images/roles_playbook.png'></p>
<p><a href="files/playbook_for_roles.yml">files/playbook_for_roles</a></p>
<br>
I have uninstalled Apache on Linux AMI
<p><img  src='images/rm_apache_ami.png'></p>
and launched a playbook to perform the role
<p><img  src='images/roles_play.png'></p>