document.getElementsByClassName("landing").style.backgroundImage.src = "IMG-20220504-WA0005.jpg"

function next(){

    var image = document.getElementById("slide1").src

    if (image =="slide1.png") {
        slideFunction2()
    }

    if (image =="slide2.png") {
        slideFunction3()
    }
    if (image =="slide3.png") {
        slideFunction1()
    }
}

function previous(){

var image = document.getElementById("slide1").src

if (image =="slide1.png") {
    slideFunction3()
}

if (image =="slide2.png") {
    slideFunction1()
}
if (image =="slide3.png") {
    slideFunction2()
}
}

function slideFunction1(curent)
{
    document.getElementById("slide1").src ="slide1.png"
    setTimeout(() => {
        slideFunction2()
    }, 3000);
}



function slideFunction2(curent)
{
     document.getElementById("slide1").src = "slide2.png"

    setTimeout(() => {
        slideFunction3()
    }, 3000);
}



function slideFunction3(curent)
{
    document.getElementById("slide1").src = "slide3.png"
    setTimeout(() => {
        slideFunction1()
    }, 3000);
}
slideFunction1(1)

// script for the red more buton


 var read = document.getElementById("toggle")
    
 read.onclick = expand()
 function expand() {
      console.log("cliqed")
    var elem = document.getElementById("toggle").textContent;
    if (elem == "Read More") {
      //Stuff to do when btn is in the read more state
      document.getElementById("toggle").textContent="Read Less";
      document.getElementById("textt").slideDown;
    } else {
      //Stuff to do when btn is in the read less state
      document.getElementById("toggle").text("Read More");
      document.getElementById("textt").slideUp();
    }
  };