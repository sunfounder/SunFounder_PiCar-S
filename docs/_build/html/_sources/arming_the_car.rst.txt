Arming the Car!
===============

A car without sensor modules is unarmed just like a man without sight
and hearing, thus he has no feeling for the surrounding environment. So
what we are going to do is arm the car, allowing it to detect the
surroundings. Now let’s turn the **PiCar** into the **PiCar-S**.

What exactly is the PiCar-S? ------- We arm the PiCar with some sensors,
which endow the car with the ability to collect and process the data.
The **sensor modules** to the **PiCar** is what the **cartridges** to
the **game console**; they are added to the basic design of the game and
thus richening the play. It’s also similar to the code. The processor
will use *SunFounder_PiCar* to drive the car’s movement, and call the
corresponding code package for different modules
(**SunFounder_Light_Follower**, **SunFounder_Line_Follower**,
**SunFounder_Ultrasonic_Avoidance**).

Assemble the desired sensor module according to the wiring in
corresponding module instructions below. Have fun with **The
Transformer**!


.. image:: media/image232.png
   

.. toctree::
   :maxdepth: 2
   
   obstacle_avoidance
   light_following
   line_following
   combination