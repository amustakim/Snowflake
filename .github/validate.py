import sys
# Arguments passed
print("\nName of Python script:", sys.argv[0])

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

if n > 2 or n == 1:
    print("Please pass Correct Arg")
    exit(1)

path = sys.argv[1]
try:
    loadFile = open(path)
except:
    print("unable to load file")
    exit(1)

readLine = loadFile.readline()
line = 0
while (line < 10):
    if len(readLine) == 1:
        readLine = loadFile.readline()
       # print(readLine)
    else:
        break
    line = line+1

tableName = readLine.split()
print(tableName)
if tableName == "":
    print("Read is empty")
    exit(1)

schemaName = ""
schemaType = ""
for i in tableName:
    if "Schema" in i or "schema" in i or "SCHEMA" in i:
        print(i)
        schemaName = i
    if "table" in i or "Table" in i or "TABLE" in i:
        schemaType = "Tables"
    elif "view" in i or "View" in i or "VIEW" in i:
        schemaType = "Views"
    elif "PROCEDURE" in i or "Procedure" in i or "procedure" in i:
        schemaType = "Procedures"
    else:
        continue

if schemaName == "" or schemaType == "":
    print("place the files in correct location ")
    exit(1)
splitSchemaName = schemaName.split('.')
checkPath = splitSchemaName[0]+"/"+schemaType

if checkPath in path and checkPath != "/":
    print("files locations are correct ")
    exit(0)
else:
    print("place the files in correct location ")
    exit(1)
