
filePath1 = "slr-1.yal"
filePath2 = "slr-2.yal"
filePath3 = "slr-3.yal"
filePath4 = "slr-4.yal"

delim_tokens = []
definition_keyword = "let"




test= "parte1(*comentario1*)parte2(*comentario2*)parte3 \n parte4 \n parte5"

openining_symbol = "(*"
closing_symbol = "*)"

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



	#print(result)
		
		


	return result





##
def define_delim(text):
	print ("SOY LA FUNCION DEFINE_DELIM  Y RECIBI : \n ")
	print(text)
	pass



def define_ws(text):
	pass



def define_letter(text):

	pass


def define_digit(text):
	pass

def define_digits(text):
	pass
# str_list = myStr.split(substring)
# for element in str_list:
#     output_string += element








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
	