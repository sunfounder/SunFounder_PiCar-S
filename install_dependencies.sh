#!/bin/bash
#Installation


# check if sudo is used
if [ "$(id -u)" != 0 ]; then
  echo 'Sorry, you need to run this script with sudo'
  exit 1
fi

sudo apt-get update

###################################
# install i2c-tools python-smbus runtime #
###################################
    echo "\n    Installing  python-pip and django \n"

	if sudo apt-get install i2c-tools python-smbus -y;then
		echo "Successfully installed i2c-tools python-smbus \n"
	else
		echo "Failed to installed i2c-tools python-smbus"
        exit
    fi

###################################
# Enable I2C1 #
###################################
# Add lines to /boot/config.txt
echo "\n    Enalbe I2C \n"
egrep -v "^#|^$" /boot/config.txt > config.txt.bak
if grep -q 'dtparam=i2c_arm=on' config.txt.bak; then
	echo 'Seem i2c_arm parameter already set, skip this step'
else
	echo 'dtparam=i2c_arm=on' >> /boot/config.txt
fi
rm config.txt.bak 	
echo "\n complete, now reboot to take effect\n"
sudo reboot
