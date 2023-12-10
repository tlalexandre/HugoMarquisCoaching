function adjustFontSize() {
    var elements = document.getElementsByClassName('dynamic-font-size');
    var maxAllowedFontSize = 90; // Set your maximum allowed font size

    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];
        var parent = element.closest('.card-body'); // Select the closest parent with the class 'card-body'
        var parentWidth = parent.offsetWidth;
        var parentHeight = parent.offsetHeight;

        var textLength = element.textContent.length; // Get the length of the text string
        var divisor = textLength / 3.2; // Adjust the divisor to a smaller value
        var maxFontSize = parentHeight / divisor; // Calculate the maximum font size based on the length of the text string

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
    var parentElements = document.querySelectorAll('.card-body'); // Select all .card-body elements
    var textElements = document.querySelectorAll('.dynamic-font-size'); // Select all .dynamic-font-size elements

    for (var i = 0; i < parentElements.length; i++) {
        var backgroundImage = window.getComputedStyle(parentElements[i]).backgroundImage;
        var imageUrl = backgroundImage.split(',').pop().trim(); // Extract the URL of the image from the background image
        textElements[i].style.backgroundImage = imageUrl;
    }

    adjustFontSize();
};

window.onresize = function() {
    adjustFontSize();
};