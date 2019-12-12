'''

'''

def save(dict):
    fichier=open("note.json","w")
    dictstr=str(dict)
    dictstr=dictstr.replace("'",'"')
    fichier.write(dictstr)
    fichier.close