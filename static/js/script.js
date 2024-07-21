document.getElementById('clear').addEventListener('click', function () {
    document.getElementById('prompt').value = '';

});

document.getElementById('speakButton').addEventListener('change', function () {
    const responseText = document.getElementById('response').innerText;
    if (this.checked) {

        if ('speechSynthesis' in window) {
            const utterance = new SpeechSynthesisUtterance(responseText);
            utterance.pitch = 1;
            utterance.rate = 1;
            utterance.volume = 1;
            utterance.lang = 'en-US';
            window.speechSynthesis.speak(utterance);
            utterance.onend = function (event) {
                console.log('Speech has finished after ' + event.elapsedTime + ' milliseconds.');
            };
            utterance.onerror = function (event) {
                console.error('SpeechSynthesisUtterance.onerror', event);
            };

        } else {
            alert('Your browser does not support speech synthesis.');
        }
    } else {
        window.speechSynthesis.cancel();
    }
});

document.getElementById('speakButton').addEventListener('change', function () {
    const alertBox = document.getElementById('customAlert');
    alertBox.style.display = 'block';
    if (this.checked) {
        setTimeout(() => {
            alertBox.style.display = 'none';
        }, 10000); // 10 seconds
    } else {
        alertBox.style.display = 'none';
    }
});

// for accessibility only
document.getElementById("speakButton").addEventListener("change", function () {
    this.setAttribute("aria-checked", this.checked);
});