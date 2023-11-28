window.onload = function() {
    var calendarEl = document.getElementById('calendar');
    if (calendarEl){

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
    },
    dateClick : function(info) {
        var clickedDate = info.dateStr;
        window.location.href = '/bookings/event_create/?date=' + info.date.toISOString();
    },
});
calendar.render();
}


    let cells = document.querySelectorAll('.fc-time-slot');
    cells.forEach(function(cell) {
        cell.addEventListener('mouseover', function() {
            console.log(cell);
            let tooltip = document.createElement('span');
            tooltip.innerText = 'Click to add an event';
            tooltip.classList.add('tooltip');
            cell.appendChild(tooltip);
        });

        cell.addEventListener('mouseout', function() {
            if (cell.lastChild.classList.contains('tooltip')) {
                cell.removeChild(cell.lastChild);
            }
        });
    });

};
