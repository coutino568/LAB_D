
filePath1 = "slr-1.yal"
filePath2 = "slr-2.yal"
filePath3 = "slr-3.yal"
filePath4 = "slr-4.yal"

tokens = []
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
					##incluir todo despues del comentario
					# for k in range (x, len(original)):
					# 	result+=(original[k])

					#print("RESULT SO FAR:  \n")
					#print(result)
					break
	##incluir todo despues del ultimo comentario
	for l in range (lastStart, len(original)):
		result=result+original[l]



	#print(result)
		
		


	return result




# str_list = myStr.split(substring)
# for element in str_list:
#     output_string += element


file = open(filePath1, "r")


original_string = file.read()
#print(original_string)
clean = removeComments(original_string , openining_symbol , closing_symbol)
print (clean)
# clean = removeComments(test , openining_symbol , closing_symbol)
# print (clean)

def read():
	pass
	