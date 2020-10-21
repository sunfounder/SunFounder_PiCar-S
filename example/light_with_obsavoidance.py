#!/usr/bin/env python
'''
**********************************************************************
* Filename    : light_with_obsavoidance.py
* Description : An example for sensor car kit to followe light
* Author      : Dream
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Dream    2016-10-08    New release
**********************************************************************
'''

from SunFounder_Light_Follower import Light_Follower
from ultrasonic_module import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
from picar import ADC
import time
import picar

picar.setup()

# D0~D7 to BCM number
# D0 = 17
# D1 = 18
# D2 = 27
# D3 = 22
# D4 = 23
# D5 = 24
# D6 = 25
# D7 = 4

ua = Ultrasonic_Avoidance()
lf = Light_Follower.Light_Follower()
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
adc = ADC()

lf.read_analog = adc.read

gate_value = 50		# less then the normal, will act
forward_speed = 90
lt_status_last = [0,0,0]

a_step = 20
b_step = 40

FLASH_LIGHT_DELAY = 50

turning_angle = 40
forward_speed = 70
backward_speed = 60

back_distance = 10
turn_distance = 20

def calibration():	# measure 10 times then use the minimal as reference
	print("calibrating.....")
	references = [0, 0, 0]
	global gate_value

	env0_list = []
	env1_list = []
	env2_list = []
	fw.turn(70)
	bw.forward()
	bw.speed = forward_speed

	for times in range(1,10):
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

def state_light():
	#print("start_follow")
	global step

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
			light_flag = 0
		# turn right
		elif lt_status_now in ([1,1,0],[1,0,0]):
			light_flag = 1
		# turn left
		elif lt_status_now in ([0,1,1],[0,0,1]):
			light_flag = 2
		# backward
		elif lt_status_now == [1,0,1]:
			light_flag = 3
		# none of all above
		elif lt_status_now == [0,0,0]:
			light_flag = 4

		return light_flag

def state_sonic():
	#print("start_avoidance")
	distance = ua.get_distance()
	if 0<=distance<back_distance: # backward
		avoid_flag = 2
	elif back_distance<distance<turn_distance : # turn
		avoid_flag = 1
	else:						# forward
		avoid_flag = 0

	print('distance = ',distance)
	return avoid_flag

def stop():
	bw.stop()
	fw.turn_straight()

def main():
	calibration()
	while True:
		light_flag = state_light()
		avoid_flag = state_sonic()

		# touch obstruction, backward
		if avoid_flag == 2:	
			bw.backward()
			bw.speed = backward_speed
			print(" touch obstruction")
			time.sleep(1)
			bw.stop()

		# near obstruction, turn
		elif avoid_flag == 1: 
			fw.turn(90 + turning_angle)
			bw.forward()
			bw.speed = forward_speed
			print("  near obstruction")
			time.sleep(1)
			bw.stop()

		# no obstruction, track light
		else:	
			print("   no obstruction, light_flag = ",light_flag)
			if light_flag == 0:		# direction
				fw.turn(90)
				bw.forward()
				bw.speed = forward_speed
			elif light_flag == 1:	# turn right
				fw.turn(90 - step)
				bw.forward()
				bw.speed = forward_speed
			elif light_flag == 2:	# turn left
				fw.turn(90 + step)
				bw.forward()
				bw.speed = forward_speed
			elif light_flag == 3:	# backward
				fw.turn(90)
				bw.backward()
				bw.speed = forward_speed
			elif light_flag == 4:	# stop to wait light
				fw.turn(90)
				bw.stop()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		stop()
