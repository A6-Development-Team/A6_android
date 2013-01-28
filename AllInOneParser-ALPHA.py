import urllib, os, unicodedata, string, pickle
from Tkinter import *

def leerlingverbouwing():
    #Bestand openen en de inhoud in een string dumpen
    print "Bovenbouwroosters"
    print "================="
    llnr = 0
    leerlingenlijst = []
    while llnr < 703: #Even op 703 gezet, 404 vinden werkte niet
        RoosterBestand = urllib.urlopen("https://files.itslearning.com/data/423/3904/P3bovenbouw/%s.html"%str(llnr+1))
        beginRooster = RoosterBestand.read().decode("windows-1252")
        RoosterBestand.close()

        if beginRooster[:1] == """<!DOCTYPE html""":
            print "Done: 404 reached"
            break


        #Slecht geformatteerd rooster inladen
        nuttigGedeelteRooster = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[3]

        leerlingKlas = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[1].lstrip().split("\n")[0].strip()[1:]
        leerlingAchternaam = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[2].lstrip().split("\n")[0].strip()
        leerlingVoornaam = nuttigGedeelteRooster.split("</TD>")[0].lstrip().rstrip()
        leerlingVoornaamNormalised = ''.join(x for x in unicodedata.normalize('NFKD', leerlingVoornaam) if x in (string.ascii_letters + "-")) #Don't ask.
        leerlingAchternaamNormalised = ''.join(x for x in unicodedata.normalize('NFKD', leerlingAchternaam) if x in (string.ascii_letters + "-"))
        print "%d: %s %s, %s" % (llnr+1, leerlingVoornaam, leerlingAchternaam, leerlingKlas)

        roosterTabel = nuttigGedeelteRooster.split("<table>")[1]

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
            roosterUren[i] = "<tr>" + roosterUren[i]
            roosterDagen = roosterUren[i].split("<td>")
            for e in range(len(roosterDagen[1:])):
                roosterDagen[e+1] = ('<td id="TTVLd%su%s">' % (str(e+1),str(i+1))) + roosterDagen[e+1]
            roosterUren[i] = "".join(roosterDagen)

        roosterTabel = "".join(roosterTabel.split("<tr>")[:2] + roosterUren)
        beginHTML = u"""<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <title>%s</title>
                <link rel="stylesheet" href="../../jquery.mobile-1.2.0.min.css" />
                <script src="../../js.min.js">
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
                    <div data-role="content" id="rooster">
                    <div id="pauze" style="visibility:hidden;">%s</div> """ %(leerlingVoornaam,leerlingVoornaam,leerlingKlas[0])
        eindHTML= u"""
        </div>
        </div>
        </body>
        </html>"""

        mapNaam = os.getcwd() + "/assets/www/rooster/%s/%s/" % (leerlingKlas[:2],leerlingKlas[2:])
        if not os.path.exists(mapNaam):
            os.makedirs(mapNaam)
        NieuwBestand = open("%s%s.html" % (mapNaam, leerlingVoornaamNormalised+leerlingAchternaamNormalised),"w")
        NieuwBestand.write((beginHTML + u'\n<table style="width:100%;"><tr>' + roosterTabel + u"\n" + eindHTML).encode('utf8'))
        NieuwBestand.close()
        leerlingenlijst.append((leerlingKlas,leerlingVoornaam,leerlingAchternaam))
        llnr += 1
    LLbestand = open("leerlingenlijst","w")
    LLbestand.write(pickle.dumps(leerlingenlijst))
    LLbestand.close()

def leerlingenlijsten():
    print "================="
    print "Setup"
    print "================="
    Bestand = open("leerlingenlijst","r")
    leerlingenlijst = pickle.loads(Bestand.read())
    Bestand.close()

    uniekeKlassen, uniekeNiveaus, leerlingenhtml, klassenhtml = [], [], [], []


    for leerling in leerlingenlijst:
        if leerling[0] not in uniekeKlassen:
            uniekeKlassen.append(leerling[0])
        if leerling[0][:2] not in uniekeNiveaus:
            uniekeNiveaus.append(leerling[0][:2])
    uniekeKlassen.sort()

    for leerling in leerlingenlijst:
        strAchternaam = leerling[2].split(" ")
        strAchternaam.append(strAchternaam.pop(0))
        htmlstring = u"""<li data-theme="c">
    <a href="../../index.html" data-ajax="false" onclick="localStorage.leerling = 'rooster/%s/%s/%s.html #rooster';" data-transition="none">
    %s
    </a>
    </li>""" % (leerling[0][:2], leerling[0][2],(''.join(x for x in unicodedata.normalize('NFKD', leerling[1]+leerling[2]) if x in (string.ascii_letters + "-"))).replace(" ","%20"),leerling[1]+" "+" ".join(strAchternaam))
        leerlingenhtml.append((leerling[0],htmlstring,leerling[1].encode("utf8")))
        print "%s %s, %s"% (leerling[1]," ".join(strAchternaam),leerling[0])
    leerlingenhtml = sorted(leerlingenhtml, key=lambda k: k[1])

    yolo = []
    for klas in uniekeKlassen:
        grotehtmlstring = ""
        for leerling in leerlingenhtml:
            if leerling[0] == klas:
                grotehtmlstring += leerling[1]

        htmlstring = u"""
    <div data-role="collapsible" data-inset="true">
    <h2>%s</h2>
    <ul data-role="listview">
    %s
    </ul>
    </div><!-- /collapsible -->
    """ % (klas, grotehtmlstring)

        klassenhtml.append((klas,htmlstring))

    for niveau in uniekeNiveaus:
        grotehtmlstring = ""
        for klas in klassenhtml:
            if klas[0][:2] == niveau:
                grotehtmlstring += klas[1]
        uiteindelijkeHTML = u"""<!DOCTYPE html>
    <html>
    <head>
            <title>A6</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta charset="utf-8">
            <link rel="stylesheet" href="../../css/jquery.mobile-1.2.0.min.css" />
            <script src="../../js/cordova-2.3.0.js"></script>
            <script src="../../js/jquery.min.js"></script>
            <script src="../../js/jquery.mobile-1.2.0.min.js"></script>
    <body>

    <div data-role="page" >

            <div data-role="header" data-position="fixed">
            <a href="../../index.html" data-transition="none" data-icon="arrow-l" data-theme="a" data-role="button">Terug</a>
                    <h1>Vandaag</h1>
            </div><!-- /header -->

            <div data-role="content">
                    <h1 style="text-align:center">%s</h1>
                    <div data-role="collapsible-set" data-theme="c" data-content-theme="c" data-collapsed-icon="arrow-r" data-expanded-icon="arrow-d" style="margin:0"> %s      </div><!-- /collapsible -->
                            </div><!-- /content -->
            </div><!-- /page -->

    </body>""" % (niveau, grotehtmlstring)
        HTML = open("%s/assets/www/rooster/%s/setup.html" % (os.getcwd(),niveau),"w")
        HTML.write(uiteindelijkeHTML.encode("utf8"))
        HTML.close()
    print "Setups klaar."
def leraarlijsten():
    print "================="
    print "Setup"
    print "================="
    Bestand = open("lerarenlijst","r")
    lerarenlijst = pickle.loads(Bestand.read())
    Bestand.close()
    html = ""
    for leraar in lerarenlijst:
        html += """<li data-theme="c">
    <a href="../../index.html" data-ajax="false" onclick="localStorage.leerling = 'rooster/leraar/%s.html #rooster';" data-transition="none">
    %s
    </a>
    </li>""" % (''.join(x for x in unicodedata.normalize('NFKD', leraar) if x in (string.ascii_letters + "-")),leraar)

    html = """<!DOCTYPE html>
    <html>
    <head>
    <title>A6</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="utf-8">
    <link rel="stylesheet" href="../../css/jquery.mobile-1.2.0.min.css" />
    <script src="../../js/cordova-2.3.0.js"></script>
    <script src="../../js/jquery.min.js"></script>
    <script src="../../js/jquery.mobile-1.2.0.min.js"></script>
<body>

<div data-role="page" >

<div data-role="header" data-position="fixed">
<a href="../../index.html" data-transition="none" data-icon="arrow-l" data-theme="a" data-role="button">Terug</a>
<h1>Vandaag</h1>
</div><!-- /header -->

<div data-role="content">
<h1 style="text-align:center">Leraren</h1>
<ul data-role="listview" data-inset="true">
%s
</ul>
</div><!-- /content -->
</div><!-- /page -->

</body>""" % html

    HTML = open("%s/assets/www/rooster/leraar/setup.html" % os.getcwd(),"w")
    HTML.write(html.encode("utf8"))
    HTML.close()

def leraarverbouwing():
    #Bestand openen en de inhoud in een string dumpen
    print "================="
    print "Lerarenroosters"
    print "================="
    llnr = 0
    lerarenlijst = []
    while llnr < 95: #Tot 95, omdat 404 detection niet echt vlekkeloos werkt
        RoosterBestand = urllib.urlopen("https://files.itslearning.com/data/423/3904/P3docenten/%s.html"%str(llnr+1))
        beginRooster = RoosterBestand.read().decode("windows-1252")
        RoosterBestand.close()

        if beginRooster[:14] == """<!DOCTYPE html""":
            print "Done: 404 reached"
            break


        #Slecht geformatteerd rooster inladen
        nuttigGedeelteRooster = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[2]

        #leraarKlas = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[1].lstrip().split("\n")[0].strip()[1:]
        leraarVoornaam = nuttigGedeelteRooster.split("</TD>")[0].lstrip().rstrip()
        leraarVoornaamNormalised = ''.join(x for x in unicodedata.normalize('NFKD', leraarVoornaam) if x in (string.ascii_letters + "-")) #Don't ask.
        print "%d: %s" % (llnr+1, leraarVoornaam)

        roosterTabel = nuttigGedeelteRooster.split("<table>")[1]

        #deze zooi is belangrijk
        for i in range(9):
            roosterTabel = roosterTabel.replace("u0%s"%str(i+1),str(i+1))

        Replacements = [("Uur\Dag",""),("MTU","mt"),("<br>","<br />"),("maandag","Ma"),("dinsdag","Di"),("woensdag","Wo"),("donderdag","Do"),("vrijdag","Vr"),("teamvergadering","team")]

        for r in Replacements:
            roosterTabel = roosterTabel.replace(r[0],r[1])

        roosterTabel = roosterTabel.split("""<td style="background-color: rgb(220, 220, 220);">u10</td>""")[0].rstrip().rstrip("<tr>")
        roosterTabel += "\n</table>"
        roosterUren = roosterTabel.split("<tr>")[2:]
        for i in range(len(roosterUren)):
            roosterUren[i] = "<tr>" + roosterUren[i]
            roosterDagen = roosterUren[i].split("<td>")
            for e in range(len(roosterDagen[1:])):
                try:
                    vak = roosterDagen[e+1].split("<br />")[1].split(" ")[0]
                    klas = roosterDagen[e+1].split("<br />")[0].replace(vak,"")
                    lokaal = roosterDagen[e+1].split("<br />")[1].split(" ")[1][1:]

                    roosterDagen[e+1] = "%s<br />%s %s"%(klas,vak,lokaal)
                except: pass
                roosterDagen[e+1] = ('<td id="TTVLd%su%s">' % (str(e+1),str(i+1))) + roosterDagen[e+1].lstrip("1")
            roosterUren[i] = "".join(roosterDagen)

        RoosterTabel = "".join(roosterTabel.split("<tr>")[:2] + roosterUren)
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
                    <div data-role="content" id="rooster">
                    <div id="pauze" style="visibility:hidden;">%s</div> """ %(leraarVoornaam,leraarVoornaam,N)
        eindHTML= u"""
        </div>
        </div>
        </body>
        </html>"""

        mapNaam = os.getcwd() + "/assets/www/rooster/leraar/"
        if not os.path.exists(mapNaam):
            os.makedirs(mapNaam)
        NieuwBestand = open(mapNaam + "%s.html" % leraarVoornaamNormalised,"w")
        NieuwBestand.write((beginHTML + u'\n<table style="width:100%;"><tr>' + RoosterTabel + u"\n" + eindHTML).encode('utf8'))
        NieuwBestand.close()
        lerarenlijst.append(leraarVoornaam)
        llnr += 1
    LLbestand = open("lerarenlijst","w")
    LLbestand.write(pickle.dumps(lerarenlijst))
    LLbestand.close()
    #LerarenParser bestaat nog niet, dan komt nog hopelijk. Roosters binnenhalen is in ieder geval al iets.

def onderverbouwing():
    #Bestand openen en de inhoud in een string dumpen
    print "================="
    print "Onderbouwroosters"
    print "================="
    llnr = 0
    onderbouwlijst = []
    while llnr < 16: #Tot 16, omdat 404 detection niet echt vlekkeloos werkt
        RoosterBestand = urllib.urlopen("https://files.itslearning.com/data/423/3904/P3onderbouw/%s.html"%str(llnr+1))
        beginRooster = RoosterBestand.read().decode("windows-1252")
        RoosterBestand.close()

        if beginRooster[:14] == """<!DOCTYPE html""":
            print "Done: 404 reached"
            break


        #Slecht geformatteerd rooster inladen
        nuttigGedeelteRooster = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[1]
        #print nuttigGedeelteRooster ##debug

        onderbouwKlas = beginRooster.split('<TD BGCOLOR="DCDCDC" NOWRAP style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[1].lstrip().split("\n")[0].strip()[1:]
        #onderbouwVoornaam = nuttigGedeelteRooster.split("</TD>")[0].lstrip().rstrip()
        #onderbouwVoornaamNormalised = ''.join(x for x in unicodedata.normalize('NFKD', onderbouwVoornaam) if x in (string.ascii_letters + "-")) #Don't ask.
        print "%d: %s" % (llnr+1, onderbouwKlas)

        roosterTabel = nuttigGedeelteRooster.split("<table>")[1]
        #print roosterTabel ##debug

        #deze zooi is belangrijk
        for i in range(9):
            roosterTabel = roosterTabel.replace("u0%s"%str(i+1),str(i+1))

        Replacements = [("Uur\Dag",""),("MTU","mt"),("<br>","<br />"),("maandag","Ma"),("dinsdag","Di"),("woensdag","Wo"),("donderdag","Do"),("vrijdag","Vr")]

        for r in Replacements:
            roosterTabel = roosterTabel.replace(r[0],r[1])
        
        onderbouwNiveau = ""
        #####DIT MOET DUS OP DE SCHOP:
        #####- TTVL Toewijzing ##BAM! DONE. IK HEB NOG EENS WAT GELEERD OP SCHOOL!
        #####- Rooster ombouwen? Verticaal ipv horizontaal... Beetje dom dat ik dat niet meteen door had :$
        #roosterTabel = roosterTabel.split("""<td style="background-color: rgb(220, 220, 220);">u10</td>""")[0].rstrip().rstrip("<tr>")
        roosterTabel += "\n</table>"
        roosterUren = roosterTabel.split("<tr>")[2:]
        for i in range(len(roosterUren)):
            roosterUren[i] = "<tr>" + roosterUren[i]
            roosterDagen = roosterUren[i].split("<td>")
            for e in range(len(roosterDagen[1:])):
                roosterDagen[e+1] = ('<td id="TTVLd%su%s">' % (str(e+1),str(i+1))) + roosterDagen[e+1]
            roosterUren[i] = "".join(roosterDagen)

        roosterTabel = "".join(roosterUren)


        ##TTVL Toewijzing
        ##We gaan even sophisticated die lettertjes toewijzen.
        i = onderbouwKlas[:1] ##Stap 1: We pakken de klas, nemen de eerste letter (Trouwens, Clusterfuck alert: Altijd als ik het eerste element wil, moet ik het nulde nemen. Bij een string moet ik dan wel 1 doen ipv 0. ARGH.)
        if i == "A":          ##Stap 2: Met een standaard if/elif/else-structuurtje vergelijken we de eerste letter van 't rooster met een A, G of H. A en G krijgen "A", H krijgt "H".
            onderbouwNiveau = "A"
        elif i == "G":
            onderbouwNiveau = "A"
        else:
            onderbouwNiveau = "H"
        print onderbouwNiveau
        ##En toen dacht je: Shit, Rene heeft al bij bovenbouw Havo en VWO moeten scheiden, ik had hier alleen nog maar Gymnasium eruit moeten halen... Damn it.
        ##But it works!

        beginHTML = u"""<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <title>%s</title>
                <link rel="stylesheet" href="../../jquery.mobile-1.2.0.min.css" />
                <script src="../../js.min.js">
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
                    <div data-role="content" id="rooster">
                    <div id="pauze" style="visibility:hidden;">%s</div> """ %(onderbouwKlas,onderbouwKlas,onderbouwNiveau)
        eindHTML= u"""
        </div>
        </div>
        </body>
        </html>"""

        print onderbouwKlas
        mapNaam = os.getcwd() + "/assets/www/rooster/onderbouw/"
        if not os.path.exists(mapNaam):
            os.makedirs(mapNaam)
        NieuwBestand = open(mapNaam + "%s.html" % onderbouwKlas,"w")
        NieuwBestand.write((beginHTML + u'\n<table style="width:100%;">' + roosterTabel + u"\n" + eindHTML).encode('utf8'))
        NieuwBestand.close()
        onderbouwlijst.append(onderbouwKlas)
        llnr += 1
    LLbestand = open("onderbouwlijst","w")
    LLbestand.write(pickle.dumps(onderbouwlijst))
    LLbestand.close()
    #OnderbouwParser bestaat nog niet, dan komt nog hopelijk. Roosters binnenhalen is in ieder geval al iets.

def afsluiten():
    venster.destroy()

def all_starting():
    leerlingverbouwing()
    leerlingenlijsten()
    onderverbouwing()
    leraarverbouwing()
    welkom.config(text="Alle roosters voltooid.")
    start3.config(text="Sluit.", command=afsluiten)

def leerling_starting():
    leerlingverbouwing()
    leerlingenlijsten()
    welkom.config(text="Bovenbouwroosters voltooid.")
    start.config(text="Sluit.", command=afsluiten)

def leraar_starting():
    leraarverbouwing()
    leraarlijsten()
    welkom.config(text="Lerarenroosters voltooid.")
    start2.config(text="Sluit.", command=afsluiten)
    
def onderbouw_starting():
    onderverbouwing()
    welkom.config(text="Onderbouwroosters voltooid.")
    start4.config(text="Sluit.", command=afsluiten)

## GUI
venster = Tk()

welkom = Label(master=venster, text="Welkom", font=("Arial",24))
start3 = Button(master=venster, text="ALLES", font=("Arial",60), command=all_starting)
start = Button(master=venster, text="Bovenbouwleerlingen", command=leerling_starting)
start4 = Button(master=venster, text="Onderbouwleerlingen", command=onderbouw_starting)
start2 = Button(master=venster, text="Leraren", command=leraar_starting)
welkom.pack()
start3.pack(padx=5, pady=5, fill=X)
start4.pack(padx=5, pady=5, fill=X)
start.pack(padx=5, pady=5, fill=X)
start2.pack(padx=5, pady=5, fill=X)

venster.minsize(width=250, height=80)

venster.title("RoosterParser")
#venster.iconbitmap(default="favicon.ico")
venster.mainloop()
