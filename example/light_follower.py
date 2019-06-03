#!/usr/bin/env python
'''
**********************************************************************
* Filename    : light_follower
* Description : An example for sensor car kit to followe light
* Author      : Dream
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Dream    2016-09-20    New release
**********************************************************************
'''

from SunFounder_Light_Follower import Light_Follower
from picar import front_wheels
from picar import back_wheels
from picar import ADC
import time
import picar

picar.setup()

lf = Light_Follower.Light_Follower()
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
adc = ADC()

lf.read_analog = adc.read

gate_value = 30		# less then the normal, will act
forward_speed = 90
bw.speed = forward_speed
lt_status_last = [0,0,0]

a_step = 20
b_step = 40

FLASH_LIGHT_DELAY = 50

def calibration():
	print("calibrating.....")
	references = [0, 0, 0]
	global gate_value

	env0_list = []
	env1_list = []
	env2_list = []
	fw.turn(70)
	bw.forward()
	for times in range(1,20):
		print("calibrate %d "%times)
		A0 = lf.read_analogs()[0]
		A1 = lf.read_analogs()[1]
		A2 = lf.read_analogs()[2]

		env0_list.append(A0)
		env1_list.append(A1)
		env2_list.append(A2)
		
		time.sleep(0.5)

	references[0] = min(env0_list)
	references[1] = min(env1_list)
	references[2] = min(env2_list)

	for i in range(0,3):
		lf.references[i] = references[i] - gate_value

	fw.turn(90)
	bw.stop()
	print("calibration finished")
	print("Minimal references =", references)

def start_follower():
	print("start_follow")
	bw.speed = forward_speed

	while True:
		lt_status_now = lf.read_flashlight()
		print(lt_status_now)
		# Angle calculate
		if	lt_status_now == [0,1,0]:
			step = 0
		elif lt_status_now == [1,1,0] or lt_status_now == [0,1,1]:
			step = a_step
		elif lt_status_now == [1,0,0] or lt_status_now == [0,0,1]:
			step = b_step
		
		# Direction calculate
		if	lt_status_now in ([0,1,0],[1,1,1]):
			fw.turn(90)
			bw.forward()
			bw.speed = forward_speed
		# turn right
		elif lt_status_now in ([1,1,0],[1,0,0]):
			fw.turn(90 - step)
			bw.forward()
			bw.speed = forward_speed
		# turn left
		elif lt_status_now in ([0,1,1],[0,0,1]):
			fw.turn(90 + step)
			bw.forward()
			bw.speed = forward_speed
		# backward
		elif lt_status_now == [1,0,1]:
			fw.turn(90)
			bw.backward()
			bw.speed = forward_speed
		# none of all above
		elif lt_status_now == [0,0,0]:
			fw.turn(90)
			bw.stop()

def stop():
	bw.stop()
	fw.turn_straight()

if __name__ == '__main__':
	try:
		calibration()
		start_follower()
	except KeyboardInterrupt:
		stop()
