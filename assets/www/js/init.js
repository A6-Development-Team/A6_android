/**
 * Created with JetBrains WebStorm.
 * User: Léon
 * Date: 20-2-13
 * Time: 10:34
 * To change this template use File | Settings | File Templates.
 */
var tijdNu = new Date();
function TTVLrepeater(){
    if ((tijdNu.getHours()*60+tijdNu.getMinutes()) < 990){
        var t = document.getElementById("TTVLt").innerHTML.replace(" min","");
        if(t>0 && (t%10 != 0)){
            t -= 1;
            document.getElementById("TTVLt").innerHTML =  t + " min";
        } else {
            TijdVolgendeUur();
        }
    }
}
var repeater = setInterval(TTVLrepeater,60000);
document.addEventListener("resume", onresume, true);
document.addEventListener("deviceready", initPushwoosh, true);
$(window).bind('pageshow', function() { pageshow(); });
function onresume() {clearInterval(repeater); var repeater = setInterval(TTVLrepeater,30000);}
function init() { $('#rooster').load(localStorage.leerling, function() { TijdVolgendeUur(); });};
function pageshow() {init();}