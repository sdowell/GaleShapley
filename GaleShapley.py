import scipy.io
import sys

class Matching:
	
	def __init__(self, p1, p2, spots = 1):
		self.p1 = p1
		self.p2 = p2
		self.spots = spots
		
	def match(self, profile):
		assert profile == 1 or profile == 2
		if profile == 1:
			print(self.p1.shape[0])
			return self.match1()
		elif profile == 2:
			print(self.p2.shape[1])
			return self.match2()
		
	def match1(self):
		judges = [0] * self.p1.shape[0]
		candidates = [0] * self.p1.shape[1]
		
		return
		
	def match2(self):

		return


def loadMatFile(filename):
	return scipy.io.loadmat(filename)



def main(args):
	if len(args) == 0:
		print("Expected filename")
		return
	filename = args[0]
	mat = loadMatFile(filename)
	match = Matching(mat["School_Preference"],mat["Student_Preference"])
	match.match(1)
	match.match(2)
	return


if __name__ == "__main__":
	main(sys.argv[1:])
