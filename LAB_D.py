
filePath1 = "slr-1.yal"
filePath2 = "slr-2.yal"
filePath3 = "slr-3.yal"
filePath4 = "slr-4.yal"

filepaths=["slr-1.yal","slr-2.yal","slr-3.yal","slr-4.yal"]

delim_tokens = []
definition_keyword = "let"
ws_tokens = []
letter_tokens =[]
str_tokens =[]
digit_tokens =[]
digits_tokens = []
id_tokens = []
positive_kleene = '+'
kleene = '*'
symbols_Table= []
keywords = []
errors = []

alphabet=['A','	B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
digits=[]
openining_symbol = "(*"
closing_symbol = "*)"


## UTILS

#busca un caracter en una cadena y devuelve la cantidad de veces que lo encontro
def findAndCount(text,characterToSearch):
	count=0
	for i in range (0,len(text)):
		if (text[i]==characterToSearch):
			count = count+1
	return count








#busca un caracter en una cadena y devuelve la cantidad de veces que lo encontro
def findAndReturnIndexes(text,characterToSearch):
	indexes = []
	for i in range (0,len(text)):
		if (text[i]==characterToSearch):
			indexes.append(i)
	return indexes


def printErrors():
	print("ERRORS FOUND: \n ")
	print(errors)
	for error in errors:
		print(error)






#FUNCION QUE LE QUITA LOS COMENTARIOS 
def removeComments(original , openining_symbol, closing_symbol):
	result = ""
	lastStart=0
	lastEnd=0
	for character_id in range (0, len(original)):
		#print(original[character_id])
		if (original[character_id] == "(" and original[character_id+1]=="*"):
			#print (" ENCONTRE (*")
			for x in range (character_id, len(original)):
				if (original[x]=="*" and original[x+1]==")"):
					##incluir todo antes del comentario

					for j in range (lastStart, character_id):
						result +=(original[j])
					lastStart=x+2
					
					break
	##incluir todo despues del ultimo comentario
	for l in range (lastStart, len(original)):
		result=result+original[l]
	return result



##GUARDA LOS TOKEN ACEPTADOS EN DELIM
def define_delim(text):
	if (text==""):
		return
	print ("SOY LA FUNCION DEFINE_DELIM  Y RECIBI :\n'"+text+"'")
	tokens=[]

	reduced_text = ""

	keywords.append("delim")
	if(text.find('[')!="-1"):
		print("encontre un '[' ")
		if(findAndCount(text,'[')!=findAndCount(text,']')):
			errors.append("THERE IS A MISSING [] in DELIM")
		if(findAndCount(text,"'")!=findAndCount(text,"'")):
			errors.append("THERE IS A MISSING '' in DELIM")
		if(findAndCount(text,'"')!=findAndCount(text,'"')):
			errors.append("THERE IS A MISSING \"\" in DELIM")
		countOfDashes= findAndCount(text,'-')
		
		reduced_text = text[text.find('[')+1:text.find(']')]
		#reduced_text= text[findAndCount(text,"["):findAndCount(text,"]")]
		print(reduced_text)
		if (countOfDashes >0):
			pass

		tokens_indexes= []
		singleQuoteIndixes = findAndReturnIndexes(reduced_text,"'")
		temp=""
		for i in range (0,len(singleQuoteIndixes)):
			if(i%2 == 0):
				temp = reduced_text[singleQuoteIndixes[i]:singleQuoteIndixes[i+1]]
				
				tokens_indexes= singleQuoteIndixes[i]

			print("LOS INDICES DE LOS TOKENS SON "+ tokens_indexes)
		print("LO QUE ESTA CONTENIDO EN '' es:"+ reduced_text[i+1])
		tokens.append(reduced_text[i+1])




	pass


##GUARDA LOS TOKEN ACEPTADOS EN WHITE SPACE
def define_ws(text):
	if (text==""):
		return
	keywords.append("ws")
	print ("SOY LA FUNCION DEFINE_WS  Y RECIBI :\n'"+text+"'")
	
	pass


##GUARDA LOS TOKEN ACEPTADOS EN LETTER
def define_letter(text):
	if (text==""):
		return
	keywords.append("letter")
	print ("SOY LA FUNCION DEFINE_LETTER  Y RECIBI :\n'"+text+"'")
	

	pass
##GUARDA LOS TOKEN ACEPTADOS EN STR
def define_str(text):
	if (text==""):
		return
	keywords.append("str")
	print ("SOY LA FUNCION DEFINE_STR  Y RECIBI :\n'"+text+"'")
	

	pass


##GUARDA LOS TOKEN ACEPTADOS EN DIGIT
def define_digit(text):
	if (text==""):
		return
	keywords.append("digit")
	print ("SOY LA FUNCION DEFINE_DIGIT  Y RECIBI :\n'"+text+"'")
	
	pass


##GUARDA LOS TOKEN ACEPTADOS EN DIGITS
def define_digits(text):
	if (text==""):
		return
	keywords.append("digits")
	print ("SOY LA FUNCION DEFINE_DIGITS  Y RECIBI :\n'"+text+"'")
	
	pass

##GUARDA LOS TOKEN ACEPTADOS EN ID
def define_id(text):
	if (text==""):
		return
	keywords.append("id")
	print ("SOY LA FUNCION DEFINE_ID  Y RECIBI :\n'"+text+"'")
	
	pass

##GUARDA LOS TOKEN ACEPTADOS EN NUMBER
def define_number(text):
	if (text==""):
		return
	keywords.append("number")
	print ("SOY LA FUNCION DEFINE_NUMBER  Y RECIBI :\n'"+text+"'")
	
	pass


##ESTA FUNCION ENCONTRARA LAS LINEAS DONDE SE DEFINEN LAS REGEX Y SE LAS PASARA A LAS FUNCIONES CORRESPONDIENTES

def find_definitions(clean_text,text_to_find):

	#DELIM DEFINITION
	definition_text = ""
	start = clean_text.find(text_to_find)
	if (start ==-1):
		return definition_text
	end =0
	for i in range (start+1, len(clean_text)):
		if (clean_text[i]=="l" and clean_text[i+1]=="e" and clean_text[i+2]=="t" and clean_text[i+3]==" "):
			end = i-1
			break
		elif (clean_text[i]=="r" and clean_text[i+1]=="u" and clean_text[i+2]=="l"and clean_text[i+3]=="e"):
			end = i-1
			break
	for i in range (start, end):
		definition_text=definition_text+ clean_text[i]
	return definition_text



def interpretRegEx(regex):
	pass


def readRegEx(regex):
	pass


def showLEX():
	print



print(filepaths)
file_id=int( input("INGRESE EL NUMERO DEL ARCHIVO QUE DESEA USAR\n"))
file = open(filepaths[file_id-1], "r")
original_string = file.read()
clean = removeComments(original_string , openining_symbol , closing_symbol)
print (clean)



define_delim(find_definitions(clean,"let delim"))
# define_ws(find_definitions(clean,"let ws"))
# define_letter(find_definitions(clean,"let letter"))
# define_str(find_definitions(clean,"let str"))
# define_digit(find_definitions(clean,"let digit"))
# define_digits(find_definitions(clean,"let digits"))
# define_id(find_definitions(clean,"let id"))
# define_number(find_definitions(clean,"let number"))


printErrors()

def read():
	pass
	
