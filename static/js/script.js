document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'timeGridWeek',
      firstDay: 1,
      slotMinTime:"8:00:00",
      slotMaxTime:"18:00:00",
      nowIndicator:true,
      events:'/bookings/get_events/',
      eventContent: function(arg) {
        var content = document.createElement('div');
        content.className = 'event-details';
        var title = document.createElement('strong');
        title.textContent = arg.event.title;
        content.appendChild(title);
        return { domNodes: [content] };
    }
    });
    calendar.render();
});
console.log(events)