!/bin/bash
apt-get update
apt-get install zsh -y
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
 
 
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
#source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
 
echo "alias la='ls -A'" >> ~/.bash_profile
echo "alias l='ls -alF'" >> ~/.bash_profile
echo "alias ll='ls -alF'" >> ~/.bash_profile
echo "alias vi='vim'" >> ~/.bash_profile
echo "alias tailf='tail -f'" >> ~/.bash_profile
cd ~
source .bash_profile
