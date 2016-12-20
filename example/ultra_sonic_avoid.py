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

from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import time

ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(17)
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

turning_angle = 40
forward_speed = 70
backward_speed = 60

back_distance = 10
turn_distance = 20

timeout = 10

def start_avoidance():
	print 'start_avoidance'
	fw.turn(90)
	#bw.speed = forward_speed
	bw.forward()

	while True:
		distance = ua.get_distance()
		if distance > 0:
			count = 0
			if distance<back_distance: # backward
				bw.backward()
				bw.speed = backward_speed
				time.sleep(1)
			elif distance < turn_distance:                     # turn
				fw.turn(90 + turning_angle)
				bw.forward()
				bw.speed = forward_speed
				time.sleep(1)
			else:
				fw.turn_straight()
				bw.forward()
				bw.speed = forward_speed

		else:						# forward
			fw.turn_straight()
			if count > timeout:  # timeout, stop;
				bw.stop()
			else:
				bw.forward()
				bw.speed = forward_speed
				count += 1

		print 'distance = ',distance

def stop():
	bw.stop()
	fw.turn_straight()

if __name__ == '__main__':
	try:
		start_avoidance()
	except KeyboardInterrupt:
		stop()
