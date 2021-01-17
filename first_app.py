def calc_tranche(a):
    cons =round((((9+(a*3.12))*1.07)*1.0025),2)
    print("la consommation est :  {}".format(cons))

a = int(input("entrer la valeur : "))
while  type(a) != str : 
    calc_tranche()
else :
    print ("la valeur doit être numérique")
    if type(a) != str:
        calc_tranche(a)