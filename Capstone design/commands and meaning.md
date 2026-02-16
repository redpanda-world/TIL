### $ ifconfig 
This command can show us the information of internet connection like below
<img width="725" height="341" alt="image" src="https://github.com/user-attachments/assets/2eef8c08-0ae9-4a15-b0c3-de959075aa8d" />

flags=4163<UP,BROADCAST,RUNNING,MULTICAST>
Up, running: this wifi is running normally.
inet 172.30.1.20: My current wifi address. This address is changeable depending on where it is connected. 
ether: My device's (laptop or desktop...) unique number

### $ nano ~/.bashrc
nano: this means text editor.
~:this is shortcut for /home/username
.:it means fild which is followed by dot is hidden. If I save a file with dot at the very beginning, it is also treated as hidden file.
bash:this is name of file. Whenever you open terminal computer implements this file. 
rc:it stands for run commands
<img width="446" height="43" alt="image" src="https://github.com/user-attachments/assets/6ad4f62b-338f-4228-8bb4-70d8638b5952" />
export ROS_MASTER_URI: Master's address
export ROS_HOSTNAME:Advertised Master's address to nodes. when nodes want to communicate with Master, they use this information.


### source ~/.bashrc
This is just for letting computer know the change. Normally, if a file is revised, computer don't realize it until the programm restarts. This command make it does.






