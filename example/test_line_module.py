from SunFounder_Line_Follower import Line_Follower
import time

lf = Line_Follower.Line_Follower()
while True:
	print lf.read_analog()
	time.sleep(0.5)

