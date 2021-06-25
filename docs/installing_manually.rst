Installing Manually
===================================

1. Update the apt list.

.. code-block::

    sudo apt-get update

2. Install python-smbus.

.. code-block::

    sudo apt-get install python-smbus -y

3. Install the PiCar module.

.. code-block::

    cd~
.. code-block::

    git clone --recursive https://github.com/sunfounder/SunFounder_PiCar.git
.. code-block::

    cd SunFounder_PiCar
.. code-block::

    python3 setup.py install

4. Enable I2C.

Edit the file /boot/config.txt

.. code-block::

    sudo nano /boot/config.txt

The **"#"** in front of each line is to comment the following contents
which does not take effect in a sketch. The I2C configuration part is
commented by default too. Add the following code at the end of the file,
or delete the pound mark "#" at the beginning of related line; either
way will do.

.. code-block::

    dtparam=i2c_arm=on

5. Reboot.

.. code-block::

    sudo reboot