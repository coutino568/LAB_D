
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
symbols_Table= []

alphabet=['A','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']

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

##GUARDA LOS TOKEN ACEPTADOS EN ID
def define_id(text):
	print ("SOY LA FUNCION DEFINE_ID  Y RECIBI : \n ")
	print(text)
	pass

##GUARDA LOS TOKEN ACEPTADOS EN NUMBER
def define_number(text):
	print ("SOY LA FUNCION DEFINE_NUMBER  Y RECIBI : \n ")
	print(text)
	pass


##ESTA FUNCION ENCONTRARA LAS LINEAS DONDE SE DEFINEN LAS REGEX Y SE LAS PASARA A LAS FUNCIONES CORRESPONDIENTES

def find_definitions(clean_text,text_to_find):

	#DELIM DEFINITION
	definition_text = ""
	start = clean_text.find(text_to_find)
	end =0
	for i in range (start+1, len(clean_text)):
		if (clean_text[i]=="l" and clean_text[i+1]=="e" and clean_text[i+2]=="t"):
			end = i-1
			break
		if (clean_text[i]=="r" and clean_text[i+1]=="u" and clean_text[i+2]=="l"and clean_text[i+3]=="e"):
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


file = open(filePath4, "r")


original_string = file.read()
#print(original_string)
clean = removeComments(original_string , openining_symbol , closing_symbol)
print (clean)

#find_definitions(clean)
define_delim(find_definitions(clean,"let delim"))
define_ws(find_definitions(clean,"let ws"))
define_letter(find_definitions(clean,"let letter"))
define_str(find_definitions(clean,"let str"))
define_digit(find_definitions(clean,"let digit"))
define_digits(find_definitions(clean,"let digits"))
define_id(find_definitions(clean,"let id"))
define_number(find_definitions(clean,"let number"))

# clean = removeComments(test , openining_symbol , closing_symbol)
# print (clean)






def read():
	pass
	