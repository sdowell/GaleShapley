import scipy.io
import sys
import queue

class Profile:
	def __init__(self, prof):
		#print("Creating profile with " + str(len(prof)) + " choices")
		self.prefs = {}
		for p in range(0,len(prof)):
		#	print(str(prof[p]))
			self.prefs[prof[p]-1] = p

class Matching:
	
	def __init__(self, p1, p2, spots = 1):
		self.p1 = p1
		self.p2 = p2
		self.spots = spots
		
	def match(self, profile):
		assert profile == 1 or profile == 2
		if profile == 1:
			#print(self.p1.shape[0])
			return self.match1()
		elif profile == 2:
			#print(self.p2.shape[1])
			return self.match1()
		
	def match1(self):
		print(str(self.p1))
		print(str(self.p2))
		judges = []
		candidates = []
		choices = {}
		judgeprefs = []
		rejects = []
		
		done = False
		for j in range(0,self.p1.shape[0]):
			print("Creating judge " + str(j))
			judges.append(queue.PriorityQueue())
			judgeprefs.append(Profile(p1[j]))
		for c in range(0,self.p1.shape[1]):
			candidates.append(queue.PriorityQueue())
			#print(str(c))
			for j in range(0,self.p1.shape[0]):
				print("Candidate " + str(c) + " ranks " + str(self.p2[j][c]) + " as " + str(j))
				candidates[c].put((j, self.p2[j][c]-1))
		while not done:
			rejects = []
			for index in range(0,len(candidates)):
				c = candidates[index]
				try:
					choice = c.get_nowait()
				except queue.Empty:
					continue
				print("Candidate " + str(index) + " chose " + str(choice))
				judges[choice[1]].put((judgeprefs[choice[1]].prefs[index],index))
				choices[index] = choice
			chosen = []
			for j in judges:
				for s in range(0,self.spots):
					try:
						a = j.get_nowait()
						chosen.append(a)
						print("Accepted " + str(a))
					except queue.Empty:
						pass
				while not j.empty():
					r = j.get_nowait()
					rejects.append(r)
					print("Rejected " + str(r))
			if len(rejects) == 0:
				done = True
			else:
				#print(str(chosen))
				for t in chosen:
					candidates[t[1]].put(choices[t[1]])
			#done = True
		return
		
	def match2(self):
		print(str(p1))
		print(str(p2))
		judges = []
		candidates = []
		choices = {}
		judgeprefs = []
		rejects = []
		
		done = False
		for j in range(0,p1.shape[0]):
			print("Creating judge " + str(j))
			judges.append(queue.PriorityQueue())
			judgeprefs.append(Profile(p1[j]))
		for c in range(0,p1.shape[1]):
			candidates.append(queue.PriorityQueue())
			#print(str(c))
			for j in range(0,p1.shape[0]):
				print("Candidate " + str(c) + " ranks " + str(p2[j][c]) + " as " + str(j))
				candidates[c].put((j, p2[j][c]-1))
		while not done:
			rejects = []
			for index in range(0,len(candidates)):
				c = candidates[index]
				try:
					choice = c.get_nowait()
				except queue.Empty:
					continue
				print("Candidate " + str(index) + " chose " + str(choice))
				judges[choice[1]].put((judgeprefs[choice[1]].prefs[index],index))
				choices[index] = choice
			chosen = []
			for j in judges:
				for s in range(0,self.spots):
					try:
						a = j.get_nowait()
						chosen.append(a)
						print("Accepted " + str(a))
					except queue.Empty:
						pass
				while not j.empty():
					r = j.get_nowait()
					rejects.append(r)
					print("Rejected " + str(r))
			if len(rejects) == 0:
				done = True
			else:
				#print(str(chosen))
				for t in chosen:
					candidates[t[1]].put(choices[t[1]])
			#done = True
		return


def loadMatFile(filename):
	return scipy.io.loadmat(filename)



def main(args):
	if len(args) == 0:
		print("Expected filename")
		return
	filename = args[0]
	mat = loadMatFile(filename)
	match = Matching(mat["School_Preference"],mat["Student_Preference"],spots=1)
	print("Match 1")
	match.match(1)
	print("Match 2")
	match.match(2)
	return


if __name__ == "__main__":
	main(sys.argv[1:])
