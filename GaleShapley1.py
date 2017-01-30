import scipy.io
import sys
import queue
import numpy


class Profile:
	def __init__(self, prof):
		print("Creating profile with " + str(len(prof)) + " choices")
		self.prefs = {}
		for p in range(0,len(prof)):
			print(str(prof[p]))
			self.prefs[p] = prof[p] - 1

class Matching:
	
	def __init__(self, p1, p2, spots = 1, quota=None):
		self.p1 = p1
		self.p2 = p2
		self.spots = spots
		self.quota = quota
		
	def match(self, profile):
		assert profile == 1 or profile == 2
		if profile == 1:
			#print(self.p1.shape[0])
			return self.match1(self.p1, self.p2, False)
		elif profile == 2:
			#print(self.p2.shape[1])
			return self.match1(self.p2.T, self.p1.T, True)
			return
		
	def match1(self, p1 , p2, trans):
		print(str(p1))
		print(str(p2))
		judges = []
		candidates = []
		choices = {}
		judgeprefs = []
		rejects = []
		numstages = 0
		done = False
		for j in range(0,p1.shape[0]):
			#print("Creating judge " + str(j))
			judges.append(queue.PriorityQueue())
			judgeprefs.append(Profile(p1[j]))
		for c in range(0,p1.shape[1]):
			candidates.append(queue.PriorityQueue())
			#print(str(c))
			for j in range(0,p1.shape[0]):
				print("Candidate " + str(c) + " ranks " + str(j) + " as " + str(p2[j][c]))
				candidates[c].put((p2[j][c]-1, j))
		while not done:
			numstages = numstages + 1
			rejects = []
			for index in range(0,len(candidates)):
				c = candidates[index]
				choices[index] = {}
				#if self.quota is not None:
				#	spots = self.quota[index]
				#else:
				#	spots = self.spots
				for s in range(0, self.spots):
					try:
						choice = c.get_nowait()
					except queue.Empty:
						continue
					print("Candidate " + str(index) + " offered to judge " + str(choice[1]) + " (preference " + str(choice[0]) + ")")
					judges[choice[1]].put((judgeprefs[choice[1]].prefs[index],index))
					choices[index][choice[1]] = choice
					#choices[index]= choice
					if not trans:
						break
			chosen = []
			print("NumStages: " + str(numstages))
			for index in range(0,len(judges)):
				j = judges[index]
				if self.quota is not None:
					spots = self.quota[index]
				else:
					spots = self.spots
				for s in range(0,spots):
					try:
						a = j.get_nowait()
						chosen.append((index,a[1]))
						#print("NumStages: " + str(numstages))
						print("[" +str(index) + " " + str(a[1]) + "]")
						#print("Judge " + str(index) + " Accepted candidate " + str(a[1]) + " (preference " + str(a[0]) + ")")
					except queue.Empty:
						pass
					if trans:
						break
				while not j.empty():
					r = j.get_nowait()
					rejects.append(r)
					print("Judge " + str(index) + " Rejected candidate " + str(r[1]) + " (preference " + str(r[0]) + ")")
			if len(rejects) == 0:
				done = True
			else:
				#print(str(chosen))
				for t in chosen:
					#print("Candidate " + str(t[1]) + " on waitlist for " + str(choices[t[1]]))
					candidates[t[1]].put(choices[t[1]][t[0]])
					#candidates[t[1]].put(choices[t[1]])
			#done = True
		return
		


def loadMatFile(filename):
	return scipy.io.loadmat(filename)

def problem2():
	p1 = numpy.asarray([[3,4,2,1],[3,1,4,2],[2,3,4,1],[3,2,1,4]])
	p2 = numpy.asarray([[1,2,3,4],[1,4,3,2],[2,1,3,4],[4,2,3,1]])
	prob2 = Matching(p1,p2.T)
	prob2.match(2)
	return
	
def problem3():
	p31 = numpy.asarray([[5,4,1,2,3],[4,5,1,3,2],[5,4,3,1,2],[4,5,3,1,2],[5,3,1,2,4]])
	p32 = numpy.asarray([[1,5,2,4,3],[4,1,2,5,3],[5,1,2,3,4],[1,2,3,5,4],[2,4,1,3,5]])
	prob3 = Matching(p31,p32.T)
	prob3.match(1)
	return
	
def problem4():
	p41 = numpy.asarray([[1,2,3],[1,3,2],[2,1,3],[3,1,2],[3,2,1]])
	p42 = numpy.asarray([[2,1,3,4,5],[3,1,2,5,4],[3,1,4,2,5]])
	prob4 = Matching(p42,p41.T)
	prob4.match(2)
	return
	
def problem5(part):
	p1 = numpy.asarray([[1,3,2,4],[1,3,4,2],[4,1,2,3]])
	p2 = numpy.asarray([[2,3,1],[2,1,3],[3,1,2],[1,3,2]])
	prob5 = Matching(p1,p2.T)
	prob5.match(1)
	
def problem6(filename):
	mat = loadMatFile(filename)
	print(str(mat))
	match = Matching(mat["School_Preference"],mat["Student_Preference"],spots=3, quota=mat["Quota"])
	print("Match 1")
	match.match(1)	
	
def main(args):
	if len(args) == 0:
		print("Expected filename")
		return
	filename = args[0]
	problem6(filename)
	return
	p41 = numpy.asarray([[1,2,3],[1,3,2],[2,1,3],[3,1,2],[3,2,1]])
	p42 = numpy.asarray([[2,1,3,4,5],[3,1,2,5,4],[3,1,4,2,5]])
	prob4 = Matching(p42,p41.T)
	prob4.match(2)
	#return
	p31 = numpy.asarray([[5,4,1,2,3],[4,5,1,3,2],[5,4,3,1,2],[4,5,3,1,2],[5,3,1,2,4]])
	p32 = numpy.asarray([[1,5,2,4,3],[4,1,2,5,3],[5,1,2,3,4],[1,2,3,5,4],[2,4,1,3,5]])
	prob3 = Matching(p31,p32.T)
	prob3.match(1)
	return
	mat = loadMatFile(filename)
	match = Matching(mat["School_Preference"],mat["Student_Preference"],spots=1)
	print("Match 1")
	match.match(1)
	#print("Match 2")
	#match.match(2)
	
	return


if __name__ == "__main__":
	main(sys.argv[1:])
