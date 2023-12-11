function adjustFontSize() {
    var elements = document.querySelectorAll('.masthead h1.dynamic-font-size, .card-body h2.dynamic-font-size');
    var maxAllowedFontSize = 100; // Set your maximum allowed font size
    var buffer = 30; // Set a buffer value to prevent the text from being too close to the edge of the parent

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

        var textLength = element.textContent.length; // Get the length of the text string
        var divisor = textLength / 5; // Adjust the divisor to a smaller value
        var maxFontSizeHeight = parentHeight / divisor; // Calculate the maximum font size based on the length of the text string
        var maxFontSizeWidth = parentWidth / divisor; // Calculate the maximum font size based on the width of the parent
        var maxFontSize = Math.min(maxFontSizeHeight, maxFontSizeWidth); // Use the smaller of the two as the maximum font size

        var minFontSize = 0; // Minimum possible font size

        var iterations = 0; // Count the number of iterations
        while (maxFontSize - minFontSize > 1 && iterations < 1000) { // Limit the number of iterations to 1000
            var midFontSize = Math.floor((minFontSize + maxFontSize) / 2);
            element.style.fontSize = midFontSize + 'px';
            element.style.lineHeight = '0.8'; // Set the line-height to 1

            if (element.offsetWidth > parentWidth || element.offsetHeight > parentHeight) {
                maxFontSize = midFontSize;
            } else {
                minFontSize = midFontSize;
            }

            iterations++; // Increment the number of iterations
        }

        // Cap the font size at the maximum allowed value
        if (minFontSize > maxAllowedFontSize) {
            minFontSize = maxAllowedFontSize;
        }

        element.style.fontSize = minFontSize + 'px';
        element.style.lineHeight = '0.8'; // Set the line-height to 1
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