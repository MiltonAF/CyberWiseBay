function signinPass() {
    var tipo = document.getElementById("password-in");
    var show = document.getElementById("show-pass-in");
    var hide = document.getElementById("hide-pass-in");
    if (tipo.type == "password") {
        tipo.type = "text";
        show.style.display = "none";
        hide.style.display = "block";
    } else {
        tipo.type = "password";
        show.style.display = "block";
        hide.style.display = "none";
    }
}

function signupPass() {
    var tipo = document.getElementById("password-up1");
    var show = document.getElementById("show-pass-up1");
    var hide = document.getElementById("hide-pass-up1");
    if (tipo.type == "password") {        
        tipo.type = "text";
        show.style.display = "none";
        hide.style.display = "block";
    } else {
        tipo.type = "password";
        show.style.display = "block";
        hide.style.display = "none";
    }
}

function signupComfirmPass() {
    var tipo = document.getElementById("password-up2");
    var show = document.getElementById("show-pass-up2");
    var hide = document.getElementById("hide-pass-up2");
    if (tipo.type == "password") {
        tipo.type = "text";
        show.style.display = "none";
        hide.style.display = "block";
    } else {
        tipo.type = "password";
        show.style.display = "block";
        hide.style.display = "none";
    }
}