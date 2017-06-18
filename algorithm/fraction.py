def gcd(m, n):
	while m%n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm%oldn
	return n

class Fraction:

	def __init__(self, top, bottom):
		if((isinstance(top, int) and isinstance(bottom, int))):
			if (top * bottom < 0):
				top = int(top * (-1))
				bottom = int(bottom * (-1))
			common = gcd(top, bottom)
			self.num = top//common
			self.den = bottom//common
		else:
			print("The value of num and de is not integrter")
			exit()

	def __str__(self):
		if(self.num != 0):
			return str(self.num) + "/" + str(self.den)
		else:
			return "0"

	def __add__(self, otherFaction):
		newnum = self.num * otherFaction.den + self.den * otherFaction.num
		newden = self.den * otherFaction.den
		#common = gcd(newnum, newden)
		#return Fraction(newnum//common, newden//common)
		return Fraction(newnum, newden)

	def __eq__(self, otherFaction):
		firstnum = self.num * otherFaction.den
		secondnum = self.den * otherFaction.num
		return firstnum == secondnum

	def __sub__(self, otherFaction):
		newnum = self.num*otherFaction.den - self.den*otherFaction.num
		newden = self.den * otherFaction.den
		return Fraction(newnum, newden)

	def __mul__(self, otherFaction):
		newnum = self.num * otherFaction.num
		newden = self.den * otherFaction.den
		return Fraction(newnum, newden)

	def __truediv__(self, otherFaction):
		newnum = self.num * otherFaction.den
		newden = self.den * otherFaction.num
		return Fraction(newnum, newden)

	def __gt__(self, otherFaction):
		substract = self - otherFaction
		return substract.num > 0

	def __ge__(self, otherFaction):
		substract = self - otherFaction
		return substract.num >= 0

	def __lt__(self, otherFaction):
		substract = self - otherFaction
		return substract.num < 0

	def __le__(self, otherFaction):
		substract = self - otherFaction
		return substract.num <= 0

	def __ne__(self, otherFaction):
		substract = self - otherFaction
		return substract.num == 0

	def getNum(self):
		return self.num

	def getDen(self):
		return self.den

myfrac = Fraction(1, -2)
print("The 1st fraction " + str(myfrac))
otherfrac = Fraction(1, 2)
print("The 12nd fraction " + str(otherfrac))

print("the add operator")
result = myfrac + otherfrac
print(result)

print("the substract operator")
result = myfrac - otherfrac
print(result)

print("the multiply operator")
result = myfrac * otherfrac
print(result)

print("the true divide operator")
result = myfrac / otherfrac
print(result)

print("the greater than operator")
result = myfrac > otherfrac
print(result)

print("the greater than or equal operator")
result = myfrac >= otherfrac
print(result)

print("the less than operator")
result = myfrac < otherfrac
print(result)

print("the less than equal operator")
result = myfrac <= otherfrac
print(result)

print("the equal operator")
result = myfrac == otherfrac
print(result)

