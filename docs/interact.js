window.addEventListener('DOMContentLoaded',init,false);
            
var switched = false;
function init() {
    var buttons = document.getElementsByTagName("button")
    buttons[0].addEventListener('click', switchColors, false);
}

function switchColors() {
    var divCollection = document.getElementsByTagName("div")
        for (var i = 0; i < divCollection.length; i++) {
        if (divCollection[i].className == "white") {
            divCollection[i].classList.remove("white");
            divCollection[i].classList.add("black");
        } else if (divCollection[i].className == "black") {
            divCollection[i].classList.remove("black");
            divCollection[i].classList.add("white");
        }
 }
}