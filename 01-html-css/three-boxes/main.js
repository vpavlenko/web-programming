function toggleYellow() {
    if (this.style.background == "blue") {
        this.style.background = "red";
    } else {
        this.style.background = "blue";
    }
}

var rects = document.getElementsByClassName("rect");
for (var i in rects) {
    rects[i].addEventListener("click", toggleYellow);   
}
