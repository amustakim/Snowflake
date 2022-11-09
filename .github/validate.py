import sys
# Check if any arguments are passed
print("\nName of Python script:", sys.argv[0])

# Total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

if n > 2 or n == 1:
    print("Please pass correct number of arguments")
    exit(1)

path = sys.argv[1]
try:
    loadFile = open(path)
except:
    print("Error: Unable to load file")
    exit(1)

readLine = loadFile.readline()
line = 0
while (line < 100): #incase there are empty lines in the beginning of the file
    if len(readLine) == 1:
        readLine = loadFile.readline()
       # print(readLine)
    else:
        break
    line = line+1

tableName = readLine.split()
print(tableName)
if tableName == "":
    print("Error: Atleast one of the SQL script is empty")
    exit(1)

schemaName = ""
objectType = ""
for i in tableName:
    if "Schema" in i or "schema" in i or "SCHEMA" in i:
        schemaName = ''.join([i[0].upper(), i[1:]])
        print(schemaName)
    if "table" in i or "Table" in i or "TABLE" in i:
        objectType = "Tables"
    elif "view" in i or "View" in i or "VIEW" in i:
        objectType = "Views"
    elif "PROCEDURE" in i or "Procedure" in i or "procedure" in i:
        objectType = "Procedures"
    else:
        continue

if schemaName == "" or objectType == "":
    print("Error: Schema name or Object Type is missing in your SQL file DDL. Please check your files!")
    exit(1)
splitSchemaName = schemaName.split('.')
checkPath = splitSchemaName[0]+"/"+objectType

if checkPath in path and checkPath != "/":
    print("Success: SQL files are placed in correct schema/object folders")
    exit(0)
else:
    print("Error: SQL files are NOT placed in correct schema/object folders. Please check your files!")
    exit(1)
