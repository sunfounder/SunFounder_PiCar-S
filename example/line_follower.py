#!/usr/bin/env python
'''
**********************************************************************
* Filename    : line_follower
* Description : An example for sensor car kit to followe line
* Author      : Dream
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Dream    2016-09-21    New release
**********************************************************************
'''

from SunFounder_Line_Follower import Line_Follower
from picar import front_wheels
from picar import back_wheels
import time


REFERENCES = [117, 113, 120, 120, 116]

forward_speed = 100
backward_speed = 70
turning_angle = 90

max_off_track_count = 40


fw = front_wheels.Front_Wheels()
bw = back_wheels.Back_Wheels()
lf = Line_Follower.Line_Follower(references=REFERENCES)

fw.ready()
bw.ready()

def straight_run():
	while True:
		bw.speed = 70
		bw.forward()
		fw.turn_straight()

def setup():

	cali()

def main():
	global turning_angle
	off_track_count = 0
	bw.speed = forward_speed

	a_step = 3
	b_step = 15
	c_step = 30
	d_step = 50
	bw.forward()
	while True:
		lt_status_now = lf.read_digital()
		print lt_status_now
		# Angle calculate
		if	lt_status_now == [0,0,1,0,0]:
			step = 0
		elif lt_status_now == [0,1,1,0,0] or lt_status_now == [0,0,1,1,0]:
			step = a_step
		elif lt_status_now == [0,1,0,0,0] or lt_status_now == [0,0,0,1,0]:
			step = b_step
		elif lt_status_now == [1,1,0,0,0] or lt_status_now == [0,0,0,1,1]:
			step = c_step
		elif lt_status_now == [1,0,0,0,0] or lt_status_now == [0,0,0,0,1]:
			step = d_step

		# Direction calculate
		if	lt_status_now == [0,0,1,0,0]:
			off_track_count = 0
			fw.turn(90)
		# turn right
		elif lt_status_now in ([0,1,1,0,0],[0,1,0,0,0],[1,1,0,0,0],[1,0,0,0,0]):
			off_track_count = 0
			turning_angle = int(90 - step)
		# turn left
		elif lt_status_now in ([0,0,1,1,0],[0,0,0,1,0],[0,0,0,1,1],[0,0,0,0,1]):
			off_track_count = 0
			turning_angle = int(90 + step)
			
		elif lt_status_now == [0,0,0,0,0]:
			off_track_count += 1
			if off_track_count > max_off_track_count:
				tmp_angle = -(turning_angle - 90) + 90
				bw.speed = backward_speed
				bw.backward()
				fw.turn(tmp_angle)
				
				lf.wait_tile_center()
				bw.stop()

				fw.turn(turning_angle)
				time.sleep(0.2)
				bw.speed = forward_speed
				bw.forward()

				

		else:
			off_track_count = 0
	
		fw.turn(turning_angle)

def cali():
	references = [0, 0, 0, 0, 0]
	print "cali for module:\n  first put all sensors on white, then put all sensors on black"
	mount = 100
	fw.turn(70)
	print "\n cali white"
	time.sleep(4)
	fw.turn(90)
	white_references = lf.get_average(mount)
	fw.turn(95)
	time.sleep(0.5)
	fw.turn(85)
	time.sleep(0.5)
	fw.turn(90)
	time.sleep(1)

	fw.turn(110)
	print "\n cali black"
	time.sleep(4)
	fw.turn(90)
	black_references = lf.get_average(mount)
	fw.turn(95)
	time.sleep(0.5)
	fw.turn(85)
	time.sleep(0.5)
	fw.turn(90)
	time.sleep(1)

	for i in range(0, 5):
		references[i] = (white_references[i] + black_references[i]) / 2
	lf.references = references
	print "Middle references =", references
	time.sleep(1)

def destroy():
	bw.stop()
	fw.turn(90)

if __name__ == '__main__':
	try:
		#setup()
		main()
		#straight_run()
	except KeyboardInterrupt:
		destroy()

