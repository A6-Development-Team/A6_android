var n, tijdNu = new Date();
function TijdVolgendeUur() {
    n = document.getElementById("pauze").innerHTML;
    tijdNu = new Date();
	
	if (n == "n") {
        n = LeraarPauze();
	} else if (n == "H" || n == "A") {
        n += n;
    }

    var tv = TijdVerschil(), t = tv[0], u = tv[1]; //beetje uitgedund: we willen functies zo weinig mogelijk aanroepen
    if (tijdNu.getDay() != 0 && tijdNu.getDay() != 6 && t > 0) {
        var hv = VakLokaal(u), hu = hv[0], hl = hv[2];
        hv = hv[1];
        var vv = VakLokaal(u + 1), vu = vv[0], vl = vv[2];
        vv = vv[1];

        WriteHTML(hu, hl, hv, vu, vl, vv, t + " min"); //code inspection, y u so Stasi
    } else if (n != undefined) { //undefined of andere falsy waarden afvangen
        WriteHTML();
    }

}

function LeraarPauze() {
    var p1 = document.getElementById("TTVLd" + tijdNu.getDay() + "u" + 3).innerHTML, pauze1;
    if (p1 == "&nbsp;") {
        pauze1 = "A"
    } //Yolo
    else if (p1.split("</br>")[0][1] == "H") {
        pauze1 = "H"
    }
    else {
        pauze1 = "A"
    }
    var p2 = document.getElementById("TTVLd" + tijdNu.getDay() + "u" + 6).innerHTML, pauze2;
    if (p2 == "&nbsp;") {
        pauze2 = "A"
    } //Yolo
    else if (p2.split("</br>")[0][1] == "H") {
        pauze2 = "H"
    }
    else {
        pauze2 = "A"
    }
    return pauze1.concat(pauze2 + "L"); //Die L zorgt ervoor dat mijn return een length heeft van 3, wat ik later kan gebruiken om terug te halen dat het om een leraar gaat
}

function TijdVerschil() {
    var lesUren = [], tijdVerschil;
    lesUren[0] = {uur:8, minuut:10}; //1e uur
    lesUren[1] = {uur:9, minuut:0}; //2e uur
    lesUren[2] = {uur:9, minuut:50}; //HAVO: pauze 1, VWO: 3e uur
    lesUren[3] = (n[0] == "H") ? {uur:10, minuut:5} : {uur:10, minuut:40};
    lesUren[4] = {uur:10, minuut:55}; //4e uur
    lesUren[5] = {uur:11, minuut:45}; //HAVO: pauze 2, VWO: 5e uur
    lesUren[6] = (n[1] == "H") ? {uur:12, minuut:10} : {uur:12, minuut:35};
    lesUren[7] = {uur:13, minuut:0}; //6e uur
    lesUren[8] = {uur:13, minuut:50}; //7e uur
    lesUren[9] = {uur:14, minuut:40}; //pauze 3
    lesUren[10] = {uur:14, minuut:50}; //8e uur
    lesUren[11] = {uur:15, minuut:40}; //9e uur
    lesUren[12] = {uur:16, minuut:30}; //einde lesdag

    for (var i = 0; i < lesUren.length; i++) {
        tijdVerschil = (lesUren[i].uur - tijdNu.getHours()) * 60 + (lesUren[i].minuut - tijdNu.getMinutes());
        if (tijdVerschil > 0) {
            return [tijdVerschil, i];
        }
    }
    return [0, 12];
} //geeft verschil in tijd tussen nu en eind les, of 0 bij afgelopen les, alsmede de index van de les
function VakLokaal(u) {
    var l, v;
        switch (u) {
            case 0 || 13:
                u = ""; break;
            case ((n[0]=="H") ? 3 : 4): //BAM, zowel HAVO en VWO pauzes in 1 case gesodekankerd.
                u = "P1"; v = "Pauze"; break;
            case ((n[1]=="H") ? 6 : 7):
                u = "P2"; v = "Pauze"; break;
            case 10:
                u = "P3"; v = "Pauze"; break;
            default:
                if (u > 9) {u -= 3}
                else if (u > ((n=="H") ? 5 : 6)) {u -= 2}
                else if (u > ((n=="H") ? 2 : 3)) {u -= 1}//u bijstellen voor uren na de pauzes

                var roosterinhoud = document.getElementById("TTVLd" + tijdNu.getDay() + "u" + u);
                if (roosterinhoud != null) {
                    v = roosterinhoud.innerHTML;
                } else {
                    v = "&nbsp;";
                }
                if (v != "&nbsp;") {
                    if (n.length == 3){ //leraar
                        l = v.split("<br>")[1].split(" ")[1];
                        v = v.split("<br>")[0] + " " + v.split("<br>")[1].split(" ")[0];
                    } else { //leerling
                    l = v.split("<br>")[2].replace("1","");
                    v = VakReplace(v.split("<br>")[0]);
                    }
                } else {
                    v = "";
                }
        }
    return [u, v, l];
} //plukt de lessen uit de tabel
function VakReplace(str) {
    var vakken = {
        "wisA":"Wiskunde A", "wisB":"Wiskunde B", "wisC":"Wiskunde C", "wisD":"Wiskunde D", "nat":"Natuurkunde", "schk":"Scheikunde",
        "biol":"Biologie", "in":"Informatica", "lit":"Literatuur", "ak":"Aardrijkskunde", "ges":"Geschiedenis", "maw":"Maatschappijwet.",
        "maat":"Maatschappijleer", "mu":"Muziek", "econ":"Economie", "fi":"Filosofie", "m&amp;o":"M&amp;O", "nezl":"Nederlands",
        "netl":"Nederlands", "enzl":"Engels", "entl":"Engels", "duzl":"Duits", "dutl":"Duits", "fazl":"Frans",
        "fatl":"Frans", "grtl":"Grieks", "latl":"Latijn", "lo":"LO", "ckv":"CKV", "kcv":"KCV",
        "anw":"ANW", "bevo":"Bevo", "te":"Tekenen", "bsm":"BSM", "tdd":"Teamdagdeel", "mt":"Mentorles", "MTU":"Mentorles"};
    for (var i in vakken) {
        if (str == i) {
            str = str.replace(i, vakken[i]);
            break;
        }
    } //godverdomme Mier dit is valsspelen, je ramt hier serieus 4 statements op 1 regel?
    return str;
} //vervangt vakcodes voor namen
function WriteHTML(hu, hl, hv, vu, vl, vv, t) {
    document.getElementById("TTVLhu").innerHTML = hu || "-";
    document.getElementById("TTVLhv").innerHTML = hv || "------";
    document.getElementById("TTVLhl").innerHTML = hl || "-";
    document.getElementById("TTVLt").innerHTML = t || "-------";
    document.getElementById("TTVLvu").innerHTML = vu || "-";
    document.getElementById("TTVLvv").innerHTML = vv || "------";
    document.getElementById("TTVLvl").innerHTML = vl || "-";
}//schrijft de tags weg in het document: kan aangeroepen worden zonder argumenten of met "" voor elke lege tag