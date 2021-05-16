### CI/CD (Jenkins)

I launched Jenkins on VM1 (with a static ip 192.168.31.100) and developed a simple job.
<p><img  src='images/4.png'></p>
<p><img  src='images/1.png'></p>

Then I limited the recording of a job on the server to 5 jobs (to save disk space).
<p><img  src='images/2.png'></p>
<p><img  src='images/3.png'></p>

I have installed additional Jenkins plugins such as "Locale" and "Green Balls".
<p><img  src='images/5.png'></p>
<p><img  src='images/6.png'></p>

I deployed a simple html page to the Apache web server on VM2 (with a static ip 192.168.31.101) using ssh.
<p><img  src='images/7.png'><img  src='images/8.png'></p>
<p><img  src='images/9.png'></p>
<p><img  src='images/10.png'></p>

Then I added credentials for my web server and deployed the modified html page.
<p><img  src='images/11.png'></p>
<p><img  src='images/12.png'></p>
<p><img  src='images/13.png'></p>

I connected the main branch of the repository with my web project to the integration job.
<p><img  src='images/14.png'></p>

And I made a deployment to the web server of my repository.
<p><img  src='images/16.png'></p>
To deploy the directory from GitHub, you need to use "*/**/**" where we choose which files we can integrate.
<p><img  src='images/17.png'></p>
<p><img  src='images/15.png'></p>

Because there is no way to set up a web-hook on a virtual machine, I used time checking (SCM).
<p><img  src='images/18.png'></p>
<p><img  src='images/19.png'></p>

I used VM3 (with static ip 192.168.31.99) as a slave for Jenkins.
<p><img  src='images/20.png'></p>
<p><img  src='images/21.png'></p>
<p><img  src='images/22.png'></p>
<p><img  src='images/23.png'></p>

Jenkins Slave, a slave is a Java executable that runs on a remote machine. The characteristics of the slave are: It hears requests from the Jenkins Master instance. Slaves can run on a variety of operating systems.
<p><img  src='images/24.png'></p>
<p><img  src='images/25.png'></p>
<p><img  src='images/26.png'></p>


I installed Jenkins CLI on VM1 with Jenkins and tried different authentication options.
<p><img  src='images/27.png'></p>
<p><img  src='images/28.png'></p>
<p><img  src='images/29.png'></p>
<p><img  src='images/30.png'></p>
<p><img  src='images/31.png'></p>
Then I installed Jenkins CLI on my laptop and tried remote commands for Jenkins.
<p><img  src='images/32.png'></p>

I made a backup of my job.
<p><img  src='images/33.png'></p>
<p><img  src='images/34.png'></p>

Then I created a new job from the backup.
<p><img  src='images/35.png'></p>
<p><img  src='images/36.png'></p>

I created my first pipeline and Jenkins file on a remote repository.
<p><img  src='images/37.png'></p>
<p><img  src='images/38.png'></p>
<p><img  src='images/42.png'></p>
<p><img  src='images/39.png'></p>
<p><img  src='images/40.png'></p>
<p><img  src='images/41.png'></p>