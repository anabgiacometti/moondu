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

    var button = document.getElementsByClassName("button_video")[ActiveSlide - 1]
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

    var button = document.getElementsByClassName("button_video")[ActiveSlide - 1]
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

    var button = document.getElementById("about-button-video")
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

    var button = document.getElementById("about-button-video")
    button.classList.remove("fadeOutLeftBig")
    button.classList.add("fadeInLeftBig")

    var text = document.getElementById("abouttext")
    text.classList.remove("fadeOutLeftBig")
    text.classList.add("fadeInLeftBig")
}

function getContactFormData(form) {
    // creates a FormData object and adds chips text
    var formData = new FormData(document.getElementById(form));
    //    for (var [key, value] of formData.entries()) { console.log('formData', key, value);}
    return formData
}

function send_form(form, form_id, url, type, inner_ajax, formData) {
    // form validation and sending of form items

    if (form[0].checkValidity() && isFormDataEmpty(formData) == false) { // checks if form is empty
        event.preventDefault();

        // inner AJAX call
        inner_ajax(url, type, formData);

    } else {
        // first, scan the page for labels, and assign a reference to the label from the actual form element:
        var labels = document.getElementsByTagName('LABEL');
        for (var i = 0; i < labels.length; i++) {
            if (labels[i].htmlFor != '') {
                var elem = document.getElementById(labels[i].htmlFor);
                if (elem)
                    elem.label = labels[i];
            }
        }

        // then find all invalid input elements (form fields)
        var Form = document.getElementById(form_id);
        var invalidList = Form.querySelectorAll(':invalid');

        if (typeof invalidList !== 'undefined' && invalidList.length > 0) {
            // errors were found in the form (required fields not filled out)

            // for each invalid input element (form field) return error
            for (var item of invalidList) {
                item.classList += " border-danger"
            }
            M.toast({ html: "Por favor, preencha todos os campos.", classes: 'bg-danger text-white' });

        } else {
            M.toast({ html: "Desculpe, ocorreu um erro. Tente novamente.", classes: 'bg-danger text-white' });
        }
    }
}


function isFormDataEmpty(formData) {
    // checks for all values in formData object if they are empty
    for (var [key, value] of formData.entries()) {
        if (key != 'csrf_token') {
            if (value != '' && value != []) {
                return false;
            }
        }
    }
    return true;
}

function modular_ajax(url, type, formData) {
    // Most simple modular AJAX building block
    $.ajax({
        url: url,
        type: type,
        data: formData,
        processData: false,
        contentType: false,
        beforeSend: function() {
            // show the preloader (progress bar)
            $('#form-response').html("<div class='progress'><div class='indeterminate'></div></div>");
        },
        complete: function() {
            // hide the preloader (progress bar)
            $('#form-response').html("");
        },
        success: function(data) {
            if (!$.trim(data.feedback)) { // response from Flask is empty
                toast_error_msg = "An empty response was returned.";
                toast_category = "danger";
            } else { // response from Flask contains elements
                toast_error_msg = data.feedback;
                toast_category = data.category;
                $("input").attr("readonly", true)
                $("form").find("button").attr("disabled", true)
            }
        },
        error: function(xhr) {
            console.log("error. see details below.");
            console.log(xhr.status + ": " + xhr.responseText);
            toast_error_msg = "Ocorreu um erro";
            toast_category = "danger";
        },
    }).done(function() {
        M.toast({ html: toast_error_msg, classes: 'bg-' + toast_category + ' text-white' });

    });
};

var csrf_token = "{{ csrf_token() }}";

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        }
    }
});