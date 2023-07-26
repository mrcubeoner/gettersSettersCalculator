import os
# This function write in the file
def wFile(string):
    fileName= "GettersySetters.txt"
    with open(fileName, 'w') as file:
        file.write(string)

# Esta funcion nos sirve para eliminar el file previo
def deleteFile() -> None:
    if os.path.exists("GettersySetters.txt"):
        os.remove("GettersySetters.txt")
        print(f"The file already exists and has been deleted")
    else:
        print(f"The file doesn't exists. Do nothing")

#######################################################################################################
# Main FUnction
deleteFile()
variableNo = int(input("Number of variables: "))

count=0
stringF = ""

while count!=variableNo:
    variableName=input("Variable name: ")
    semistring= "def get"+ str(variableName[0:1].upper()) + str(variableName[1:]) +" (self): \n\treturn self."+ variableName +" \ndef set"+ str(variableName[0:1].upper()) + str(variableName[1:]) +" (self, "+ variableName +") -> (None): \n\tself."+variableName+" = "+variableName+"\n"
    stringF = stringF + semistring
    count = count + 1

print(f"The result is: \n\n{stringF}")
wFile(stringF)