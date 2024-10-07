function change_theme(event) {
    event.stopPropagation();
    event.preventDefault();
    if (document.getElementById("theme-mode").src.endsWith(darkModeImageUrl)) {
        document.getElementById("theme-mode").src = lightModeImageUrl;
        document.documentElement.style.setProperty("--background_veil", "lightgrey");
        sendThemeMode("dark");
    } else {
        document.getElementById("theme-mode").src = darkModeImageUrl;
        document.documentElement.style.setProperty("--background_veil", "whitesmoke");
        sendThemeMode("light");
    }
}

function getCsrfToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}

function sendThemeMode(themeMode) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/set-theme-mode/", true);

    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // Get the CSRF token from the meta tag
    var csrfToken = getCsrfToken();

    // Send the mode and the CSRF token
    xhr.send("theme_mode=" + themeMode + "&csrfmiddlewaretoken=" + csrfToken);
}


