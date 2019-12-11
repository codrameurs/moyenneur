new_note=input("entre un note")
new_sur=input("sur")
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