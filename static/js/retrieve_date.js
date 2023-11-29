var url = new URL(window.location.href);
// Use the URL API to parse the URL
// Use the `searchParams` property of the URL object to get the `date` query parameter
var clickedDate = url.searchParams.get('date');
var start_time_element = document.getElementById('start_time');
var end_time_element = document.getElementById('end_time');
var id_start_time_element = document.getElementById('id_start_time');
var id_end_time_element = document.getElementById('id_end_time');

var date= new Date(clickedDate);

var dateTime = date.getFullYear() + '-' +
    ('0' + (date.getMonth()+1)).slice(-2) + '-' +
    ('0' + date.getDate()).slice(-2) + 'T' +
    ('0' + date.getHours()).slice(-2) + ':' +
    ('0' + date.getMinutes()).slice(-2);

// Now you can use `clickedDate` to prepopulate the start time field of the form

date.setTime(date.getTime() + 3600000);

var endDateTime = date.getFullYear() + '-' +
    ('0' + (date.getMonth()+1)).slice(-2) + '-' +
    ('0' + date.getDate()).slice(-2) + 'T' +
    ('0' + date.getHours()).slice(-2) + ':' +
    ('0' + date.getMinutes()).slice(-2);


if (start_time_element) {
    start_time_element.value = dateTime;
}

if (end_time_element) {
    end_time_element.value = endDateTime;
}

if (id_start_time_element) {
    id_start_time_element.value = dateTime;
}

if (id_end_time_element) {
    id_end_time_element.value = endDateTime;
} 