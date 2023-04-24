
filePath1 = "slr-1.yal"
filePath2 = "slr-2.yal"
filePath3 = "slr-3.yal"
filePath4 = "slr-4.yal"

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



test= "parte1(*comentario1*)parte2(*comentario2*)parte3 \n parte4 \n parte5"

openining_symbol = "(*"
closing_symbol = "*)"

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
	print ("SOY LA FUNCION DEFINE_DELIM  Y RECIBI : \n ")
	print(text)
	pass


##GUARDA LOS TOKEN ACEPTADOS EN WHITE SPACE
def define_ws(text):
	print ("SOY LA FUNCION DEFINE_WS  Y RECIBI : \n ")
	print(text)
	pass


##GUARDA LOS TOKEN ACEPTADOS EN LETTER
def define_letter(text):
	print ("SOY LA FUNCION DEFINE_LETTER  Y RECIBI : \n ")
	print(text)

	pass
##GUARDA LOS TOKEN ACEPTADOS EN STR
def define_str(text):
	print ("SOY LA FUNCION DEFINE_STR  Y RECIBI : \n ")
	print(text)

	pass


##GUARDA LOS TOKEN ACEPTADOS EN DIGIT
def define_digit(text):
	print ("SOY LA FUNCION DEFINE_DIGIT  Y RECIBI : \n ")
	print(text)
	pass


##GUARDA LOS TOKEN ACEPTADOS EN DIGITS
def define_digits(text):
	print ("SOY LA FUNCION DEFINE_DIGITS  Y RECIBI : \n ")
	print(text)
	pass




##ESTA FUNCION ENCONTRARA LAS LINEAS DONDE SE DEFINEN LAS REGEX Y SE LAS PASARA A LAS FUNCIONES CORRESPONDIENTES
def find_definitions(clean_text):
	

	#DELIM DEFINITION
	delim_text = ""
	delim_start = clean_text.find('let delim')
	delim_end =0
	for i in range (delim_start+1, len(clean_text)):
		if (clean_text[i]=="l" and clean_text[i+1]=="e" and clean_text[i+2]=="t"):
			delim_end = i-1
			break
		if (clean_text[i]=="r" and clean_text[i+1]=="u" and clean_text[i+2]=="l"and clean_text[i+3]=="e"):
			delim_end = i-1
			break
	for i in range (delim_start, delim_end):
		delim_text=delim_text+ clean_text[i]
	define_delim(delim_text)

	#ws DEFINITION
	ws_text = ""
	ws_start = clean_text.find('let ws')
	ws_end =0
	for i in range (ws_start+1, len(clean_text)):
		if (clean_text[i]=="l" and clean_text[i+1]=="e" and clean_text[i+2]=="t"):
			ws_end = i-1
			break
		if (clean_text[i]=="r" and clean_text[i+1]=="u" and clean_text[i+2]=="l"and clean_text[i+3]=="e"):
			ws_end = i-1
			break
	for i in range (ws_start, ws_end):
		ws_text=ws_text+ clean_text[i]
	define_ws(ws_text)


	#letter DEFINITION
	letter_text = ""
	letter_start = clean_text.find('let letter')
	letter_end =0
	for i in range (letter_start+1, len(clean_text)):
		if (clean_text[i]=="l" and clean_text[i+1]=="e" and clean_text[i+2]=="t"):
			letter_end = i-1
			break
		if (clean_text[i]=="r" and clean_text[i+1]=="u" and clean_text[i+2]=="l"and clean_text[i+3]=="e"):
			letter_end = i-1
			break
	for i in range (letter_start, letter_end):
		letter_text=letter_text+ clean_text[i]
	define_letter(letter_text)




	#str DEFINITION
	str_text = ""
	str_start = clean_text.find('let str')
	str_end =0
	for i in range (str_start+1, len(clean_text)):
		if (clean_text[i]=="l" and clean_text[i+1]=="e" and clean_text[i+2]=="t"):
			str_end = i-1
			break
		if (clean_text[i]=="r" and clean_text[i+1]=="u" and clean_text[i+2]=="l"and clean_text[i+3]=="e"):
			str_end = i-1
			break
	for i in range (str_start, str_end):
		str_text=str_text+ clean_text[i]
	define_str(str_text)
	



def showLEX():
	print


file = open(filePath4, "r")


original_string = file.read()
#print(original_string)
clean = removeComments(original_string , openining_symbol , closing_symbol)
print (clean)

find_definitions(clean)


# clean = removeComments(test , openining_symbol , closing_symbol)
# print (clean)

def read():
	pass
	