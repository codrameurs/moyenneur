'''

'''
new_note=input("entre une note:")
new_sur=input("sur:")
new_note=int(new_note)
new_sur=int(new_sur)
dict={
    "francais":{
        "gen":0,
        "notes":[
            [0,0],
        ]
    }
}
def convertir(new_note,new_sur):
        produit = new_note*20
        new_note=produit/new_sur
        new_sur=20
        print("t'as note sur 20 est de %d/%d"%(new_note,new_sur))
        return new_note
if new_sur != 20:
    convertir(new_note,new_sur)
dict["francais"]["notes"][0][0]=new_note
dict["francais"]["notes"][0][1]=new_sur
fichier=open("teste.json","w")
dictstr=str(dict)
dictstr=dictstr.replace("'",'"')
fichier.write(dictstr)
fichier.close
        
        