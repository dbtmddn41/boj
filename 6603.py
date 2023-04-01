import sys

class Lotto():
	def __init__(self):
		self.n = 0
		self.nums = None
	def init(self):
		inp = sys.stdin.readline().rstrip().split(' ')
		if inp[0] == '0':
			return -1
		self.n = int(inp[0])
		self.nums = inp[1:]
		return 0
	def print_nums(self, nums_srch):
		print(' '.join(map(str, nums_srch)))
	def get_lottos(self, nums_srch, start, depth):
		if depth == 6:
			self.print_nums(nums_srch)
			return
		for i in range(start, self.n):
			if self.n - i + len(nums_srch) < 6:
				continue
			nums_srch.append(self.nums[i])
			self.get_lottos(nums_srch, i+1, depth+1)
			nums_srch.pop()

L = Lotto()

notfirst = 0
while True:
	if L.init() == -1:
		break
	if notfirst:
		print()
	else:
		notfirst = 1
	L.get_lottos([], 0, 0)