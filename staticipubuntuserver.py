import os
import subprocess

def set_static_ip(interface):
  print("Setting static IP address...")
  ip_address = input("Enter IP address: ")
  gateway = input("Enter gateway IP address: ")
  dns = input("Enter DNS IP address: ")

  with open('/etc/netplan/00-installer-config.yaml', 'w') as file:
    file.write('network:\n')
    file.write('  version: 2\n')
    file.write('  renderer: networkd\n')
    file.write('  ethernets:\n')
    file.write(f'    {interface}:\n')
    file.write(f'      addresses:\n')
    file.write(f'        - {ip_address}/24\n')
    file.write(f'      nameservers:\n')
    file.write(f'        addresses: [{dns}]\n')
    file.write(f'      routes:\n')
    file.write(f'        - to: default\n')
    file.write(f'          via: {gateway}\n')

  os.system('sudo netplan apply')
  print("Static IP address has been set successfully!")

def get_active_interface():
  # Use subprocess to execute the "ip route" command and capture its output
  output = subprocess.check_output(['ip', 'route'])

  # Decode the output from bytes to a string
  output = output.decode('utf-8')

  # Split the output into lines and look for the line that starts with "default"
  lines = output.split('\n')
  for line in lines:
    if line.startswith('default'):
      # Extract the name of the interface from the line
      parts = line.split()
      interface = parts[4]
      return interface

  # If no interface is found, return None
  return None

def main():
  # Check if the Linux distribution is Ubuntu Server 22.04
  with open('/etc/os-release', 'r') as file:
    lines = file.readlines()
    for line in lines:
      if "VERSION_ID" in line:
        version_id = line.strip().split('=')[1].strip('"')
        if version_id == "22.04":
          print("Ubuntu Server 22.04 detected.")
          interface = get_active_interface()
          if interface is None:
            print("Unable to determine active interface.")
          else:
            print(f"Active interface: {interface}")
            answer = input("Do you want to set a static IP address? (y/n): ")
            if answer.lower() == 'y':
              set_static_ip(interface)
            else:
              print("No changes were made.")
        else:
          print("This script only works with Ubuntu Server 22.04.")

if __name__ == '__main__':
  main()
