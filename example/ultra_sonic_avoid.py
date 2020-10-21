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

from ultrasonic_module import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import time
import picar
import random

force_turning = 0    # 0 = random direction, 1 = force left, 2 = force right, 3 = orderdly

picar.setup()

ua = Ultrasonic_Avoidance()
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45

forward_speed = 70
backward_speed = 70

back_distance = 10
turn_distance = 20

timeout = 10
last_angle = 90
last_dir = 0
def rand_dir():
	global last_angle, last_dir
	if force_turning == 0:
		_dir = random.randint(0, 1)
	elif force_turning == 3:
		_dir = not last_dir
		last_dir = _dir
		print('last dir  %s' % last_dir)
	else:
		_dir = force_turning - 1
	angle = (90 - fw.turning_max) + (_dir * 2* fw.turning_max)
	last_angle = angle
	return angle

def opposite_angle():
	global last_angle
	if last_angle < 90:
		angle = last_angle + 2* fw.turning_max
	else:
		angle = last_angle - 2* fw.turning_max
	last_angle = angle
	return angle

def start_avoidance():
	print('start_avoidance')

	count = 0
	while True:
		distance = ua.get_distance()
		print("distance: %scm" % distance)
		if distance > 0:
			count = 0
			if distance < back_distance: # backward
				print( "backward")
				fw.turn(opposite_angle())
				bw.backward()
				bw.speed = backward_speed
				time.sleep(1)
				fw.turn(opposite_angle())
				bw.forward()
				time.sleep(1)
			elif distance < turn_distance: # turn
				print("turn")
				fw.turn(rand_dir())
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
				bw.backward()
				bw.speed = forward_speed
				count += 1

def stop():
	bw.stop()
	fw.turn_straight()

if __name__ == '__main__':
	try:
		start_avoidance()
	except KeyboardInterrupt:
		stop()
