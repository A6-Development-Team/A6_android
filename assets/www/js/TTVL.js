var tijdNu = new Date();

function TijdVolgendeUur() {
	n = document.getElementById("pauze").innerHTML;
    var tv = TijdVerschil(), t = tv[0], u = tv[1]; //beetje uitgedund: we willen functies zo weinig mogelijk aanroepen
    if (tijdNu.getDay() != 0 && tijdNu.getDay() != 6 && t > 0) {
        var hv = VakLokaal(u), hu = hv[0], hl = hv[2];
        hv = hv[1];
        var vv = VakLokaal(u+1), vu = vv[0], vl = vv[2];
        vv = vv[1];

        WriteHTML(hu,hl,hv,vu,vl,vv,"Over <b>"+t+"</b> minuten"); //code inspection, y u so Stasi
    } else if(n != undefined){ //undefined of andere falsy waarden afvangen
        var element = document.getElementById("comingupcard");
        element.parentNode.removeChild(element);
        
    }
    /*Voor nu rammen we dat rooster wel even in een card, geen tijd of zin om uit te zoeken hoe we dat even netjes wegwerken. document.getElementsByTagName("table")[0].style.visibility = "hidden";*/}

function TijdVerschil() {
    var lesUren = [],tijdVerschil;
    if (n == "A"){
    lesUren[0] = {uur : 8, minuut : 10, uurNaam : "1<sup>e</sup> uur"};     lesUren[1] = {uur : 9, minuut : 0, uurNaam : "2<sup>e</sup> uur"};
    lesUren[2] = {uur : 9, minuut : 50, uurNaam : "3<sup>e</sup> uur"};     lesUren[3] = {uur : 10, minuut : 40, uurNaam : "1<sup>e</sup> pauze"};
    lesUren[4] = {uur : 10, minuut : 55, uurNaam : "4<sup>e</sup> uur"};    lesUren[5] = {uur : 11, minuut : 45, uurNaam : "5<sup>e</sup> uur"};
    lesUren[6] = {uur : 12, minuut : 35, uurNaam : "2<sup>e</sup> pauze"};  lesUren[7] = {uur : 13, minuut : 0, uurNaam : "6<sup>e</sup> uur"};
    lesUren[8] = {uur : 13, minuut : 50, uurNaam : "7<sup>e</sup> uur"};    lesUren[9] = {uur : 14, minuut : 40, uurNaam : "3<sup>e</sup> pauze"};
    lesUren[10] = {uur : 14, minuut : 50, uurNaam : "8<sup>e</sup> uur"};   lesUren[11] = {uur : 15, minuut : 40, uurNaam : "9<sup>e</sup> uur"};
    lesUren[12] = {uur : 16, minuut : 30, uurNaam : "einde lesdag"};}
    else if (n == "H"){
    lesUren[0] = {uur : 8, minuut : 10};     lesUren[1] = {uur : 9, minuut : 0};
    lesUren[2] = {uur : 9, minuut : 50};     lesUren[3] = {uur : 10, minuut : 5};
    lesUren[4] = {uur : 10, minuut : 55};    lesUren[5] = {uur : 11, minuut : 45};
    lesUren[6] = {uur : 12, minuut : 10};  lesUren[7] = {uur : 13, minuut : 0};
    lesUren[8] = {uur : 13, minuut : 50};    lesUren[9] = {uur : 14, minuut : 40};
    lesUren[10] = {uur : 14, minuut : 50};   lesUren[11] = {uur : 15, minuut : 40};
    lesUren[12] = {uur : 16, minuut : 30};}
    for (var i = 0; i < lesUren.length; i++) {
        tijdVerschil = (lesUren[i].uur - tijdNu.getHours()) * 60 + (lesUren[i].minuut - tijdNu.getMinutes());
        if (tijdVerschil > 0) {
            return [tijdVerschil, i];
        }
    }
    return [0, 12];} //geeft verschil in tijd tussen nu en eind les, of 0 bij afgelopen les, alsmede de index van de les
function VakLokaal(u){
    var l, v;
	if (n == "H"){
    switch(u){ //hier wordt de shit voor het volgende uur ingevuld
        case 0 || 13:
            u = ""; break;
        case 3:
            u = "P1";v = "Pauze"; break;
        case 6:
            u = "P2";v = "Pauze"; break;
        case 10:
            u = "P3"; v = "Pauze"; break;
        default:
        	if (u > 9) {u -= 3}
        	else if (u > 5) {u -= 2}
            else if (u > 2) {u -= 1} //hu bijstellen voor uren na de pauzes
            

          	var roosterinhoud = document.getElementById("TTVLd" + tijdNu.getDay() + "u" + u);
          	if (roosterinhoud != null){
            v = roosterinhoud.innerHTML;}
            else{v="&nbsp;"}
            if (v !="&nbsp;"){
                l = v.split("<br>")[2].replace("1","");
                v = VakReplace(v.split("<br>")[0]);
            } else {
                v = "";
            }
    }} else{
        switch(u){ //hier wordt de shit voor het volgende uur ingevuld
            case 0 || 13:
                u = ""; break;
            case 4:
                u = "P1";v = "Pauze"; break; //Deze mogelijke fallthroughs zijn bewust...
            case 7:
                u = "P2";v = "Pauze"; break;
            case 10:
                u = "P3"; v = "Pauze"; break;
            default:
                    if (u > 9) {u -= 3}
                    else if (u > 6) {u -= 2}
                    else if (u > 3) {u -= 1}//hu bijstellen voor uren na de pauzes


                var roosterinhoud = document.getElementById("TTVLd" + tijdNu.getDay() + "u" + u);
                if (roosterinhoud != null){
                    v = roosterinhoud.innerHTML;}
                else{v="&nbsp;"}
                if (v !="&nbsp;"){
                    l = v.split("<br>")[2].replace("1","");
                    v = VakReplace(v.split("<br>")[0]);
                } else {
                    v = "";
                }
    }

}
    return [u,v,l];
} //plukt de lessen uit de tabel
function VakReplace(str) {
    var vakken = {
        "wisA":"Wiskunde A",    "wisB":"Wiskunde B",    "wisC":"Wiskunde C",    "wisD":"Wiskunde D",    "nat":"Natuurkunde",    "schk":"Scheikunde",
        "biol":"Biologie",      "in":"Informatica",     "lit":"Literatuur",     "ak":"Aardrijkskunde",  "ges":"Geschiedenis",   "maw":"Maatschappijwetenschappen",
        "maat":"Maatschappijleer","mu":"Muziek",        "econ":"Economie",      "fi":"Filosofie",       "m&amp;o":"M&O",        "nezl":"Nederlands",
        "netl":"Nederlands",    "enzl":"Engels",        "entl":"Engels",        "duzl":"Duits",         "dutl":"Duits",         "fazl":"Frans",
        "fatl":"Frans",         "grtl":"Grieks",        "latl":"Latijn",        "lo":"LO",              "ckv":"CKV",            "kcv":"KCV",
        "anw":"ANW",            "bevo":"Bevo",          "te":"Tekenen",         "bsm":"BSM",            "tdd":"Teamdagdeel",    "mt":"Mentorles"};
    for (var i in vakken){
        if (str == i){
            str = str.replace(i, vakken[i]);
            break;
        }
    } //godverdomme Mier dit is valsspelen, je ramt hier serieus 4 statements op 1 regel?
    return str;} //vervangt vakcodes voor namen
function WriteHTML(hu,hl,hv,vu,vl,vv,t){
    document.getElementById("TTVLhu").innerHTML = hu || "-";
    document.getElementById("TTVLhv").innerHTML = hv  || "------";
    document.getElementById("TTVLhl").innerHTML = hl || "-";
    document.getElementById("TTVLt").innerHTML = t || "-------";
    document.getElementById("TTVLvu").innerHTML = vu || "-";
    document.getElementById("TTVLvv").innerHTML = vv || "------";
    document.getElementById("TTVLvl").innerHTML = vl || "-";}//schrijft de tags weg in het document: kan aangeroepen worden zonder argumenten of met "" voor elke lege tag