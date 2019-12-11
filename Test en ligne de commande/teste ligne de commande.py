import Moyenne_arithmétique
new_note=input("entre une note:")
new_sur=input("sur:")
dict={
    "francais":{
        "gen":0,
        "notes":[
            [0,0],
        ]
    }
}
dict["francais"]["notes"][0][0]=new_note
dict["francais"]["notes"][0][1]=new_sur
fichier=open("teste.json","w")
dictstr=str(dict)
dictstr=dictstr.replace("'",'"')
print(dictstr)
fichier.write(dictstr)
fichier.close
def convertir(dict,new_note,new_sur):
    if (new_sur != 20):
        dif = 20-new_sur
        somme = new_note+dif

