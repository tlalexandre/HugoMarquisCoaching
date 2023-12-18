function adjustFontSize() {
    var elements = document.querySelectorAll('.masthead h1.dynamic-font-size, .card-body h2.dynamic-font-size');
    var minFontSize = 30; // Set a larger minimum possible font size
    var buffer = 30; // Set a buffer value to prevent the text from being too close to the edge of the parent
    var factor = 1.8; // Set a factor to adjust the calculated font size

    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];
        var parent = element.closest('.masthead, .card-body'); // Select the closest parent with the class 'card-body'
        var parentWidth = parent.offsetWidth;
        var parentHeight = parent.offsetHeight;

        // Apply the buffer only if the parent has the class 'masthead'
        if (parent.classList.contains('masthead')) {
            parentWidth -= buffer;
            parentHeight -= buffer;
        }

        var area = parentWidth * parentHeight; // Calculate the area of the parent container
        var textLength = element.textContent.length; // Get the length of the text
        var maxFontSize = Math.sqrt(area / textLength) / factor; // Calculate the initial font size based on the square root of the area divided by the text length

        element.style.fontSize = maxFontSize + 'px'; // Set the initial font size
        element.style.lineHeight = '1.2'; // Set the initial line height

        // Gradually decrease the font size until the text fits within the container
        while (element.offsetWidth > parentWidth || element.offsetHeight > parentHeight) {
            maxFontSize -= 5; // Decrease the font size by 5
            element.style.fontSize = maxFontSize + 'px'; // Update the font size
            element.style.lineHeight = '1.2'; // Update the line height

            // If the font size reaches minFontSize, break the loop
            if (maxFontSize <= minFontSize) {
                break;
            }
        }
    }
}

window.onload = function() {
    var parentElements = document.querySelectorAll('.masthead, .card-body'); // Select all .masthead and .card-body elements
    var textElements = document.querySelectorAll('.masthead h1.dynamic-font-size, .card-body h2.dynamic-font-size'); // Select all .dynamic-font-size elements within .masthead h1 and .card-body h2

    for (var i = 0; i < parentElements.length; i++) {
        var backgroundImage = window.getComputedStyle(parentElements[i]).backgroundImage;
        var backgroundPosition = window.getComputedStyle(parentElements[i]).backgroundPosition;
        var backgroundSize = window.getComputedStyle(parentElements[i]).backgroundSize;
        var backgroundRepeat = window.getComputedStyle(parentElements[i]).backgroundRepeat;
        var imageUrl = backgroundImage.split(',').pop().trim(); // Extract the URL of the image from the background image
        textElements[i].style.backgroundImage = imageUrl;
        textElements[i].style.backgroundPosition = backgroundPosition;
        textElements[i].style.backgroundSize = backgroundSize;
        textElements[i].style.backgroundRepeat = backgroundRepeat;
    }

    adjustFontSize();
};

window.onresize = function() {
    adjustFontSize();
};