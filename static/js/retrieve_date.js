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
document.getElementById('start_time').value = dateTime;