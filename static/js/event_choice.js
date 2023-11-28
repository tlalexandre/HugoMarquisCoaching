// Create the modal
console.log(clickedDate);
var modal = document.createElement('div');
modal.id = 'choiceModal';
modal.innerHTML = `
    <div>
        <h1>Choose an action</h1>
        <button id="createCourse">Create Course</button>
        <button id="createUnavailablePeriod">Add Unavailable Period</button>
        <span>on ${clickedDate}</span>
    </div>
`;
document.body.appendChild(modal);

// Add event listeners to the buttons
document.getElementById('createCourse').addEventListener('click', function() {
    window.location.href = '/bookings/event_create/?date=' + clickedDate;
});
document.getElementById('createUnavailablePeriod').addEventListener('click', function() {
    window.location.href = '/bookings/unavailable_periods/add/?date=' + clickedDate;
});