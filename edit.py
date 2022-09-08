with open('bois.txt', 'r', encoding='utf-8') as inFile,\
     open('boisn.txt', 'w', encoding='utf-8') as outFile:
    for line in inFile:
        outFile.write(line[17:])