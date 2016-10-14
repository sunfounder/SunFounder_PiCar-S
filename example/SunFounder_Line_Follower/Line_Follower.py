
import smbus
import math
import time

class Line_Follower(object):
	def __init__(self, address=0x11, references=[300, 300, 300, 300, 300]):
		self.bus = smbus.SMBus(1)
		self.address = address
		self._references = references

	def read_raw(self):
		for i in range(0, 5):
			try:
				raw_result = self.bus.read_i2c_block_data(self.address, 0, 10)
				Connection_OK = True
				break
			except:
				Connection_OK = False

		if Connection_OK:
			return raw_result
		else:
			return False
			print "Error accessing %2X" % self.address

	def read_analog(self):
		raw_result = self.read_raw()
		if raw_result:
			analog_result = [0, 0, 0, 0, 0]
			for i in range(0, 5):
				high_byte = raw_result[i*2] << 8
				low_byte = raw_result[i*2+1]
				analog_result[i] = high_byte + low_byte
			return analog_result

	def read_digital(self):	
		lt = self.read_analog()
		digital_list = []
		for i in range(0, 5):
			if lt[i] > self._references[i]:
				digital_list.append(0)
			elif lt[i] < self._references[i]:
				digital_list.append(1)
			else:
				digital_list.append(-1)
		return digital_list

	def get_average(self, mount):
		if not isinstance(mount, int):
			raise ValueError("Mount must be interger")
		average = [0, 0, 0, 0, 0]
		lt_list = [[], [], [], [], []]
		for times in range(0, mount):
			lt = self.read_analog()
			for lt_id in range(0, 5):
				lt_list[lt_id].append(lt[lt_id])
		for lt_id in range(0, 5):
			average[lt_id] = int(math.fsum(lt_list[lt_id])/mount)
		return average

	def found_line_in(self, timeout):
		if isinstance(timeout, int) or isinstance(timeout, float):
			pass
		else:
			raise ValueError("timeout must be interger or float")
		time_start = time.time()
		time_during = 0
		while time_during < timeout:
			lt_status = self.read_digital()
			result = 0
			if 1 in lt_status:
				return lt_status
			time_now = time.time()
			time_during = time_now - time_start
		return False

	def wait_tile_status(self, status):
		while True:
			lt_status = self.read_digital()
			if lt_status in status:
				break

	def wait_tile_center(self):
		while True:
			lt_status = self.read_digital()
			if lt_status[2] == 1:
				break

	@property
	def references(self):
		return self._references
	
	@references.setter
	def references(self, value):
		self._references = value

if __name__ == '__main__':
	lf = Line_Follower()
	while True:
		print lf.read_analog()
