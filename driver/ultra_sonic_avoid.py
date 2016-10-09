#!/usr/bin/env python
'''
**********************************************************************
* Filename    : ultra_sonic_avoidance.py
* Description : An example for sensor car kit to followe light
* Author      : Dream
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Dream    2016-09-27    New release
**********************************************************************
'''

import ultra_sonic_module
import front_wheels
import back_wheels
import time

# D0~D7 to BCM number
D0 = 17
D1 = 18
D2 = 27
D3 = 22
D4 = 23
D5 = 24
D6 = 25
D7 = 4

ua = ultra_sonic_module.UltraSonic_Avoidance(D0)
fw = front_wheels.Front_Wheels()
bw = back_wheels.Back_Wheels()

turning_angle = 40
forward_speed = 70
backward_speed = 60

back_distance = 10
turn_distance = 20

def start_avoidance():
	print 'start_avoidance'
	fw.turn(90)
	#bw.set_speed(forward_speed)
	bw.forward()

	while True:
		distance = ua.get_distance()
		if 0<=distance<back_distance: # backward
			bw.backward()
			bw.set_speed(backward_speed)
			time.sleep(1)
		elif back_distance<distance<turn_distance : # turn
			fw.turn(90 + turning_angle)
			bw.forward()
			bw.set_speed(forward_speed)
			time.sleep(1)
		else:						# forward
			fw.turn_straight()
			bw.forward()
			bw.set_speed(forward_speed)

		print 'distance = ',distance

def stop():
	bw.stop()
	fw.turn_straight()

if __name__ == '__main__':
	try:
		start_avoidance()
	except KeyboardInterrupt:
		stop()
