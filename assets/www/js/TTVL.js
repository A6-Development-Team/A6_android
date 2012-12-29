function MultiReplace(str, match, repl) {
	return str.split(match).join(repl);
	/*str.replace() vervangt maar 1 keer godverdomme,
	moet ik weer creatief gaan lopen doen om alle <br>'s eruit te krijgen*/
}
function TijdVolgendeUur() {
	var tijdNu = new Date(),
	tijdVolgendeUur = new Date(),
	lesUren = [],
    tijdVerschil;
	tijdNu.setHours(10);
	tijdNu.setMinutes(39);
    tijdNu.setDate(28);
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
		
		var TTVLtag = "TTVLd" + tijdNu.getDay() + "u" + lesUur;
		
		if (lesUur > 0){
			if (document.getElementById(TTVLtag).innerHTML == "&nbsp;"){ //in geval van tussenuur/uit
				document.getElementById("TTVLhu").innerHTML = lesUur;
				document.getElementById("TTVLhv").innerHTML = "-----";
				document.getElementById("TTVLhl").innerHTML = "-"
			}else{
				document.getElementById("TTVLhu").innerHTML = lesUur;
				document.getElementById("TTVLhl").innerHTML = document.getElementById(TTVLtag).innerHTML.split("<br>")[2];
				document.getElementById("TTVLhv").innerHTML = document.getElementById(TTVLtag).innerHTML.split("<br>")[0]}
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

		document.getElementById("tijdVerschil").innerHTML = "Nog <b>" + tijdVerschil + " minuten</b> tot " + lesUren[i].uurNaam;
		
		TTVLtag = "TTVLd" + tijdNu.getDay() + "u" + (lesUur + 1);

		if (document.getElementById(TTVLtag).innerHTML == "&nbsp;"){ //in geval van tussenuur/uit
			document.getElementById("TTVLvu").innerHTML = (lesUur + 1);
			document.getElementById("TTVLvv").innerHTML = "-----";
			document.getElementById("TTVLvl").innerHTML = "-"}
		else { //of als je wel les hebt
		document.getElementById("TTVLvu").innerHTML = (lesUur + 1);
		document.getElementById("TTVLvl").innerHTML = document.getElementById(TTVLtag).innerHTML.split("<br>")[2];
		document.getElementById("TTVLvv").innerHTML = document.getElementById(TTVLtag).innerHTML.split("<br>")[0]}
		//document.getElementById("lesVolgende").innerHTML = MultiReplace(document.getElementById(TTVLtag).innerHTML.replace("&nbsp;","--------"),"<br>"," ")
		
		if (i == 3 || i == 6 || i == 9){ //pauze volgende uur
			if (i == 3){document.getElementById("TTVLvu").innerHTML = "P1"}
			if (i == 6){document.getElementById("TTVLvu").innerHTML = "P2"}
			if (i == 9){document.getElementById("TTVLvu").innerHTML = "P3"}
			document.getElementById("TTVLvv").innerHTML = "Pauze";
			document.getElementById("TTVLvl").innerHTML = "-"
		}
		
		/*Ok, dit is een absolute puinhoop, ik weet het. Voorlopig werkt het echter, en gezien mijn beperkte ervaring met Javascript, vind ik dat al heel wat.*/
	}
}
