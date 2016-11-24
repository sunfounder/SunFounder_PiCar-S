#from SunFounder_Light_Follower import Light_Follower
import picar

#lf = Light_Follower.Light_Follower()
adc = picar.ADC()

def main():
	a0 = adc.A0
	a1 = adc.A1
	a2 = adc.A2

	print "a0 = %s	a1 = %s	a2 = %s"%(a0, a1, a2)

if __name__ == '__main__':
	while True:
		main()
