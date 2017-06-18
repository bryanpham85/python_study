class LogicGate:
	def __init__(self, n):
		self.lable = n
		self.output = None

	def getLable(self):
		return self.lable

	def getOutput(self):
		print("hereGetOutPut")
		self.output = self.performGateLogic()
		print("after perform")
		return self.output


class BinaryGate(LogicGate):

	def __init__(self, n):
		LogicGate.__init__(self, n)
		self.pinA = None
		self.pinB = None

	def getPinA(self):
		return int(input("Enter Pin A for Gate " + self.getLable() + "-->>"))

	def getPinB(self):
		return int(input("Enter Pin B for Gate " + self.getLable() + "--->>"))

class UnaryGate(LogicGate):

	def __init__(self, n):
		LogicGate.__init__(self, n)

		self.pin = None

	def getPin(self):
		return int(input("Enter value for Gate " + self.getLable() + "---->>"))

class AndGate(BinaryGate):

	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()

		if a==1 and b==1:
			return 1
		else:
			return 0

g1 = AndGate("G1")
print("the final result. " + str(g1.getOutput()))
