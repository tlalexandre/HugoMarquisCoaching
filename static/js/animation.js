window.onload = function() {
    var heroContainer = document.querySelector('.hero-container');

    if (!localStorage.getItem('alreadyVisited')) {
        // Play the animation
        heroContainer.classList.add('shrink');

        // Set the flag in localStorage
        localStorage.setItem('alreadyVisited', 'true');
    } else {
        // Set the width and height to their normal values
        heroContainer.classList.add('normal-size');
    }
}