#!/usr/bin/env python3

import subprocess
import os

#Checking if ZSH is installed and if not installing it

p1 = subprocess.run("zsh --version", shell=True, stderr=subprocess.DEVNULL)

value = 127

if p1.returncode == value :
    print ("ZSH is not installed. Installing ZSH next and making default SHELL:")
    install_zsh = 'sudo apt update && sudo apt install zsh -y && chsh -s $(which zsh)'
    os.system(install_zsh)
    print("ZSH is installed and is the default SHELL. Please exit ssh or your login and restart the script")
    exit()
else:
    print ("ZSH is installed, will pass on this step")

#Checking if Oh-My-Zsh is installed and if not installing it

file_path_zshrc = os.path.expanduser('~/.zshrc')
word_ohmyzsh = "export ZSH"

with open(file_path_zshrc, 'r') as file:
    # read all content of a file
    content = file.read()
    # check if string present in a file
    file.close()
    if word_ohmyzsh in content:
        print('Oh-my-zsh is installed, will pass on this step')
    else:
        print('Oh-my-zsh is not installed proceeding to installation:')
        install_ohmyzsh = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
        os.system(install_ohmyzsh)
        print('Please press "exit" so the script continues to next step')

#Check if plugins are installed if not installing it

word_ohmyzsh_plugin = "plugins=(git)"
word_ohmyzsh_new_plugin = "plugins=(git zsh-syntax-highlighting zsh-autosuggestions)"

with open(file_path_zshrc, 'r') as file:
    # read all content of a file
    content = file.read()
    # check if string present in a file
    if word_ohmyzsh_plugin in content:
        print('Installing the following oh-my-zsh plugins: ')
        content = content.replace(word_ohmyzsh_plugin, word_ohmyzsh_new_plugin)
        install_omz_highlighting = 'git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting'
        os.system(install_omz_highlighting)
        install_omz_autosuggestions = 'git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions'
        os.system(install_omz_autosuggestions)
        with open(file_path_zshrc, 'w') as file:
            file.write(content)
            file.close()
    else:
        print('The plugins are installed, passing this step')
        file.close()

#Check if Powerlevel10k is installed
        
word_ohmyzsh_theme = 'ZSH_THEME="robbyrussell"'
word_ohmyzsh_new_theme = 'ZSH_THEME="powerlevel10k/powerlevel10k"'

with open(file_path_zshrc, 'r') as file:
    # read all content of a file
    content = file.read()
    # check if string present in a file
    if word_ohmyzsh_theme in content:
        print('Installing the new powerlevel10k ')
        content = content.replace(word_ohmyzsh_theme, word_ohmyzsh_new_theme)
        install_omz_theme = 'git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k'
        os.system(install_omz_theme)
        with open(file_path_zshrc, 'w') as file:
            file.write(content)
            file.close()
    else:
        print('Powerlevel10k is installed moving to next step')
        file.close()
