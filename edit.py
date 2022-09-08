with open('file_name.txt', 'r', encoding='utf-8') as inFile,\
     open('file_name.txt', 'w', encoding='utf-8') as outFile:
    for line in inFile:
        outFile.write(line[17:]) #do feel free to change the 17 to any number - THIS IS TO REMOVE THE TIMESTAMP DATA WHEN YOU EXPORT TXT FILE FROM WHATSAPP