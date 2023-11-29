var clickedDate;
var userIsSuperuser =window.userIsSuperuser;
console.log(userIsSuperuser);
window.onload = function() {
    var calendarEl = document.getElementById('calendar');
    if (calendarEl){

        var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'timeGridWeek',
            firstDay: 1,
            slotMinTime:"8:00:00",
            slotMaxTime:"18:00:00",
            nowIndicator:true,
            events:
            function (info, successCallback, failureCallback) {
                // Make AJAX request for all events
                $.ajax({
                    url: '/bookings/get_all_events/',
                    type: 'GET',
                    dataType: 'json',
                    success: function (data) {
                        // Call successCallback with the events
                        console.log(data);
                        successCallback(data);
                    },
                    error: function () {
                        failureCallback('There was an error fetching events.');
                    }
                });
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
        clickedDate = info.dateStr;
        // Create the modal
        var modal = document.createElement('div');
        modal.id = 'choiceModal';
        if (userIsSuperuser) {  // Replace this with the actual condition
            modal.innerHTML = `
                <div>
                    <h1>Choose an action</h1>
                    <button id="createCourse">Create Course</button>
                    <button id="createUnavailablePeriod">Add Unavailable Period</button>
                    <span>on ${clickedDate}</span>
                    <button id="closeModal">X</button>
                </div>
            `;
            document.body.appendChild(modal);
    
            // Add event listeners to the buttons
            document.getElementById('createCourse').addEventListener('click', function() {
                window.location.href = '/bookings/event_create/?date=' + clickedDate + '&type=course';
            });
            document.getElementById('createUnavailablePeriod').addEventListener('click', function() {
                window.location.href = '/bookings/unavailable_period/add/?date=' + clickedDate;
            });
            document.getElementById('closeModal').addEventListener('click', function() {
                var modal = document.getElementById('choiceModal');
                var modalBackdrop = document.querySelector('.modal-backdrop');
                modalBackdrop.parentNode.removeChild(modalBackdrop);
                modal.parentNode.removeChild(modal);
            });
        } else {
            modal.innerHTML = `
                <div>
                    <h1>Choose an action</h1>
                    <button id="createPrivateSession">Create Private Session</button>
                    <span>on ${clickedDate}</span>
                    <button id="closeModal">X</button>
                </div>
            `;
            document.body.appendChild(modal);
    
            // Add event listener to the button
            document.getElementById('createPrivateSession').addEventListener('click', function() {
                window.location.href = '/bookings/event_create/?date=' + clickedDate  + '&type=private_session';
            });
            document.getElementById('closeModal').addEventListener('click', function() {
                var modal = document.getElementById('choiceModal');
                var modalBackdrop = document.querySelector('.modal-backdrop');
                modalBackdrop.parentNode.removeChild(modalBackdrop);
                modal.parentNode.removeChild(modal);
            });
        }

        // Display the modal
        $('#choiceModal').modal('show');
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
