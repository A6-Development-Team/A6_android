function VakReplace(str) {
    str = str.replace("wisA","Wiskunde A");
    str = str.replace("wisB","Wiskunde B");
    str = str.replace("wisC","Wiskunde C");
    str = str.replace("wisD","Wiskunde D");
    str = str.replace("nat","Natuurkunde");
    str = str.replace("schk","Scheikunde");
    str = str.replace("biol","Biologie");
    str = str.replace("in","Informatica");
    str = str.replace("lit","Literatuur");
    str = str.replace("ak","Aardrijkskunde");
    str = str.replace("ges","Geschiedenis");
    str = str.replace("maw","Maatschappijwetenschappen");
    str = str.replace("maat","Maatschappijleer");
    str = str.replace("mu","Muziek");
    str = str.replace("econ","Economie");
    str = str.replace("fi","Filosofie");
    str = str.replace("m&o","M&O");
    str = str.replace("nezl","Nederlands");
    str = str.replace("netl","Nederlands");
    str = str.replace("enzl","Engels");
    str = str.replace("entl","Engels");
    str = str.replace("duzl","Duits");
    str = str.replace("dutl","Duits");
    str = str.replace("fazl","Frans");
    str = str.replace("fatl","Frans");
    str = str.replace("grtl","Grieks");
    str = str.replace("latl","Latijn");
    str = str.replace("lo","LO");
    str = str.replace("ckv","CKV");
    str = str.replace("kcv","KCV");
    str = str.replace("anw","ANW");
    str = str.replace("bevo","Bevo");
    str = str.replace("te","Tekenen");
    str = str.replace("bsm","BSM");
    str = str.replace("tdd","Teamdagdeel");
    return str;

}
function TijdVolgendeUur() {
	var tijdNu = new Date(),
	tijdVolgendeUur = new Date(),
	lesUren = [],
    tijdVerschil;
	lesUren[0] = {
		uur : 8,
		minuut : 10,
		uurNaam : "1<sup>e</sup> uur"
	};
	lesUren[1] = {
		uur : 9,
		minuut : 0,
		uurNaam : "2<sup>e</sup> uur"
	};
	lesUren[2] = {
		uur : 9,
		minuut : 50,
		uurNaam : "3<sup>e</sup> uur"
	};
	lesUren[3] = {
		uur : 10,
		minuut : 40,
		uurNaam : "1<sup>e</sup> pauze"
	};
	lesUren[4] = {
		uur : 10,
		minuut : 55,
		uurNaam : "4<sup>e</sup> uur"
	};
	lesUren[5] = {
		uur : 11,
		minuut : 45,
		uurNaam : "5<sup>e</sup> uur"
	};
	lesUren[6] = {
		uur : 12,
		minuut : 35,
		uurNaam : "2<sup>e</sup> pauze"
	};
	lesUren[7] = {
		uur : 13,
		minuut : 0,
		uurNaam : "6<sup>e</sup> uur"
	};
	lesUren[8] = {
		uur : 13,
		minuut : 50,
		uurNaam : "7<sup>e</sup> uur"
	};
	lesUren[9] = {
		uur : 14,
		minuut : 40,
		uurNaam : "3<sup>e</sup> pauze"
	};
	lesUren[10] = {
		uur : 14,
		minuut : 50,
		uurNaam : "8<sup>e</sup> uur"
	};
	lesUren[11] = {
		uur : 15,
		minuut : 40,
		uurNaam : "9<sup>e</sup> uur"
	};
	lesUren[12] = {
		uur : 16,
		minuut : 30,
		uurNaam : "einde lesdag"
	};

	if (tijdNu.getDay() !== 0 && tijdNu.getDay() !== 6) {
		for (var i = 0; i < lesUren.length; i++) {
			 tijdVerschil = (lesUren[i].uur - tijdNu.getHours()) * 60 + (lesUren[i].minuut - tijdNu.getMinutes());
			if (tijdVerschil > 0) {
				tijdVolgendeUur.setHours(lesUren[i].uur);
				tijdVolgendeUur.setMinutes(lesUren[i].minuut);
				break;
			}
		}
	} else {
		 tijdVerschil = 0
	}

	if (tijdVerschil > 0) {

		var lesUur = i;
		if (lesUur > 3) {
			lesUur -= 1;
			if (lesUur > 5) {
				lesUur -= 1;
				if (lesUur > 7) {
					lesUur -= 1;
					}
				}
			}

		var TTVLtag = "TTVLd" + tijdNu.getDay() + "u" + lesUur, TTVLvak, TTVLlok;

		if (lesUur > 0){


            if (document.getElementById(TTVLtag).innerHTML == "&nbsp;"){ //in geval van tussenuur/uit
				document.getElementById("TTVLhu").innerHTML = lesUur;
				document.getElementById("TTVLhv").innerHTML = "-----";
				document.getElementById("TTVLhl").innerHTML = "-"
			}else{
                TTVLvak = VakReplace(document.getElementById(TTVLtag).innerHTML.split("<br>")[0]);
                TTVLlok = document.getElementById(TTVLtag).innerHTML.split("<br>")[2].replace("1","");
				document.getElementById("TTVLhu").innerHTML = lesUur;
                if (TTVLlok.length > 2){document.getElementById("TTVLhl").innerHTML = TTVLlok}
				else{document.getElementById("TTVLhl").innerHTML = "-"}
				document.getElementById("TTVLhv").innerHTML = TTVLvak}
			//document.getElementById("lesNu").innerHTML = MultiReplace(document.getElementById(TTVLtag).innerHTML.replace("&nbsp;","--------"),"<br>"," ")}
		}else {
        document.getElementById("TTVLhu").innerHTML = "-";
        document.getElementById("TTVLhv").innerHTML = "-----";
        document.getElementById("TTVLhl").innerHTML = "-"
        }
		
		if (i == 4 || i == 7 || i == 10){
            if (i == 4) {
                document.getElementById("TTVLhu").innerHTML = "P1"
            }
            if (i == 7) {
                document.getElementById("TTVLhu").innerHTML = "P2"
            }
            if (i == 10) {
                document.getElementById("TTVLhu").innerHTML = "P3"
            }
            document.getElementById("TTVLhv").innerHTML = "Pauze";
			document.getElementById("TTVLhl").innerHTML = "-";
		}

		document.getElementById("TTVLt").innerHTML = "Nog <b>" + tijdVerschil + " minuten</b> tot " + lesUren[i].uurNaam;
		
		TTVLtag = "TTVLd" + tijdNu.getDay() + "u" + (lesUur + 1);

		if (document.getElementById(TTVLtag).innerHTML == "&nbsp;"){ //in geval van tussenuur/uit
			document.getElementById("TTVLvu").innerHTML = (lesUur + 1);
			document.getElementById("TTVLvv").innerHTML = "-----";
			document.getElementById("TTVLvl").innerHTML = "-"
        } else { //of als je wel les hebt
            TTVLvak = VakReplace(document.getElementById(TTVLtag).innerHTML.split("<br>")[0]);
            TTVLlok = document.getElementById(TTVLtag).innerHTML.split("<br>")[2].replace("1","");
		    document.getElementById("TTVLvu").innerHTML = (lesUur + 1);
            if (TTVLlok.length > 2){document.getElementById("TTVLvl").innerHTML = TTVLlok}
            else{document.getElementById("TTVLvl").innerHTML = "-"}
		    document.getElementById("TTVLvv").innerHTML = TTVLvak
        }
		//document.getElementById("lesVolgende").innerHTML = MultiReplace(document.getElementById(TTVLtag).innerHTML.replace("&nbsp;","--------"),"<br>"," ")
		
		if (i == 3 || i == 6 || i == 9){ //pauze volgende uur
			if (i == 3){document.getElementById("TTVLvu").innerHTML = "P1"}
			if (i == 6){document.getElementById("TTVLvu").innerHTML = "P2"}
			if (i == 9){document.getElementById("TTVLvu").innerHTML = "P3"}
			document.getElementById("TTVLvv").innerHTML = "Pauze";
			document.getElementById("TTVLvl").innerHTML = "-"
		}
		/*Ok, dit is een absolute puinhoop, ik weet het. Voorlopig werkt het echter, en gezien mijn beperkte ervaring met Javascript, vind ik dat al heel wat.*/
	} else {
        document.getElementById("TTVLhu").innerHTML = "-";
        document.getElementById("TTVLhv").innerHTML = "-----";
        document.getElementById("TTVLhl").innerHTML = "-";

        document.getElementById("TTVLt").innerHTML = "-------";

        document.getElementById("TTVLvu").innerHTML = "-";
        document.getElementById("TTVLvv").innerHTML = "-----";
        document.getElementById("TTVLvl").innerHTML = "-";
    }

    document.getElementsByTagName("table")[0].style.visibility = "hidden";
}
