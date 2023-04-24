
filePath1 = "slr-1.yal"
filePath2 = "slr-2.yal"
filePath3 = "slr-3.yal"
filePath4 = "slr-4.yal"

tokens = []
test= "jojo(*jojo*) jeje(*jejeje*)jajaja"

openining_symbol = "(*"
closing_symbol = "*)"

def removeComments(original , openining_symbol, closing_symbol):
	result = ""
	for character_id in range (0, len(original)):
		#print(original[character_id])
		if (original[character_id] == "(" and original[character_id+1]=="*"):
			print (" ENCONTRE (*")
			
		result
		
		


	return result




# str_list = myStr.split(substring)
# for element in str_list:
#     output_string += element


file = open(filePath1, "r")


original_string = file.read()
print(original_string)
# clean = removeComments(original_string , openining_symbol , closing_symbol)
# print (clean)
clean = removeComments(test , openining_symbol , closing_symbol)
print (clean)

def read():
	pass
	