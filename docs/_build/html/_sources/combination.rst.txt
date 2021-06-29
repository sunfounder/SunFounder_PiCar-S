Combination
===========

So, this smart car now is smart in three separate features. But, you
think only one sensor module is not enough? Try to combine those sensor
modules in one! Here we can show you an experiment - light following
with obstacle avoidance for reference.

When the car runs with the light follower, sometimes it may crash into
obstacles when following the light, and it’s not quite convenient to let
the car move back (though we've set the car to move backward if the
array is [1,0,1], it’s hard to acquire these values since the the car is
moving and the light cannot be exactly as required sometimes). So we
consider Also, you can let the car move backwards by a paper board or
your foot, which is quite easy.

Check below the program of this example.

Assemble the light follower module and ultrasonic obstacle avoidance
module on the car first.

Log into the Raspberry Pi on your computer via ssh, and get into the
directory

.. code-block::

    cd ~/SunFounder_PiCar-S/example

Run the code.

.. code-block::

    python3 light_with_obsavoidance.py

How it works
------------

Set the obstacle avoidance as a superior priority than light following:
if there is an obstacle in front of the car, it walk away from the
obstacle and back to the track; if not, then the car will keep follow
light.

Since the light following and obstacle avoidance of the car depend on
the sensor modules, we set two functions to read the status of two
sensors separately, and assign values to flags to be returned from the
functions: **state_light()**, and **state_sonic()**.

In the function **state_sonic()**, the return value is **avoid_flag**.

    If the car is **close to** an obstacle, it will return **avoid_flag =2**;

    if it is **too close to** the obstacle, it will return **avoid_flag =1**;

    if ahead **no obstacle** is detected near, it will return **avoid_flag =0**.

In the function **state_light()**, the return value is **light_flag**.

    If the light spot is **in front of** the car, it will return **light_flag = 0**;

    if the spot is **at the right side**, it will return **light_flag = 1**;

    if the spot is **at the left side**, it will return **light_flag = 2**;

    if the spot is **at the back**, it will return **light_flag = 3**;

    if **no light spot** is detected, it will return **light_flag = 4**.

The main program **main()** will run the corresponding program according
to **avoid_flag** and **light_flag**, and the **avoid_flag** is superior
in priority.

.. image:: media/image251.png


