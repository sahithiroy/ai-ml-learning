# Linux

## 1. What is Linux?
Linux is an open-source operating system kernel used in desktops, servers, cloud systems, and embedded devices. It is the foundation of many systems such as Ubuntu, Debian, Fedora, and CentOS.

### Why Linux is important
- Stable and secure
- Used heavily in servers and DevOps
- Preferred for data science, AI/ML, and cloud computing
- Powerful command-line interface

### Example
- A developer uses Linux to run Python, Docker, and ML models on a server.
- A data scientist uses Linux to process large datasets efficiently.

---

## 2. Linux File System
Linux organizes files in a tree-like structure starting from the root directory `/`.

### Common directories
- `/home` – user files
- `/etc` – system configuration files
- `/var` – logs and variable data
- `/usr` – installed software
- `/tmp` – temporary files
- `/root` – administrator’s home directory

### Example
- Your personal files are usually under `/home/yourname`.
- System settings are stored in `/etc`.

---

## 3. Basic Commands
These are common commands used daily in Linux.

### Essential commands
- `pwd` – print working directory
- `ls` – list files and folders
- `cd` – change directory
- `mkdir` – create directory
- `rmdir` – remove empty directory
- `touch` – create an empty file
- `cp` – copy files
- `mv` – move or rename files
- `rm` – remove files
- `clear` – clear terminal screen

### Example
```bash
pwd
ls
cd /home/user
mkdir projects
```

---

## 4. File Management
File management includes creating, editing, viewing, copying, moving, and deleting files.

### Useful commands
- `cat filename` – view file content
- `less filename` – view file page by page
- `nano filename` – edit a file
- `cp source destination` – copy a file
- `mv old new` – rename or move a file
- `rm filename` – delete a file
- `find /path -name filename` – find a file

### Example
```bash
cat notes.txt
nano app.py
cp app.py backup.py
```

---

## 5. Permissions
Linux uses permissions to control who can read, write, or execute files.

### Permission types
- `r` – read
- `w` – write
- `x` – execute

### Common commands
- `chmod` – change permissions
- `chown` – change ownership

### Example
```bash
chmod +x script.sh
chmod 755 script.sh
```

### Example scenario
- A script should be executable, so you give it permission with `chmod +x`.

---

## 6. Process Management
Process management helps you monitor and control running programs.

### Useful commands
- `ps` – show running processes
- `top` – view system processes live
- `kill` – stop a process
- `killall` – stop all processes by name
- `jobs` – view background jobs

### Example
```bash
ps -ef
top
kill 1234
```

### Example scenario
- A Python script is hanging, so you identify its process and stop it with `kill`.

---

## 7. Networking Commands
Networking commands help you check connectivity and configure network access.

### Useful commands
- `ping` – test connectivity
- `ifconfig` / `ip addr` – show IP address
- `netstat` – show network connections
- `curl` – transfer data from URLs
- `wget` – download files from the internet

### Example
```bash
ping google.com
ip addr
curl https://example.com
```

### Example scenario
- You want to verify that your server can reach the internet.

---

## 8. Package Management
Package managers install, update, and remove software.

### Debian/Ubuntu
- `apt update`
- `apt install package_name`
- `apt remove package_name`

### Red Hat/CentOS/Fedora
- `yum install package_name`
- `dnf install package_name`

### Example
```bash
sudo apt update
sudo apt install python3-pip
```

### Example scenario
- You need to install Git, Python, or Docker on a Linux machine.

---

## 9. SSH
SSH (Secure Shell) allows secure remote access to another machine.

### Common command
```bash
ssh username@hostname
```

### Example
```bash
ssh user@192.168.1.10
```

### Why SSH is important
- Secure remote login
- Used for servers and cloud machines
- Useful for managing systems remotely

### Example scenario
- A developer connects to a remote server to deploy an application.

---

## 10. Environment Variables
Environment variables store values used by the shell and programs.

### Useful commands
- `echo $VAR_NAME` – display variable
- `export VAR_NAME=value` – set variable
- `env` – show all environment variables

### Example
```bash
echo $HOME
export PATH=$PATH:/my/bin
env
```

### Example scenario
- You set a Python or Java path for the current shell session.

---

## 11. Shell Scripting Basics
A shell script is a file containing commands that the shell runs one by one.

### Example script
```bash
#!/bin/bash
echo "Hello, Linux!"
mkdir -p myfolder
```

### Make it executable
```bash
chmod +x script.sh
./script.sh
```

### Why shell scripting is useful
- Automates repetitive tasks
- Saves time
- Useful for DevOps and data workflows

---

## 12. Linux for Data Science & AI/ML
Linux is widely used in data science and AI/ML because it supports powerful tools and large-scale computation.

### Common tools
- Python
- Jupyter Notebook
- Conda / Virtualenv
- Docker
- Git
- GPU libraries such as CUDA

### Why Linux is preferred
- Faster performance on servers
- Better support for Python environments
- Easy integration with cloud platforms

### Example scenario
- A data scientist trains a machine learning model on a Linux server using Python and GPU.

---

## 13. Top 50 Linux Commands
Here is a practical list of commonly used Linux commands.

1. `pwd`
2. `ls`
3. `cd`
4. `mkdir`
5. `rmdir`
6. `touch`
7. `cp`
8. `mv`
9. `rm`
10. `cat`
11. `less`
12. `more`
13. `nano`
14. `vim`
15. `grep`
16. `find`
17. `tar`
18. `gzip`
19. `gunzip`
20. `chmod`
21. `chown`
22. `ps`
23. `top`
24. `kill`
25. `killall`
26. `jobs`
27. `ping`
28. `ip`
29. `curl`
30. `wget`
31. `ssh`
32. `scp`
33. `df`
34. `du`
35. `free`
36. `uname`
37. `whoami`
38. `hostname`
39. `history`
40. `echo`
41. `export`
42. `env`
43. `apt`
44. `yum`
45. `dnf`
46. `sudo`
47. `man`
48. `help`
49. `alias`
50. `exit`

---

## 14. Interview Questions
Here are some common Linux interview questions.

### Basic questions
- What is the difference between Linux and Unix?
- What is the root directory in Linux?
- What is the use of the `pwd` command?
- What is the difference between `cp` and `mv`?

### Intermediate questions
- What is the difference between `chmod` and `chown`?
- How do you find a file in Linux?
- What is the purpose of `grep`?
- What is a process in Linux?

### Advanced questions
- What is SSH and why is it used?
- How do environment variables work in Linux?
- What is the difference between `apt` and `yum`?
- What is a shell script and how is it executed?

### Example answer
- A shell script is a file containing commands that the shell executes sequentially to automate tasks.
