Installing Manually
===================================

1. Update the apt list.

.. raw:: html

    <run></run>
 
.. code-block::

    sudo apt-get update

2. Install python-smbus.

.. raw:: html

    <run></run>
 
.. code-block::

    sudo pip3 install smbus2

3. Install the PiCar module.

.. raw:: html

    <run></run>
 
.. code-block::

    cd~
    git clone --recursive https://github.com/sunfounder/SunFounder_PiCar.git
    cd SunFounder_PiCar
    python3 setup.py install

4. Enable I2C.

Edit the file /boot/config.txt

.. raw:: html

    <run></run>
 
.. code-block::

    sudo nano /boot/config.txt

The \"**#**\" in front of each line is to comment the following contents
which does not take effect in a sketch. The I2C configuration part is
commented by default too. Add the following code at the end of the file,
or delete the pound mark \"#\" at the beginning of related line; either
way will do.

.. raw:: html

    <run></run>
 
.. code-block::

    dtparam=i2c_arm=on

5. Reboot.

.. raw:: html

    <run></run>
 
.. code-block::

    sudo reboot