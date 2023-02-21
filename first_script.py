import os

cmd = 'sudo apt update && sudo apt upgrade && sudo apt install vim git qemu-guest-agent -y'
cmd2 = 'systemctl enable qemu-guest-agent && systemctl start qemu-guest-agent && systemctl status qemu-guest-agent'
os.system(cmd)
os.system(cmd2)
