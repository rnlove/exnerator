from exnerator import *
from record import *
import time

codebook = {
	'card': {
		'I': {
			'ZW': 1.0,
			'ZA': 4.0,
			'ZD': 6.0,
			'ZS': 3.5
		},
		"II": {
			'ZW': 4.5,
			'ZA': 3.0,
			'ZD': 6.0,
			'ZS': 3.5
		},
		"III": {
			'ZW': 5.5,
			'ZA': 3.0,
			'ZD': 4.0,
			'ZS': 4.5
		},
		"IV": {
			'ZW': 2.0,
			'ZA': 4.0,
			'ZD': 3.5,
			'ZS': 5.0
		},
		"V": {
			'ZW': 1.0,
			'ZA': 2.5,
			'ZD': 5.0,
			'ZS': 4.0
		},
		"VI": {
			'ZW': 2.5,
			'ZA': 2.5,
			'ZD': 6.0,
			'ZS': 6.5
		},
		"VII": {
			'ZW': 2.5,
			'ZA': 1.0,
			'ZD': 3.0,
			'ZS': 4.0
		},
		"VIII": {
			'ZW': 4.5,
			'ZA': 3.0,
			'ZD': 3.0,
			'ZS': 4.0
		},
		"IX": {
			'ZW': 5.5,
			'ZA': 2.5,
			'ZD': 4.5,
			'ZS': 5.0
		},
		"X": {
			'ZW': 5.5,
			'ZA': 4.0,
			'ZD': 4.5,
			'ZS': 6.0
		}
	},
	'devQuality': {
		"+": "Synthesized Response",
		"v/+": "Synthesized Response with Vague",
		"o": "Ordinary Response",
		"v": "Vague Response"
	},
	'locType': {
		"W": "Whole Response",
		"D": "Common Detail Response",
		"Dd": "Unusual Detail Response",
		"WS": "Whole Response with White Space",
		"DS": "Common Detail Response with White Space",
		"DdS": "Unusual Detail Response with White Space"
	},
	'formQuality': {
		"+": "Superior",
		"o": "Ordinary",
		"u": "Unusual",
		"-": "Minus",
		"": "None"
	},
	'determinants': {
		"F": "Form", 
		"FD": "Form Dimension",
		"(2)": "Pair",
		"Fr": "Form-Reflection",
		"rF":"Reflection-Form",
		"Ma": "Human Movement (Active)",
		"Mp": "Human Movement (Passive)",
		"Ma-p": "Human Movement (Active/Passive)",
		"FMa": "Animal Movement (Active)",
		"FMp": "Animal Movement (Passive)",
		"FMa-p": "Animal Movement (Active/Passive)",
		"ma": "Inanimate Movement (Active)",
		"mp": "Inanimate Movement (Passive)",
		"ma-p": "Inanimate Movement (Active/Passive)",
		"C": "Pure Color",
		"CF": "Color-Form",
		"FC": "Form-Color",
		"Cn": "Color Naming",
		"C'": "Pure Achromatic Color",
		"C'F": "Achromatic Color-Form",
		"FC'": "Form-Achromatic Color",
		"T": "Pure Texture",
		"TF": "Texture-Form",
		"FT": "Form-Texture",
		"V": "Pure Vista",
		"VF": "Vista-Form",
		"FV": "Form-Vista",
		"Y": "Pure Shading",
		"YF": "Shading-Form",
		"FY": "Form-Shading"
	},
	'contents': {
		"H": "Whole Human",
		"(H)": "Whole Human (Fictional)",
		"Hd": "Human Detail",
		"(Hd)": "Human Detail (Fictional)",
		"Hx": "Human Experience",
		"A": "Whole Animal",
		"(A)": "Whole Animal (Fictional)",
		"Ad": "Animal Detail",
		"(Ad)": "Animal Detail (Fictional)",
		"An": "Anatomy",
		"Art":"Art",
		"Ay":"Anthropology",
		"Bl":"Blood",
		"Bt":"Botany",
		"Cg":"Clothing",
		"Cl":"Clouds",
		"Ex":"Explosion",
		"Fi":"Fire",
		"Fd":"Food",
		"Ge":"Geography",
		"Hh":"Household",
		"Ls":"Landscape",
		"Na":"Nature",
		"Sc":"Science",
		"Sx":"Sex",
		"Xy":"X-Ray",
		"Id":"Idiographic"
	},
	'zScore': {
		"ZW": "Whole Response",
		"ZA": "Adjacent Objects",
		"ZD": "Distant Objects",
		"ZS": "Integrated White Space"
	},
	'zValue': {
		'I': {
			'ZW': 1.0,
			'ZA': 4.0,
			'ZD': 6.0,
			'ZS': 3.5
		},
		"II": {
			'ZW': 4.5,
			'ZA': 3.0,
			'ZD': 6.0,
			'ZS': 3.5
		},
		"III": {
			'ZW': 5.5,
			'ZA': 3.0,
			'ZD': 4.0,
			'ZS': 4.5
		},
		"IV": {
			'ZW': 2.0,
			'ZA': 4.0,
			'ZD': 3.5,
			'ZS': 5.0
		},
		"V": {
			'ZW': 1.0,
			'ZA': 2.5,
			'ZD': 5.0,
			'ZS': 4.0
		},
		"VI": {
			'ZW': 2.5,
			'ZA': 2.5,
			'ZD': 6.0,
			'ZS': 6.5
		},
		"VII": {
			'ZW': 2.5,
			'ZA': 1.0,
			'ZD': 3.0,
			'ZS': 4.0
		},
		"VIII": {
			'ZW': 4.5,
			'ZA': 3.0,
			'ZD': 3.0,
			'ZS': 4.0
		},
		"IX": {
			'ZW': 5.5,
			'ZA': 2.5,
			'ZD': 4.5,
			'ZS': 5.0
		},
		"X": {
			'ZW': 5.5,
			'ZA': 4.0,
			'ZD': 4.5,
			'ZS': 6.0
		},
	},
	'special': {
		"DV1": "Deviant Verbalization (Level 1)",
		"DV2": "Deviant Verbalization (Level 2)",
		"DR1": "Deviant Response (Level 1)",
		"DR2": "Deviant Response (Level 2)",
		"INCOM1": "Incongruous Combination (Level 1)",
		"INCOM2": "Incongruous Combination (Level 2)",
		"FABCOM1": "Fabulized Combination (Level 1)",
		"FABCOM2": "Fabulized Combination (Level 2)",
		"CONTAM": "Contamination",
		"ALOG": "Inappropriate Logic",
		"PSV":"Perseveration",
		"AB":"Abstract Content",
		"AG":"Aggressive Movement",
		"COP":"Cooperative Movement",
		"MOR":"Morbid Content",
		"PER":"Personal",
		"CP":"Color Projection"
		}
}

class Code:
	def __init__(self):
		pass
		self.name = ""
		self.dict = {}
		self.lookup = list(self.dict.keys())
		#self.value stores the index of an element in the list above
		self.value = self.parse(input)
		self.error = 0
	#The "short name" of a code is its dict key
	
	def short(self):
		if self.value != None:
			return self.lookup[self.value]
		else: return ""
	#The "long name" of a code is the value so we look up key
	
	def long(self):
		return self.dict[self.short()]
	
	def parseError(self):
		print("ERROR: Unmatched ", self.name.lower(),"!",sep='')
		self.error = 1
		return "ERR"

	def parse(self,input):
		if input in self.lookup:
			return input
		else:
			return self.parseError()
	
	def parseSuffix(self,input):
		output = None
		suffixLookup = sorted(self.lookup,key=len,reverse=True) #sort by length
		for code in suffixLookup:
			if output == None:
				if input.endswith(code):
					output = code
		if output == None:
			return self.parseError()
		else:
			return output

	def parsePrefix(self,input):
		output = None
		prefixLookup = sorted(self.lookup,key=len,reverse=True) #sort by length
		for code in prefixLookup:
			if output == None:
				if input.startswith(code):
					return code
		if output == None:
			return self.parseError()

	def parseList(self,input):
		output = []
		l = input.split(self.delimiter)
		for item in l:
			if item in self.lookup:
				output.append(item)
			else:
				return self.parseError()
		return output

	def printValue(self):
		print(self.name, ": ",self.strValue,sep='')
		#time.sleep(0.01)

	def genStrValue(self):
		if self.value == "ERR":
			return "ERR"
		else:
			return self.dict[self.value]

class Card(Code):
	def __init__(self,input):
		self.name = "Card"
		self.dict = codebook['card']
		#convert the dictionary into a list of keys
		self.lookup = list(self.dict.keys())
		self.error = 0
		#self.value stores the index of an element in the list above
		self.value = self.parse(input)
		self.strValue = self.value
		#self.printValue()

class DevQuality(Code):
	def __init__(self,input):
		self.name = "Developmental Quality"
		self.dict = codebook['devQuality']
		self.lookup = list(self.dict.keys())
		self.error = 0
		#self.value stores the index of an element in the list above
		self.value = self.parseSuffix(input)
		self.strValue = self.value
		#self.printValue()

class LocType(Code):
	def __init__(self,input):
		self.name = "Location Type"
		self.dict = codebook['locType']
		self.lookup = list(self.dict.keys())
		self.error = 0
		self.value = self.parsePrefix(input)
		self.strValue = self.value
		self.S = 0
		if self.strValue.endswith('S'):
			self.S = 1
		self.W = 0
		if self.strValue.startswith('W'):
			self.W = 1
		self.D = 0
		if self.strValue in ['D','DS']:
			self.D = 1
		self.Dd = 0
		if self.strValue in ['Dd','DdS']:
			self.Dd = 1
		#self.printValue()

class LocationNumber(Code):
	def __init__(self,input):
		self.name = "Location Number"
		self.dict = {}
		self.error = 0
		self.value = self.parse(input)
		self.strValue = str(self.value)
		#self.printValue()
	def parse(self,input):
		if str(input).isnumeric():
			return input
		else:
			return self.parseError()

class Determinants(Code):
	def __init__(self,input):
		self.name = "Determinants"
		self.dict = codebook['determinants']
		self.delimiter = '.'
		self.error = 0
		self.lookup = list(self.dict.keys())
		if input[-1] in codebook['formQuality'].keys():
			input = input[:-1]
		self.value = self.parseList(input)
		self.strValue = str(self.delimiter.join(self.value))
		self.M = 0
		self.FM = 0
		self.m = 0
		self.a = 0
		self.p = 0
		self.Ma = 0
		self.Mp = 0
		self.tallyMovement()
		#self.printValue()
	def tallyMovement(self):
		for determinant in self.value:
			if determinant.startswith("M"):
				self.M += 1
				if determinant.endswith("p"):
					self.Mp += 1
					self.p += 1
				if determinant[1] == 'a':
					self.Ma += 1
					self.a += 1
			elif determinant.startswith('FM'):
				self.FM += 1
				if determinant.endswith("p"):
					self.p += 1
				if determinant[1] == 'a':
					self.a += 1
			elif determinant.startswith('m'):
				self.m += 1
				if determinant.endswith("p"):
					self.p += 1
				if determinant[1] == 'a':
					self.a += 1

class FormQuality(Code):
	def __init__(self,input):
		self.name = "Form Quality"
		self.dict = codebook['formQuality']
		self.error = 0
		self.lookup = list(self.dict.keys())
		if input[-1] not in self.dict:
			self.value = "None"
			self.strValue = "None"
		else:
			self.value = input[-1]
			self.strValue = self.value
		#self.printValue()

class Pair(Code):
	def __init__(self,input):
		self.name = "Pair"
		self.dict = {}
		self.error = 0
		#self.value stores the index of an element in the list above
		self.value = self.parse(input)
		self.strValue = self.genStrValue()
		#self.printValue()
	def parse(self,input):
		if input in [2,"2"]:
			return True
		elif input == None:
			return False
		else:
			return self.parseError()
	def genStrValue(self):
		if self.value == False:
			return ""
		elif self.value == True:
			return "2"
		else:
			return "ERR"

class Contents(Code):
	def __init__(self,input):
		self.name = "Contents"
		self.dict = codebook['contents']
		self.error = 0
		self.delimiter = ','
		self.lookup = list(self.dict.keys())
		self.value = self.parseList(input)
		self.strValue = str(self.delimiter.join(self.value))
		#self.printValue()

class Popular(Code):
	def __init__(self,input):
		self.name = "Popular"
		self.dict = {}
		self.error = 0
		#self.value stores the index of an element in the list above
		self.value = self.parse(input)
		self.strValue = self.genStrValue()
		#self.printValue()
	def parse(self,input):
		if input in ['p','P']:
			return True
		elif input == None:
			return False
		else:
			return self.parseError()
	def genStrValue(self):
		if self.value == False:
			return "No"
		elif self.value == True:
			return "Yes"
		else:
			return "ERR"

class ZScore(Code):
	def __init__(self,input,card):
		self.name = "Z-Score"
		self.dict = codebook['zScore']
		self.card = card.value
		self.error = 0
		#convert the dictionary into a list of keys
		self.lookup = list(self.dict.keys())
		#self.value stores the index of an element in the list above
		if self.card == "ERR":
			self.value = "ERR"
		else:
			self.value = self.parse(input)
		self.strValue = self.genStrValue()
		#self.printValue()
	def parse(self,input):
		if input in self.lookup:
			return float(codebook['zValue'][self.card][input])
		elif input == None:
			return 0
		elif str(input).isnumeric():
			if input in codebook['zValue'][self.card].values():
				return float(input)
		return self.parseError()
	def genStrValue(self):
		if self.value == None:
			return ""
		else:
			return str(self.value)

class Special(Code):
	def __init__(self,input):
		self.name = "Special Scores"
		self.dict = codebook['special']
		self.error = 0
		self.delimiter = ','
		self.lookup = list(self.dict.keys())
		self.value = []
		self.strValue = ""
		if input != None:
			self.value = self.parseList(input)
			self.strValue = str(self.delimiter.join(self.value))
		#self.printValue()
	def addGHR(self):
		self.value.append("GHR")
		self.strValue = str(self.delimiter.join(self.value))

	def addPHR(self):
			self.value.append("PHR")
			self.strValue = str(self.delimiter.join(self.value))
