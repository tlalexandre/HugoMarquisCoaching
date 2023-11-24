function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$('#join-button').click(function() {
    console.log("Join button clicked");
    var courseId = $(this).data('course-id');
    $.ajax({
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        url: '/bookings/join_course/' + courseId + '/',
        type: 'POST',
        datatype: 'json',
        success: function(response) {
            alert(response.message);
        },
        error: function(response) {
            if (response.responseJSON) {
                alert(response.responseJSON.message);
            } else {
                alert('An error occurred');
            }
        }
    });
});