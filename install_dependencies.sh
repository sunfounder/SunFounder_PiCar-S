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
# Install RPi Car V2 Module
###################################

echo "Cloning repo \n"
cd ~
git clone --recursive https://github.com/sunfounder/SunFounder_Raspberry_Pi_Car_V2.0.git
cd SunFounder_Raspberry_Pi_Car_V2.0
echo "    Installing RPi Car module \n"
python setup.py install
cd ~/SunFounder_Smart_Sensor_Car_Kit_for_Raspberry_Pi
echo "complete\n"


###################################
# Enable I2C1 #
###################################
# Add lines to /boot/config.txt
echo "\n    Enalbe I2C \n"
egrep -v "^#|^$" /boot/config.txt > config.txt.bak  # pick up all uncomment configrations
if grep -q 'dtparam=i2c_arm=on' config.txt.bak; then  # whether i2c_arm in uncomment configrations or not
	echo 'Seem i2c_arm parameter already set, skip this step'
else
	echo 'dtparam=i2c_arm=on' >> /boot/config.txt
fi
rm config.txt.bak 	
echo "\n complete, now reboot to take effect\n"
sudo reboot

