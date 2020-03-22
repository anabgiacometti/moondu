$(document).ready(function() {

    TweenLite.set(".aboutsvg", {
        stroke: 'white',
        strokeDasharray: 60,
    });

    TweenLite.to(".aboutsvg", 5, {
        strokeDasharray: 70,
        repeat: -1,
        yoyo: true
    });

})



function ShowSlide(number) {

    if (ActiveSlide < number) {

        $('p').removeClass("fadeInDown")

        var previous_slide = document.getElementsByClassName("slider")[ActiveSlide - 1]
        previous_slide.classList.remove("fadeInLeft")
        previous_slide.classList.add("fadeOutRight")

        var current_slide = document.getElementsByClassName("slider")[number - 1]
        current_slide.classList.remove("fadeOutRight", "fadeOutLeft")
        current_slide.classList.add("fadeInLeft")
        current_slide.classList.remove("invisible")

    } else if (ActiveSlide > number) {

        $('p').removeClass("fadeInDown")

        var previous_slide = document.getElementsByClassName("slider")[ActiveSlide - 1]
        previous_slide.classList.remove("fadeInRight")
        previous_slide.classList.add("fadeOutLeft")

        var current_slide = document.getElementsByClassName("slider")[number - 1]
        current_slide.classList.remove("fadeOutRight", "fadeOutLeft")
        current_slide.classList.add("fadeInRight")

    }

    var next_dot = document.getElementsByClassName("slider-dot")[number - 1]
    var previous_dot = document.getElementsByClassName("slider-dot")[ActiveSlide - 1]

    previous_dot.classList.add("inactive")
    next_dot.classList.remove("inactive")

    ActiveSlide = number

}

function ShowVideo() {
    var video = document.getElementsByClassName("video")[ActiveSlide - 1]
    video.classList.remove("invisible")
    video.classList.remove("fadeOutRightBig")
    video.classList.add("fadeInRightBig")

    var button = document.getElementsByClassName("button-primary")[ActiveSlide - 1]
    button.classList.remove("delay-1s")
    button.classList.remove("fadeInDown")
    button.classList.add("fadeOutLeftBig")

    var text = document.getElementsByClassName("video-text")[ActiveSlide - 1]
    text.classList.remove("delay-0-5s")
    text.classList.remove("fadeInDown")
    text.classList.add("fadeOutLeftBig")
}


function ShowText() {
    var video = document.getElementsByClassName("video")[ActiveSlide - 1]
    video.classList.add("fadeOutRightBig")
    video.classList.remove("fadeInRightBig")

    var button = document.getElementsByClassName("button-primary")[ActiveSlide - 1]
    button.classList.remove("fadeOutLeftBig")
    button.classList.add("fadeInLeftBig")

    var text = document.getElementsByClassName("video-text")[ActiveSlide - 1]
    text.classList.remove("fadeOutLeftBig")
    text.classList.add("fadeInLeftBig")
}


function ShowAboutVideo() {
    var video = document.getElementById("aboutvideo")
    video.classList.remove("invisible")
    video.classList.remove("fadeOutRightBig")
    video.classList.add("fadeInRightBig")

    var button = document.getElementById("button-aboutvideo")
    button.classList.remove("delay-1s")
    button.classList.remove("fadeInDown")
    button.classList.add("fadeOutLeftBig")

    var text = document.getElementById("abouttext")
    text.classList.remove("delay-0-5s")
    text.classList.remove("fadeInDown")
    text.classList.add("fadeOutLeftBig")
}


function ShowAboutText() {
    var video = document.getElementById("aboutvideo")
    video.classList.add("fadeOutRightBig")
    video.classList.remove("fadeInRightBig")

    var button = document.getElementById("button-aboutvideo")
    button.classList.remove("fadeOutLeftBig")
    button.classList.add("fadeInLeftBig")

    var text = document.getElementById("abouttext")
    text.classList.remove("fadeOutLeftBig")
    text.classList.add("fadeInLeftBig")
}