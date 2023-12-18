const userIsSuperuser = window.userIsSuperuser;
let dayCount;
  if (isSmallDevice()) {
    dayCount=3;
  } else {
    dayCount=7;
  }
function isSmallDevice() {
    return window.innerWidth <= 768;
}

function getDayCount() {
    return isSmallDevice() ? 3 : 7;
}

function getVisibleRange(days) {
    let start = new Date();
    let end = new Date();
    end.setDate(start.getDate() + days);
    return { start: start, end: end };
}

function getHeaderContent(args) {
    let content;
    if (isSmallDevice()) { // for small devices
        content = args.date.toLocaleDateString(LANGUAGE_CODE, { day: '2-digit', month: '2-digit' });
    } else {
        content = args.date.toLocaleDateString(LANGUAGE_CODE, { weekday: 'long', month: 'long', day: 'numeric' });
    }
    return content;
}

function getEventContent(arg) {
    let content = document.createElement('div');
    content.className = 'event-details';
    let title = document.createElement('strong');
    title.textContent = arg.event.title;
    content.appendChild(title);
    return { domNodes: [content] };
}

function handleEventClick(arg) {
    // Navigate to the detail page using the slug or any other identifier
    window.location.href = '/bookings/event_detail/' + arg.event.extendedProps.slug + '/';
}

function handleDateClick(info) {
    const clickedDate = info.dateStr;
    var currentDate = new Date();  // Get the current date and time
    var clickedDateTime = new Date(clickedDate);

    // Check if the clicked date is in the past
    if (clickedDateTime < currentDate) {
        alert('Cannot create events in the past.');
        return;
    }
    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'  };
    var formattedDate = new Date(clickedDate).toLocaleDateString('fr-FR', options);
    // Create the modal
    var modal = document.createElement('div');
    modal.classList.add('d-flex','flex-column');
    modal.id = 'choiceModal';
    if (userIsSuperuser) {  // Replace this with the actual condition
        modal.innerHTML = `
            <div class="rounded-lg bg-dark">
            <div class="modal-header text-light bg-dark w-100 border-0">
                <h1 class="modal-title">Choose an action</h1>
                <button id="closeModal" class="p-2 rounded bg-danger text-light">X</button>
            </div>
            <div class="modal-body rounded d-flex justify-content-around w-80 bg-warning mb-3">
                <button id="createCourse" class="rounded bg-dark text-light shadow-lg" >Create Course</button>
                <button id="createUnavailablePeriod" class="rounded bg-dark text-light shadow-lg" >Add Unavailable Period</button>
                </div>
                <span class="text-light">on ${formattedDate}</span>
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
            if(modalBackdrop){
                modalBackdrop.parentNode.removeChild(modalBackdrop);
            }
            modal.parentNode.removeChild(modal);
            document.body.style.overflow = 'auto';
        });
    } else {
        modal.innerHTML = `
        <div class="rounded-lg bg-dark">
        <div class="modal-header text-light bg-dark w-100 border-0">
            <h1 class="modal-title">Choose an action</h1>
            <button id="closeModal" class="p-2 rounded bg-danger text-light">X</button>
        </div>
        <div class="modal-body rounded d-flex justify-content-around w-80 bg-warning mb-3">
            <button id="createPrivateSession" class="rounded bg-dark text-light shadow-lg" >Create Private Session</button>
            
            </div>
            <span class="text-light">on ${formattedDate}</span>
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
            if(modalBackdrop){
                modalBackdrop.parentNode.removeChild(modalBackdrop);
            }
            modal.parentNode.removeChild(modal);
            document.body.style.overflow = 'auto';
        });
    }

    // Display the modal
    $('#choiceModal').modal('show');
}
function addTooltipToCells() {
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
}
function fetchEvents(fetchInfo, successCallback, failureCallback) {
    $.ajax({
        url: '/bookings/get_all_events/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            successCallback(data);
        },
        error: function() {
            failureCallback('There was an error while fetching events.');
        },
    });
}


window.onload = function() {
    let calendarEl = document.getElementById('calendar');
    if (calendarEl){
        var calendar = new FullCalendar.Calendar(calendarEl, {
            dayHeaderDidMount: function(args) {
                var content;
                if (window.innerWidth <= 768) { // for small devices
                    content = args.date.toLocaleDateString(LANGUAGE_CODE, { day: '2-digit', month: '2-digit' });
                } else {
                    content = args.date.toLocaleDateString(LANGUAGE_CODE, { weekday: 'long', month: 'long', day: 'numeric' });
                }
                args.el.innerHTML = content;
            },
            locale: LANGUAGE_CODE,
            initialView:'timeGrid',
            views: {
                timeGrid: {
                  dayCount: dayCount
                }
              },
            firstDay: 1,
            slotLabelFormat: {
                hour: '2-digit',
                minute: '2-digit',
                hour12: false
            },
            eventTimeFormat: {
                hour: '2-digit',
                minute: '2-digit',
                hour12: false
            },
            slotMinTime:"8:00:00",
            slotMaxTime:"19:00:00",
            expandRows:true,
            height: 'auto',
            nowIndicator:true,
            themeSystem: 'bootstrap',
            events: fetchEvents, 
            eventContent: getEventContent,
            eventClick: handleEventClick,
            dateClick: handleDateClick,
        });
        calendar.render();
    }

    addTooltipToCells();
};