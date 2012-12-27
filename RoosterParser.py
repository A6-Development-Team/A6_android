<<<<<<< HEAD
#-------------------------------------------------------------------------------
#A6_android: Roosterparser
#MijnheerNeen
#thesociallions (A6 diacritical fix)
#-------------------------------------------------------------------------------
import urllib
import shutil
import os
import unicodedata
import string
from Tkinter import *

def roosterverbouwing():
    #Bestand openen en de inhoud in een string dumpen
    llnr = 0

    while llnr < 704:

        RoosterBestand = urllib.urlopen("https://files.itslearning.com/data/423/3904/P2bovenbouw/%s.html"%str(llnr+1))
        beginRooster = RoosterBestand.read().decode("windows-1252")
        RoosterBestand.close()

        #Slecht geformatteerd rooster inladen
        nuttigGedeelteRooster = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[3]

        leerlingKlas = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[1].lstrip().split("\n")[0].strip()
        leerlingAchternaam = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[2].lstrip().split("\n")[0].strip()
        leerlingVoornaam = nuttigGedeelteRooster.split("</TD>")[0].lstrip().rstrip()
        leerlingVoornaamNormalised = ''.join(x for x in unicodedata.normalize('NFKD', leerlingVoornaam) if x in (string.ascii_letters + "- ")) #Don't ask.
        print "%d: %s %s, %s" % (llnr+1, leerlingVoornaam, leerlingAchternaam, leerlingKlas)


        roosterTabel = nuttigGedeelteRooster.split("<table>")[1]

        ##roosterRijen = roosterTabel.split("<tr>")[2:]
        ##gespletenRoosterRijen= []
        ##for rij in roosterRijen:
        ##    gespletenRoosterRijen.append(rij.split("<td>"))
        ##
        ##gespletenRoosterRijen.remove(gespletenRoosterRijen[0])
        ##for uur in gespletenRoosterRijen:
        ##    uur.remove(uur[0])
        ##    for dag in uur[1:]:
        ##        dag = dag.rstrip("  </td>\n")
        #deze zooi wordt later belangrijk

        #deze zooi is belangrijk
        for i in range(9):
        	roosterTabel = roosterTabel.replace("u0%s"%str(i+1),str(i+1))

        Replacements = [("Uur\Dag",""),("MTU","mt"),("<br>","<br />"),("maandag","Ma"),("dinsdag","Di"),("woensdag","Wo"),("donderdag","Do"),("vrijdag","Vr")]

        for r in Replacements:
        	roosterTabel = roosterTabel.replace(r[0],r[1])

        roosterTabel = roosterTabel.split("""<td style="background-color: rgb(220, 220, 220);">u10</td>""")[0].rstrip().rstrip("<tr>")
        roosterTabel = roosterTabel + "\n</table>"
        beginHTML = u"""<!DOCTYPE html>
        <html>
        	<head>
        		<meta charset="utf-8" />
        		<meta name="viewport" content="width=device-width, initial-scale=1" />
        		<title>%s</title>
        		<link rel="stylesheet" href="../jquery.mobile-1.2.0.min.css" />
        		<script src="../js.min.js">
        		</script>

        	</head>
        	<body>
        		<!-- Home -->
        		<div data-role="page" id="page1">
        			<div data-theme="a" data-role="header" data-position="fixed">
        				<a href="#" data-rel="back" data-icon="arrow-l">Terug</a>
        				<h5>
        					%s
        				</h5>
        			</div>
        			<div data-role="content" id="rooster">""" %(leerlingVoornaam,leerlingVoornaam)
        eindHTML= u"""
        </body>
        </html>"""

        if "A6" in leerlingKlas:
            leerlingKlas = leerlingKlas[3].lower()
            mapNaam = os.getcwd() + "/assets/www/rooster/%s/" % leerlingKlas
            if not os.path.exists(mapNaam):
            	os.makedirs(mapNaam)
            NieuwBestand = open("%s%s.html" % (mapNaam, leerlingVoornaamNormalised),"w")
            NieuwBestand.write((beginHTML + u'\n<table width="100%">' + roosterTabel + u"\n" + eindHTML).encode('utf8'))
            NieuwBestand.close()
        llnr += 1

def afsluiten():
    venster.destroy()

def starting():
        roosterverbouwing()
        welkom.config(text="Klaar!")
        start.config(text="Klik hier om te sluiten.", command=afsluiten)



## GUI
venster = Tk()

welkom = Label(master=venster, text="Welkom", font=("Arial",24))
start = Button(master=venster, text="Start", command=starting)
welkom.pack()
start.pack(padx=5, pady=5, fill=X)

venster.minsize(width=250, height=80)

venster.title("RoosterParser")
#venster.iconbitmap(default="favicon.ico")
venster.mainloop()

=======
#-------------------------------------------------------------------------------
#A6_android: Roosterparser, VolgendeLes-feat branch
#MijnheerNeen
#thesociallions (A6 diacritical fix)
#-------------------------------------------------------------------------------
import urllib
import os
import unicodedata
import string
from Tkinter import *

def roosterverbouwing():
    #Bestand openen en de inhoud in een string dumpen
    llnr = 99

    while llnr < 100:

        RoosterBestand = urllib.urlopen("https://files.itslearning.com/data/423/3904/P2bovenbouw/%s.html"%str(llnr+1))
        beginRooster = RoosterBestand.read().decode("windows-1252")
        RoosterBestand.close()

        #Slecht geformatteerd rooster inladen
        nuttigGedeelteRooster = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[3]

        leerlingKlas = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[1].lstrip().split("\n")[0].strip()
        leerlingAchternaam = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[2].lstrip().split("\n")[0].strip()
        leerlingVoornaam = nuttigGedeelteRooster.split("</TD>")[0].lstrip().rstrip()
        leerlingVoornaamNormalised = ''.join(x for x in unicodedata.normalize('NFKD', leerlingVoornaam) if x in (string.ascii_letters + "- ")) #Don't ask.
        print "%d: %s %s, %s" % (llnr+1, leerlingVoornaam, leerlingAchternaam, leerlingKlas)

        roosterTabel = nuttigGedeelteRooster.split("<table>")[1]

        ##roosterRijen = roosterTabel.split("<tr>")[2:]
        ##gespletenRoosterRijen= []
        ##for rij in roosterRijen:
        ##    gespletenRoosterRijen.append(rij.split("<td>"))
        ##
        ##gespletenRoosterRijen.remove(gespletenRoosterRijen[0])
        ##for uur in gespletenRoosterRijen:
        ##    uur.remove(uur[0])
        ##    for dag in uur[1:]:
        ##        dag = dag.rstrip("  </td>\n")
        #deze zooi wordt later belangrijk

        #deze zooi is belangrijk
        for i in range(9):
            roosterTabel = roosterTabel.replace("u0%s"%str(i+1),str(i+1))

        Replacements = [("Uur\Dag",""),("MTU","mt"),("<br>","<br />"),("maandag","Ma"),("dinsdag","Di"),("woensdag","Wo"),("donderdag","Do"),("vrijdag","Vr")]

        for r in Replacements:
            roosterTabel = roosterTabel.replace(r[0],r[1])

        roosterTabel = roosterTabel.split("""<td style="background-color: rgb(220, 220, 220);">u10</td>""")[0].rstrip().rstrip("<tr>")
        roosterTabel += "\n</table>"
        roosterUren = roosterTabel.split("<tr>")[2:]
        for i in range(len(roosterUren)):
            #roosterUren[i] = ('<tr id="TTVLuur%s">' % str(i+1)) + roosterUren[i]
            roosterDagen = roosterUren[i].split("<td>")
            for e in range(len(roosterDagen[1:])):
                roosterDagen[e+1] = ('<td id="TTVLd%su%s">' % (str(e+1),str(i+1))) + roosterDagen[e+1]
            roosterUren[i] = "".join(roosterDagen)

        RoosterTabel = "".join(roosterUren)
        beginHTML = u"""<!DOCTYPE html>
        <html>
        	<head>
        		<meta charset="utf-8" />
        		<meta name="viewport" content="width=device-width, initial-scale=1" />
        		<title>%s</title>
        		<link rel="stylesheet" href="../jquery.mobile-1.2.0.min.css" />
        		<script src="../js.min.js">
        		</script>

        	</head>
        	<body>
        		<!-- Home -->
        		<div data-role="page" id="page1">
        			<div data-theme="a" data-role="header" data-position="fixed">
        				<a href="#" data-rel="back" data-icon="arrow-l">Terug</a>
        				<h5>
        					%s
        				</h5>
        			</div>
        			<div data-role="content" id="rooster">""" %(leerlingVoornaam,leerlingVoornaam)
        eindHTML= u"""
        </body>
        </html>"""

        if "A6" in leerlingKlas:
            print"  A6"
            leerlingKlas = leerlingKlas[3].lower()
            mapNaam = os.getcwd() + "/assets/www/rooster/%s/" % leerlingKlas
            if not os.path.exists(mapNaam):
                os.makedirs(mapNaam)
            NieuwBestand = open("%s%s.html" % (mapNaam, leerlingVoornaamNormalised),"w")
            NieuwBestand.write((beginHTML + u'\n<table width="100%">' + RoosterTabel + u"\n" + eindHTML).encode('utf8'))
            NieuwBestand.close()
        llnr += 1

def afsluiten():
    venster.destroy()

def starting():
    roosterverbouwing()
    welkom.config(text="Klaar!")
    start.config(text="Klik hier om te sluiten.", command=afsluiten)



## GUI
venster = Tk()

welkom = Label(master=venster, text="Welkom", font=("Arial",24))
start = Button(master=venster, text="Start", command=starting)
welkom.pack()
start.pack(padx=5, pady=5, fill=X)

venster.minsize(width=250, height=80)

venster.title("RoosterParser")
venster.iconbitmap(default="favicon.ico")
venster.mainloop()

>>>>>>> RoosterParser, tags in tabel
