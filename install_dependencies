#!/bin/bash
#Installation


repo_dir=`pwd`

is_installed_python_smbus=false

function if_continue(){
    while :; do
        echo  -e "(yes/no) \c"
        read input_item
        if [ $input_item = "yes" ]; then
            break
        elif [ $input_item = "no" ]; then
            return 0
        else
            echo -e "Input error, please try again."
        fi
    done
    return 1 
}

function end(){
    print_result
    echo -e "Exiting..."
    exit
}

function print_result(){
    echo -e "Installation result:"

    echo -e "python-smbus  \c"
    if [ is_installed_python_smbus ]; then
        echo -e "Success"
    else
        echo -e "Failed"
    fi
}


# check if sudo is used
if [ "$(whoami)" != "root" ] ; then
    echo -e "You must run setup.sh as root."
    end
fi

sudo apt-get update
#sudo apt-get upgrade -y

###################################
# install python-smbus runtime #
###################################
	echo -e "\n    Installing  python-smbus \n"

	if sudo apt-get install python-smbus -y;then
		echo -e "    Successfully installed python-smbus \n"
		is_installed_python_smbus=true
	else
		echo -e "    Failed to installed python-smbus \n"
		echo -e "    Do you want to skip this? \c"
		if_continue
		if [ $? = 1 ] ; then
			echo -e "    Skipped django installation."
		else
			end
		fi
	fi

###################################
# Install RPi Car V2 Module
###################################
	echo -e "Cloning repo \n"
	cd ../
	git clone --recursive https://github.com/sunfounder/SunFounder_PiCar.git
	cd SunFounder_PiCar
	echo -e "    Installing PiCar module \n"
	sudo python3 setup.py install
	sudo python setup.py install
	cd $repo_dir
	echo -e "complete\n"


###################################
# Enable I2C1 #
###################################
# Add lines to /boot/config.txt
	echo -e "Enalbe I2C \n"
	egrep -v "^#|^$" /boot/config.txt > config.txt.temp  # pick up all uncomment configrations
	if grep -q 'dtparam=i2c_arm=on' config.txt.temp; then  # whether i2c_arm in uncomment configrations or not
	    echo -e '    Seem i2c_arm parameter already set, skip this step \n'
	else
	    echo -e '    dtparam=i2c_arm=on \n' >> /boot/config.txt
	fi
	rm config.txt.temp   
	echo -e "complete\n"

	print_result

	echo -e "The stuff you have change may need reboot to take effect."
	echo -e "Do you want to reboot immediately? \c"
	if_continue
	if [ $? = 1 ]; then
	    echo -e "Rebooting..."
	    sudo reboot
	else
	    echo -e "Exiting..."
	    exit
	fi
