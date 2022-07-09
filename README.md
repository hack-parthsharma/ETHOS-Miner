# ethos-miner-com
A little program that can be used for controlling your EthOS from serial port.
# Usage
The usage is actually very simple. You send commands by serial port.
There are commands:
1. `r` - Reboot
2. `s` - Shutdown
3. `mr` - Run Miner
4. `ms` - Stop Miner\
If all went good you will get response: `ok`
# Setting up in system
* Set Following data to the `/etc/apt/sources.list`:\
`deb http://deb.debian.org/debian/ stretch main`\
`deb-src  http://deb.debian.org/debian/ stretch main`\
`deb http://deb.debian.org/debian/ stretch-updates main`\
`deb-src  http://deb.debian.org/debian/ stretch-updates main`
* Update your packages `sudo apt-get update`
* Install Git, Python and PiP `sudo apt-get install git python python-pip`
* Install Python daemon wrapper `pip install python-daemon`
* Install ethos-miner-com `cd /opt && git clone https://github.com/hack-parthsharma/ETHOS Miner`
* Set `/opt/ethos-miner-com/main.py start` in your `/etc/profile`
* Modify the TTYSN variable to your COM port
