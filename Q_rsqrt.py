import struct

def Q_rsqrt(x):
	i = struct.unpack('i', struct.pack('f', x))[0]
	i = 0x5f3759df - (i >> 1)
	y = struct.unpack('f', struct.pack('i', i))[0]
	y = y * (1.5 - (x * 0.5 * y * y))
	
	return y