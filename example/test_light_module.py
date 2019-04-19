#from SunFounder_Light_Follower import Light_Follower
import picar

#lf = Light_Follower.Light_Follower()

adc = picar.ADC()

#lf.analog_read = adc.read

def main():
	a0 = adc.A0 
	a1 = adc.A1
	a2 = adc.A2

	#a0 = lf.analog_read(0)
	#a1 = lf.analog_read(1)
	#a2 = lf.analog_read(2)

	print("a0 = %s	a1 = %s	a2 = %s"%(a0, a1, a2))

if __name__ == '__main__':
	while True:
		main()
