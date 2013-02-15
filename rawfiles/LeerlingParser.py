import pickle, string, os, unicodedata

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
		<div data-role="collapsible-set" data-theme="c" data-content-theme="c" data-collapsed-icon="arrow-r" data-expanded-icon="arrow-d" style="margin:0"> %s 		</div><!-- /collapsible -->
			</div><!-- /content -->
	</div><!-- /page -->

</body>""" % (niveau, grotehtmlstring)
    HTML = open("%s/assets/www/rooster/%s/setup.html" % (os.getcwd(),niveau),"w")
    HTML.write(uiteindelijkeHTML.encode("utf8"))
    HTML.close()