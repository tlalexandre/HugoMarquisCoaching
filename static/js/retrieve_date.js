var url = new URL(window.location.href);
console.log(url);
// Use the URL API to parse the URL
// Use the `searchParams` property of the URL object to get the `date` query parameter
var clickedDate = url.searchParams.get('date');
console.log(clickedDate);

var date= new Date(clickedDate);
console.log(date);

var dateTime = date.getFullYear() + '-' +
    ('0' + (date.getMonth()+1)).slice(-2) + '-' +
    ('0' + date.getDate()).slice(-2) + 'T' +
    ('0' + date.getHours()).slice(-2) + ':' +
    ('0' + date.getMinutes()).slice(-2);

// Now you can use `clickedDate` to prepopulate the start time field of the form
document.getElementById('id_start_time').value = dateTime;

date.setTime(date.getTime() + 3600000);
console.log(date);  // check the updated date

var endDateTime = date.getFullYear() + '-' +
    ('0' + (date.getMonth()+1)).slice(-2) + '-' +
    ('0' + date.getDate()).slice(-2) + 'T' +
    ('0' + date.getHours()).slice(-2) + ':' +
    ('0' + date.getMinutes()).slice(-2);

console.log(endDateTime);  // check the endDateTime string

document.getElementById('id_end_time').value = endDateTime;
console.log(document.getElementById('end_time').value);  // check the value of the end_time input field