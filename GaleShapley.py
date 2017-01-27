import scipy.io
import sys
def loadMatFile(filename):
	return scipy.io.loadmat(filename)


def main(args):
	if len(args) == 0:
		print("Expected filename")
	filename = args[0]
	mat = loadMatFile(filename)
	return


if __name__ == "__main__":
	main(sys.argv[1:])
