<h1 align="center"> Socket Based Backdoor and Listener</h1>

<hr>
<br>

## Project Description 🧾👨‍🏫 :- 
<hr>

The Project is mainly based on Sockets 🔌 , File Handling and subprocess library for Creating 
For Hacking 💀 into one's Computer (Any OS-Platform Service)   and listening on your computer and waiting for Connections and Running system Commands
from Your Computer to the target Computer for which Output will be Displayed On your Computer. 👏👏

<br>
<br>

## Project Features ✍✍✍ :-
<hr>

- Listeners are used to recieve the incomming Data from the Target Computer 👂
- Backdoors are Used to Execute on target Computer to send the data 📩
- Once the Connection is made you can write any command on Listener and Execute 
- Any Command Executed on listener will be executed silently in the Target Machine
- Output Will be Displayed on listener machine
- All the **Target OS Commands Can Be Executed On Listener**
- Backdoors are made **Persistent** So you Won't lose Connection Once the Computer Restarts IT WILL BE BACK!!!
- You Can Convert the python files into any target machine Executable so it's not **Suspicious**

<br>
<br>

# Usage (<i>For Testing Purposes</i>) :
<hr>

Step 1: Use Virtual Box and Install any Linux OS and bridge the wifi Adapter in network Settings
<br>
Step 2: Head to Command Line and edit execute_Listener.py and enter the IP address of Linux Machine wherever mentioned:
```
ifconfig 
```
(For getting IP address on eth0)
<br>
Step 3: Execute the execute_Listener.py file:
```
python3 execute_Listener.py
```
(remember:- listener.py should be in same directory)
<br>

Step 4: Head Over to Target Machine (Example Windows OS) and change the IP address of execute_backdoor similiar to listener's IP:
<br>

Step 5: Execute the execute_backdoor.py file:
```
python3 execute_backdoor.py
```
(remember:- reverse_backdoor.py should be in same directory)

<br>
## **AND YOU ARE SET TO GO !!!** go to the listener and execute any system commands you would like (eg : cd)

<br>
<br>
# Additional Features ⭐⭐🌟🌟🌟 :
<hr>
- USE THE Following command to download any file from target's current working directory
```
download (filename)
```

- USE THE Following command to upload any file from listener's current working directory to target's working Directory:
```
upload (filename)
```

<br>
<br>
<hr>
<h1 align="center">For Education Purpose Only. Thank you !!</h1>




