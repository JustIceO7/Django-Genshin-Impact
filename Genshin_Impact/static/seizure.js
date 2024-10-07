function handleDOMContentLoaded() {
    let audio = document.getElementById("background_music");
    audio.volume = 0.2;

    function adjustPlaybackSpeed() {
        audio.playbackRate = 2;
        audio.volume = 0.4;
        setTimeout(() => {
            audio.playbackRate = 1;
            audio.volume = 0.2
            setTimeout(() => {
                audio.playbackRate = 1.5;
                audio.volume = 0.3
            }, 2000); 
        }, 10000); 
    }

    function startSpeedChange() {
        adjustPlaybackSpeed();
        speedChangeInterval = setInterval(adjustPlaybackSpeed, 16000); 
    }

    startSpeedChange();
}

document.addEventListener("DOMContentLoaded", handleDOMContentLoaded);