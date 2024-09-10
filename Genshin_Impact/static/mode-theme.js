

function change_theme(event) {
    event.stopPropagation();
    event.preventDefault();    
    if (document.getElementById("theme-mode").src.endsWith(darkModeImageUrl)) {
        document.getElementById("theme-mode").src = lightModeImageUrl;
        document.documentElement.style.setProperty("--background_veil", "lightgrey");
    } else {
        document.getElementById("theme-mode").src = darkModeImageUrl;
        document.documentElement.style.setProperty("--background_veil", "white");
    }
}