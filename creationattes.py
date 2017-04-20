#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

import subprocess

def ecriture(nom,prenom):
    texte_ligne="Attestation de réussite|délivrée à %s %s"%(nom,prenom)
    commande = subprocess.Popen("""curl -o texte.png "http://chart.apis.google.com/chart" --data-urlencode "chst=d_text_outline" --data-urlencode "chld=000000|56|h|FFFFFF|b|%s" """%texte_ligne,shell = True,stdout=subprocess.PIPE)
    (resultat, ignorer) = commande.communicate()
    commande=subprocess.Popen("mogrify -resize 1000x600 texte.png",shell=True,stdout=subprocess.PIPE)
    (resultat, ignorer) = commande.communicate()
    commande=subprocess.Popen("""curl -o qrcode.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=http://p-fb.net/certification/SecuTIC" """,shell=True,stdout=subprocess.PIPE)
    (resultat, ignorer) = commande.communicate()
    commande=subprocess.Popen("mogrify -resize 84x84 qrcode.png",shell=True,stdout=subprocess.PIPE)
    (resultat, ignorer) = commande.communicate()
    commande=subprocess.Popen("composite -gravity center texte.png fond_attestation.png combinaison.png",shell=True,stdout=subprocess.PIPE)
    (resultat, ignorer) = commande.communicate()
    commande=subprocess.Popen("composite -geometry +1478+994 qrcode.png combinaison.png attestation.png",shell=True,stdout=subprocess.PIPE)
    (resultat, ignorer) = commande.communicate()


    #import subprocess
#command = "echo \"lol\""
#p = subprocess.Popen(command, universal_newlines=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#text = p.stdout.read()
#retcode= p.wait()
#print text
#tu remplace commande par ta commande
#si tu as des doubles guillemets dans ta commande soit tu les echappe avec anti slash
#oit les guillemets les plus exterieurs tu les remplace par des guillemets simples
#genre 'echo "lol" '
#ou "echo \"lol\" "
#commande = subprocess.Popen("""curl -o texte.png "http://chart.apis.google.com/chart" --data-urlencode "chst=d_text_outline" --data-urlencode "chld=000000|56|h|FFFFFF|b|%s" """%texte_ligne,shell = True,stdout=subprocess.PIPE)
    #(resultat, ignorer) = commande.communicate()