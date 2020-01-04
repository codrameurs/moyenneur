'''

'''
def save(dict):
    # sauve les notes dans notes.json
    fichier=open("note.json","w")
    dictstr=str(dict)
    dictstr=dictstr.replace("'",'"')
    fichier.write(dictstr)
    fichier.close

def getdict():
    #recupere les notes de notes.json
    import json
    with open("notes.json") as f:
        notes_dict = json.load(f)
    return notes_dict
