import os, sys, inspect, thread, time, json, math
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.append("/Users/kylem/Documents/LeapSDK/lib")
import Leap

class VectorDistance:

	def vector_distance(Vector v1, Vector v2):
		return math.sqrt(v1.x**2-v2.x**2 + v1.y**2-v2.y**2 + v1.z**2-v2.z**2)