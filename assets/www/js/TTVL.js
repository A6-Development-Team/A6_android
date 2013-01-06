var tijdNu = new Date();

function TijdVolgendeUur() {
	var t = TijdVerschil()[0], u = TijdVerschil()[1];
    if (tijdNu.getDay() != 0 && tijdNu.getDay() != 6 && t > 0) {
        var hv = VakLokaal(u), hu = hv[0], hl = hv[2];
        hv = hv[1];
        var vv = VakLokaal(u+1), vu = vv[0], vl = vv[2];
        vv = vv[1];

        WriteHTML(hu,hl,hv,vu,vl,vv,"Nog <b>"+t+"</b> minuten tot")
    } else {
        WriteHTML(); //geen les, dan wordt er leeg geschreven.
    }
    document.getElementsByTagName("table")[0].style.visibility = "hidden";}

function TijdVerschil() {
    var lesUren = [],tijdVerschil;
    lesUren[0] = {uur : 8, minuut : 10, uurNaam : "1<sup>e</sup> uur"};     lesUren[1] = {uur : 9, minuut : 0, uurNaam : "2<sup>e</sup> uur"};
    lesUren[2] = {uur : 9, minuut : 50, uurNaam : "3<sup>e</sup> uur"};     lesUren[3] = {uur : 10, minuut : 40, uurNaam : "1<sup>e</sup> pauze"};
    lesUren[4] = {uur : 10, minuut : 55, uurNaam : "4<sup>e</sup> uur"};    lesUren[5] = {uur : 11, minuut : 45, uurNaam : "5<sup>e</sup> uur"};
    lesUren[6] = {uur : 12, minuut : 35, uurNaam : "2<sup>e</sup> pauze"};  lesUren[7] = {uur : 13, minuut : 0, uurNaam : "6<sup>e</sup> uur"};
    lesUren[8] = {uur : 13, minuut : 50, uurNaam : "7<sup>e</sup> uur"};    lesUren[9] = {uur : 14, minuut : 40, uurNaam : "3<sup>e</sup> pauze"};
    lesUren[10] = {uur : 14, minuut : 50, uurNaam : "8<sup>e</sup> uur"};   lesUren[11] = {uur : 15, minuut : 40, uurNaam : "9<sup>e</sup> uur"};
    lesUren[12] = {uur : 16, minuut : 30, uurNaam : "einde lesdag"};

    for (var i = 0; i < lesUren.length; i++) {
        tijdVerschil = (lesUren[i].uur - tijdNu.getHours()) * 60 + (lesUren[i].minuut - tijdNu.getMinutes());
        if (tijdVerschil > 0) {
            return [tijdVerschil, i];
        }
    }
    return [0, 12];} //geeft verschil in tijd tussen nu en eind les, of 0 bij afgelopen les, alsmede de index van de les
function VakLokaal(u){
    var l,v;
    switch(u){ //hier wordt de shit voor het volgende uur ingevuld
        case 0 || 13:
            u = ""; break;
        case 4:
            u = "P1";v = "Pauze"; break;
        case 7:
            u = "P2"; v = "Pauze"; break;
        case 10:
            u = "P3"; v = "Pauze"; break;
        default:
            if (u > 3) {u -= 1} //hu bijstellen voor uren na de pauzes
            if (u > 6) {u -= 2}
            if (u > 9) {u -= 3}
            v = document.getElementById("TTVLd" + tijdNu.getDay() + "u" + u).innerHTML;
            if (v !="&nbsp;"){
                l = v.split("<br>")[2].replace("1","");
                v = VakReplace(v.split("<br>")[0]);
            }
    }
    return [u,v,l];
} //plukt de lessen uit de tabel
function VakReplace(str) {
    var vakken = {
        "wisA":"Wiskunde A",    "wisB":"Wiskunde B",    "wisC":"Wiskunde C",    "wisD":"Wiskunde D",    "nat":"Natuurkunde",    "schk":"Scheikunde",
        "biol":"Biologie",      "in":"Informatica",     "lit":"Literatuur",     "ak":"Aardrijkskunde",  "ges":"Geschiedenis",   "maw":"Maatschappijwetenschappen",
        "maat":"Maatschappijleer","mu":"Muziek",        "econ":"Economie",      "fi":"Filosofie",       "m&o":"M&O",            "nezl":"Nederlands",
        "netl":"Nederlands",    "enzl":"Engels",        "entl":"Engels",        "duzl":"Duits",         "dutl":"Duits",         "fazl":"Frans",
        "fatl":"Frans",         "grtl":"Grieks",        "latl":"Latijn",        "lo":"LO",              "ckv":"CKV",            "kcv":"KCV",
        "anw":"ANW",            "bevo":"Bevo",          "te":"Tekenen",         "bsm":"BSM",            "tdd":"Teamdagdeel",    "mt":"Mentorles"};
    for (var i in vakken){if (str == vakken[i]){ str = str.replace(i, vakken[i]);break;}}
    return str;} //vervangt vakcodes voor namen
function WriteHTML(hu,hl,hv,vu,vl,vv,t){
    document.getElementById("TTVLhu").innerHTML = hu || "-";
    document.getElementById("TTVLhv").innerHTML = hv || "-----";
    document.getElementById("TTVLhl").innerHTML = hl || "-";
    document.getElementById("TTVLt").innerHTML = t || "-------";
    document.getElementById("TTVLvu").innerHTML = vu || "-";
    document.getElementById("TTVLvv").innerHTML = vv || "-----";
    document.getElementById("TTVLvl").innerHTML = vl || "-";} //schrijft de tags weg in het document: kan aangeroepen worden zonder argumenten of met "" voor elke lege tag