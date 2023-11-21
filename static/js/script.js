document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'timeGridWeek',
      firstDay: 1,
      slotMinTime:"8:00:00",
      slotMaxTime:"18:00:00",
      nowIndicator:true,
      events: function (info, successCallback, failureCallback) {
        // Array to store all events
        var allEvents = [];

        // Make AJAX request for the first set of events
        $.ajax({
            url: '/bookings/get_courses/',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // Push events from the first source to the array
                allEvents.push(...data);
                // Continue to the next AJAX request
                fetchPrivateSessions();
            },
            error: function () {
                failureCallback('There was an error fetching events.');
            }
        });

        // Function to make AJAX request for the second set of events
        function fetchPrivateSessions() {
            $.ajax({
                url: '/bookings/get_private_sessions/',
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    // Push events from the second source to the array
                    allEvents.push(...data);
                    // Call successCallback with the combined events
                    successCallback(allEvents);
                },
                error: function () {
                    failureCallback('There was an error fetching events.');
                }
            });
        }
    },
      eventContent: function(arg) {
        var content = document.createElement('div');
        content.className = 'event-details';
        var title = document.createElement('strong');
        title.textContent = arg.event.title;
        content.appendChild(title);
        return { domNodes: [content] };
    },
    eventClick: function (arg) {
      // Navigate to the detail page using the slug or any other identifier
      window.location.href = '/bookings/event_detail/' + arg.event.extendedProps.slug + '/';
  }
    });
    calendar.render();
});
