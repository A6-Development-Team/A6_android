#-------------------------------------------------------------------------------
#A6_android: Roosterparser
#MijnheerNeen
#-------------------------------------------------------------------------------
import urllib

#Bestand openen en de inhoud in een string dumpen
RoosterBestand = open("Zermelo Rasterscherm.htm","r")
beginRooster = RoosterBestand.read()
RoosterBestand.close()

#Slecht geformatteerd rooster inladen
nuttigGedeelteRooster = beginRooster.split('<td bgcolor="DCDCDC" nowrap="" style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[3]

leerlingKlas = beginRooster.split('<td bgcolor="DCDCDC" nowrap="" style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[1].lstrip().split("\n")[0]
leerlingAchternaam = beginRooster.split('<td bgcolor="DCDCDC" nowrap="" style="border: none; font-family: Arial; font-size: 20px; font-weight: bold; padding: 5px;">')[2].lstrip().split("\n")[0]
leerlingVoornaam = nuttigGedeelteRooster.split("</td>")[0].lstrip().rstrip()

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

for i in range(9):
    roosterTabel = roosterTabel.replace("u0%s"%str(i+1),str(i+1))
roosterTabel = roosterTabel.replace("""<tr>
    <td style="background-color: rgb(220, 220, 220);">Uur\Dag</td>
    <td style="background-color: rgb(220, 220, 220);">maandag</td>
    <td style="background-color: rgb(220, 220, 220);">dinsdag</td>
    <td style="background-color: rgb(220, 220, 220);">woensdag</td>
    <td style="background-color: rgb(220, 220, 220);">donderdag</td>
    <td style="background-color: rgb(220, 220, 220);">vrijdag</td>
  </tr>""","""<tr>
    <td style="background-color: rgb(220, 220, 220);"></td>
    <td style="background-color: rgb(220, 220, 220);">Ma</td>
    <td style="background-color: rgb(220, 220, 220);">Di</td>
    <td style="background-color: rgb(220, 220, 220);">Wo</td>
    <td style="background-color: rgb(220, 220, 220);">Do</td>
    <td style="background-color: rgb(220, 220, 220);">Vr</td>
  </tr>""")
roosterTabel = roosterTabel.replace("MTU","mt")
roosterTabel = roosterTabel.replace("<br>","<br />")
roosterTabel = roosterTabel.split("""  <tr>
    <td style="background-color: rgb(220, 220, 220);">u10</td>""")[0]
roosterTabel = roosterTabel + "\n</table>"
beginHTML = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>%s</title>
        <link rel="stylesheet" href="jquery.mobile-1.2.0.min.css" />
        <script src="js.min.js">
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
eindHTML= """
</body>
</html>"""

NieuwBestand = open("%s.htm" % leerlingVoornaam,"w")
NieuwBestand.write(beginHTML + '\n<table width="100%">' + roosterTabel + "\n" + eindHTML)
NieuwBestand.close()
