window.addEventListener('DOMContentLoaded',init,false);
            
function init() {
    alert('The page loaded!');
    var buttons = document.getElementsByTagName("button")
    buttons[0].addEventListener('click',randomColor,false);
}

function randomColor() {
    //var red = (math.random * 256);
    //var blue = (math.random * 256);
    //var green = (math.random * 256);
    alert ('Function called');
    //var colorChange = document.getElementById("colorToggle");
    //{buttons[0].style.color = rgb(red, green, blue)}
    //{buttonChange.style.background-color = "skyblue"}
}